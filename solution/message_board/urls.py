from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create_message'),
    path('update/<int:msg_id>', views.update, name='update_message'),
    path('delete/<int:msg_id>', views.delete, name='delete_message'),
]
