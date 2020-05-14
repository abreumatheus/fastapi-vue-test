#! /usr/bin/env bash

# Run migrations
pip install -r /app/requirements.txt
alembic -c /app/alembic.ini upgrade head
