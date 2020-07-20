FROM python:3.8-alpine

LABEL maintainer="moh.salim.qazizada@gmail.com"

RUN mkdir /ng-app
COPY ./src /ng-app
WORKDIR /ng-app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
