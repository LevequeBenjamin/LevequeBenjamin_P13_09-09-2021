# pull the official base image
FROM python:3.9

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONUNBUFFERED=1 \
    DEBUG=False \
    PORT=8000

ADD . /app

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . /app

EXPOSE 8000

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT