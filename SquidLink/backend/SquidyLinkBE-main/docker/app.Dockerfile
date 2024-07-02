# syntax=docker/dockerfile:1

FROM alpine:latest

# Copy configs
COPY docker/Caddyfile /app/Caddyfile
RUN echo "$TZ" > /etc/timezone

# Install Caddy and Python
RUN apk add --no-cache \
    #caddy \
    python3 py3-pip \
    gcc python3-dev musl-dev


# Copy source dirs
COPY squidlink /app/squidlink
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN python3 -m venv .venv \
    && /app/.venv/bin/pip3 install --no-cache --upgrade pip setuptools \
    && /app/.venv/bin/pip3 install -r requirements.txt

# Run start script
EXPOSE 8000
ENTRYPOINT [".venv/bin/uvicorn", "squidlink.main:app", "--reload", "--port", "8000", "--host", "0.0.0.0"]
