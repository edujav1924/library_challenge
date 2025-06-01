FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

COPY src/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN rm -rf /tmp/requirements.txt

#ENTRYPOINT [ "/entrypoint.sh" ]
