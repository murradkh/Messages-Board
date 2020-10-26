from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, reverse
from .models import Message
from .forms import CreateMessageForm, UpdateMessageForm, DeleteMessageForm, SearchForm

import random

DEF_MSGS_PER_PAGE = 5


def home(request):
    if request.method == "GET":
        kwargs = request.GET
        msgs_per_page_query = {}
        search_query = {}
        if "search_title" in kwargs:
            messages = Message.objects.filter(title__contains=kwargs['search_title']).order_by('-created_on')
            search_query = {"search_title": kwargs['search_title']}
        else:
            messages = Message.objects.all().order_by('-created_on')

        if "msgs_per_page" in kwargs and kwargs.get("msgs_per_page").isdecimal() \
                and int(kwargs.get("msgs_per_page")) > 0:
            paginator = Paginator(messages, int(kwargs.get("msgs_per_page")))
            msgs_per_page_query.update({"msgs_per_page": kwargs['msgs_per_page']})
        else:
            paginator = Paginator(messages, DEF_MSGS_PER_PAGE)

        if "page" in kwargs:
            page_number = kwargs.get('page')
        else:
            page_number = 1
        page_obj = paginator.get_page(page_number)

        alert_context = {}
        if "success" in request.GET:
            alert_context.update({"display_success_alert": request.GET.get("success")})
        elif "error" in request.GET:
            alert_context.update({"display_error_alert": request.GET.get("error")})

        context = {
            'page_obj': page_obj,
            "pages_ind": range(1, paginator.num_pages + 1),
            "delete_form": DeleteMessageForm,
            "search_form": SearchForm,
            "search_query": urlencode(search_query),
            "msgs_per_page_query": urlencode(msgs_per_page_query),
            **alert_context
        }

        return render(request, "message_board.html", context)
    return redirect(reverse("home"))


def create(request):
    if request.method == 'GET':
        return render(request, "create_message.html", {"form": CreateMessageForm()})

    elif request.method == 'POST':
        form = CreateMessageForm(request.POST)
        if form.is_valid():
            context = {}
            if request.user.is_authenticated:
                message = Message(
                    title=form.cleaned_data["title"],
                    description=form.cleaned_data["message"],
                    user=request.user,
                )
            else:
                passcode = random.choice(range(1000, 10000))
                message = Message(
                    title=form.cleaned_data["title"],
                    description=form.cleaned_data["message"],
                    passcode=passcode
                )
                context.update({"passcode": passcode})

            message.save()
            return render(request, "success_create_message.html", context)
    return redirect(reverse("home"))


def update(request, msg_id):
    result = Message.objects.filter(pk=msg_id)

    if not len(result):
        return HttpResponseNotFound(f"<h1>No Message with id {msg_id} Found</h1>")
    message = result[0]

    if request.method == 'GET':
        form = UpdateMessageForm({"title": message.title, "message": message.description})
        return render(request, "edit_message.html", {"form": form})

    if request.method == 'POST':
        form = UpdateMessageForm(request.POST)
        if form.is_valid():
            message.title = form.cleaned_data['title']
            message.description = form.cleaned_data['message']
            if request.user.is_authenticated:
                if message.user == request.user:
                    message.save()
                    return render(request, "success_update_message.html")
                else:
                    return render(request, "edit_message.html",
                                  {"form": form, "display_error_alert": "Message doesn't belong to you!"})
            else:
                if form.cleaned_data.get('passcode') == message.passcode:
                    message.save()
                    return render(request, "success_update_message.html")
                else:
                    return render(request, "edit_message.html",
                                  {"form": form, "display_error_alert": "Incorrect Passcode Entered!"})
    return redirect(reverse("home"))


def delete(request, msg_id):
    result = Message.objects.filter(pk=msg_id)
    if not len(result):
        return HttpResponseNotFound(f"<h1>No Message with id {msg_id} Found</h1>")
    message = result[0]
    base_url = reverse(home)
    if request.user.is_authenticated:
        if request.user == message.user:
            message.delete()
            query_string = urlencode({'success': "Message has removed!"})
            url = '{}?{}'.format(base_url, query_string)
        else:
            query_string = urlencode({'error': "Message doesn't belong to you!"})
            url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
    else:
        if request.method == 'POST':
            form = DeleteMessageForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['passcode'] == message.passcode:
                    message.delete()
                    query_string = urlencode({'success': "Message has removed!"})
                    url = '{}?{}'.format(base_url, query_string)
                else:
                    query_string = urlencode({'error': "Incorrect Passcode Entered!"})
                    url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
    return redirect(reverse("home"))
