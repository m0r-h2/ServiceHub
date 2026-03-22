FROM python:3.13-slim

# Берем uv из официального образа
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Ставим зависимости для сборки (build-essential нужен для некоторых либ)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Сначала только зависимости для кэша
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

# Копируем весь код проекта
COPY . .

# Добавляем корень проекта в пути поиска модулей Python
ENV PYTHONPATH=/app

EXPOSE 8000