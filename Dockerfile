FROM python:3.5

RUN pip install python-telegram-bot

RUN mkdir /app
ADD . /app
WORKDIR /app

CMD python /app/bot.py
