FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN pip install  pipenv

COPY . /pokedex

EXPOSE 8000

WORKDIR /pokedex

RUN useradd -ms /bin/bash user

USER user:1000

RUN pipenv install --deploy --ignore-pipfile

WORKDIR /pokedex/pokedex

CMD pipenv run python manage.py makemigrations && pipenv run python manage.py migrate && pipenv run python manage.py runserver 0.0.0.0:8000

