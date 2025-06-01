FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

COPY src/requirements.txt /tmp/requirements.txt
COPY dev_environment/entrypoint.sh /tmp/entrypoint.sh
RUN chmod +x /tmp/entrypoint.sh

RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN rm -rf /tmp/requirements.txt
WORKDIR /app

ENTRYPOINT [ "/tmp/entrypoint.sh" ]
CMD ["python"]