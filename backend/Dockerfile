FROM python:3.12 AS prod
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1
ENV PYTHONPATH="/app"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt update && apt upgrade -y

RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi --no-root --without dev

COPY app/ ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM prod AS dev
RUN poetry install --no-interaction --no-ansi --no-root

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]