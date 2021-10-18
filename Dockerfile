FROM python:3.9.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY .env /code/
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD gunicorn my_site.wsgi:application
