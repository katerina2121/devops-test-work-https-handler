FROM ubuntu@sha256:962f6cadeae0ea6284001009daa4cc9a8c37e75d1f5191cf0eb83fe565b63dd7 AS build

ARG PYTHON_VERSION=3.10

RUN apt-get update && \
    apt-get install -y --no-install-recommends python${PYTHON_VERSION} && \
    rm -rf /var/lib/apt/lists/*

COPY --link --from=ghcr.io/astral-sh/uv:0.4 /uv /usr/local/bin/uv

ENV UV_PYTHON_DOWNLOADS=never \
    UV_LINK_MODE=copy

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,destination=/root/.cache/uv \
    uv sync --no-dev --no-install-project --frozen

COPY . .


ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    VIRTUAL_ENV=/app/.venv 

RUN addgroup --system appgroup && \
    adduser --system --uid 1000 --ingroup appgroup --disabled-password --no-create-home appuser && \
    chown -R 1000:1000 .

USER appuser

CMD ["python", "main.py"]