#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z postgres 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

gunicorn -b 0.0.0.0:8080 app:app
#gunicorn -b 0.0.0.0:5000 app:app