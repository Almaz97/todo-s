FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create directory for the django user
RUN mkdir -p /home/django

# create the appropriate directories
ENV HOME=/home/django
ENV APP_HOME=/home/django/app
RUN mkdir $APP_HOME

RUN apk update \
  # psycopg2 dependencies
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  # Postgres
  && apk add postgresql-dev \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  && apk add postgresql-client

# copy project
COPY . $APP_HOME

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy entrypoint.sh.sh
COPY ./compose/entrypoint.sh .

COPY ./compose/start.sh .
RUN chmod +x entrypoint.sh start.sh

RUN addgroup -S django && adduser -S django -G django --uid 1000
RUN chown django:django -R start.sh entrypoint.sh

USER django

WORKDIR $APP_HOME

ENTRYPOINT ["/entrypoint.sh"]

