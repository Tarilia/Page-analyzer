FROM python:3.10 as base

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWEITEBYTECODE 1

WORKDIR /page_analyzer

COPY pyproject.toml ./
COPY poetry.lock ./

RUN pip install "poetry==1.7.0"
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN poetry config virtualenvs.create false
RUN poetry config installer.max-workers 1

EXPOSE 5000

FROM base as dev

RUN poetry install --no-interaction --no-ansi
RUN poetry build
RUN python3 -m pip install --user --force-reinstall dist/*.whl
