FROM python:3.10
EXPOSE 9090

WORKDIR /app

COPY /requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY /app/ /app/

ENV WEB_CONCURRENCY=4
ENV GUNICORN_CMD_ARGS="--bind 0.0.0.0:9090 --worker-class uvicorn.workers.UvicornWorker --max-requests 200 --max-requests-jitter 200 --timeout 60"

CMD ["gunicorn", "main:app"]
