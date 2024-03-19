FROM python:3.11.5 as requirements-stage

WORKDIR /tmp

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

FROM python:3.11.5-alpine3.17

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY app/ app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
