FROM ubuntu:14.04
MAINTAINER Ted Scharff

ENV DEBIAN_FRONTEND noninteractive
ENV APPNAME wtfbot

EXPOSE 80 443

RUN apt-get update && apt-get install -y \
    python-pip python-dev uwsgi-plugin-python \
    nginx supervisor curl \
     libmysqlclient-dev
COPY deploy/init_uwsgi.conf /etc/init/uwsgi.conf
COPY deploy/nginx.conf /etc/nginx/sites-available/$APPNAME.conf
ADD deploy/uwsgi.ini /etc/uwsgi.ini
COPY deploy/supervisord.conf /etc/supervisor/conf.d/
COPY requirements.txt /home/docker/
RUN  pip install -r /home/docker/requirements.txt

COPY . /home/docker/$APPNAME

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/$APPNAME.conf /etc/nginx/sites-enabled/$APPNAME.conf \
    && echo "daemon off;" >> /etc/nginx/$APPNAME.conf

CMD ["supervisord", "-n"]
