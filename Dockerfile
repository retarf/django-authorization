FROM        python:3.9.16
ENV         PYTHONBUFFERED 1 
ENV         PYTHONDONTWRITEBYTECODE 1

WORKDIR     /app
COPY        requirements.txt /app

RUN         apt update \
            && apt upgrade -y 

RUN         apt install -y apt-utils python3-setuptools vim
RUN         pip3 install --upgrade pip -r requirements.txt

COPY        . /app

EXPOSE      8000
CMD         gunicorn --bind 0.0.0.0:8000 cleancash.wsgi
