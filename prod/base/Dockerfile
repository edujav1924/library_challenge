# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_USERNAME ${DJANGO_SUPERUSER_USERNAME}
ENV DJANGO_SUPERUSER_EMAIL ${DJANGO_SUPERUSER_EMAIL}
ENV DJANGO_SUPERUSER_PASSWORD ${DJANGO_SUPERUSER_PASSWORD}

RUN apt-get update && apt-get install -y pkg-config
# Install system dependencies
RUN apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies

# Copy the app folder into the container
COPY ../src/core /app
COPY ../src/requirements.txt /app
COPY ../prod/base/entrypoint.sh /tmp/entrypoint.sh

RUN mkdir /app/static

RUN chmod +x /tmp/entrypoint.sh

RUN pip install -r /app/requirements.txt --no-cache-dir


ENTRYPOINT ["/tmp/entrypoint.sh"]

# Define the command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "common.wsgi","--workers", "3", "--timeout", "120", "--log-level", "info", "--access-logfile", "/logs/access.log", "--error-logfile", "/logs/error.log"]