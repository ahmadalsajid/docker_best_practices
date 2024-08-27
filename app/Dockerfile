FROM python:3.12-alpine3.20
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update && \
    apk add curl && \
    rm -rf /var/cache/apk/* && \
    python -m pip install --upgrade pip

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
EXPOSE 8000

HEALTHCHECK  --start-period=30s \
  CMD curl http://localhost:8000/healthcheck/ || exit 1
CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2" ]