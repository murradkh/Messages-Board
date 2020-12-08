FROM python:3.8
RUN mkdir -p /home/message-board && \
pip  install django requests
COPY ./solution /home/message-board
WORKDIR /home/message-board/
RUN python manage.py migrate
CMD ["python","manage.py","runserver", "0.0.0.0:8000"]
