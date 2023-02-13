FROM python:3.10 as requirements-stage

WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.10

WORKDIR /src

COPY --from=requirements-stage /tmp/requirements.txt /src/requirements.txt
RUN pip install  -r /src/requirements.txt
COPY . /src
EXPOSE 8000
CMD ["uvicorn", "app.main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]