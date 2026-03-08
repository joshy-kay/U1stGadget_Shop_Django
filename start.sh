#!/usr/bin/env bash
# Start script for Render. Runs Gunicorn using the project's WSGI app.
#
# Render will execute this to start the web service. Make sure the service
# uses this command as the start command in Render settings.

set -e

# Auto-detected Django project name (from manage.py settings): u1stgadget
echo "Starting Gunicorn for u1stgadget.wsgi:application"
exec gunicorn u1stgadget.wsgi:application --bind 0.0.0.0:$PORT --workers 3
gunicorn u1stgadget.wsgi:application
