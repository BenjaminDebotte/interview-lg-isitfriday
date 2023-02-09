FROM python:3.8

ADD . /app
WORKDIR /app

RUN pip install poetry
RUN poetry install --no-dev

ENTRYPOINT [ "flask", "run", "src/main.py" ]
