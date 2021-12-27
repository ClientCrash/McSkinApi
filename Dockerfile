FROM python:3.9-bullseye
WORKDIR /usr/mcskinapi
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/mcskinapi/requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install gunicorn -y
COPY . /usr/mcskinapi/
EXPOSE 80

CMD gunicorn --workers 4 --bind 0.0.0.0:80 wsgi:app