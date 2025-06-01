# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPERUSER_USERNAME ${DJANGO_SUPERUSER_USERNAME}
ENV DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}

RUN apt-get update && apt-get install -y pkg-config
# Install system dependencies
RUN apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
# Set environment variables for MySQL client library
#ENV MYSQLCLIENT_CFLAGS "-I/usr/include/mysql"
#ENV MYSQLCLIENT_LDFLAGS "-L/usr/lib/x86_64-linux-gnu -lmysqlclient"
# Set the working directory in the container
WORKDIR /app

# Install dependencies

# Copy the app folder into the container
COPY ../src/book_manager /app
COPY ../src/requirements.txt /app
COPY ../prod/base/entrypoint.sh /tmp/entrypoint.sh

RUN mkdir /app/static

RUN chmod +x /tmp/entrypoint.sh


# Define the command to run your application
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi:application"]
# Install dependencies
RUN pip install -r  requirements.txt


ENTRYPOINT ["/tmp/entrypoint.sh"]

# Define the command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "common.wsgi"]