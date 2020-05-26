FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /fastapi/
COPY ./fastapi /app

ENV PYTHONPATH=/app

ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=

RUN pip install -r /app/requirements.txt
