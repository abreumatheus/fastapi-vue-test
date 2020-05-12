FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /backend/
COPY ./backend /app

ENV PYTHONPATH=/app

ENV AWS_ACCESS_KEY_ID=***REMOVED***
ENV AWS_SECRET_ACCESS_KEY=***REMOVED***

