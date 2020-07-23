FROM python:3.8-alpine

LABEL maintainer="moh.salim.qazizada@gmail.com"

RUN mkdir /app
COPY ./src /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
