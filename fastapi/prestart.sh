#! /usr/bin/env bash

# Install packages
pip install -r /app/requirements.txt

# Run migrations
alembic -c /app/alembic.ini upgrade head