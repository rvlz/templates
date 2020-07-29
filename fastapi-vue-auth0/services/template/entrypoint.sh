#!/bin/sh

while ! nc -z template-db 5432; do
  sleep 0.1
done

uvicorn wsgi:app --reload --workers 1 --host 0.0.0.0 --port 8000
