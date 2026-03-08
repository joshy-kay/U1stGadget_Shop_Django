#!/usr/bin/env bash
# Build script for Render deployment.
# Installs Python dependencies, collects static files and runs migrations.
# Render will run this during the build/deploy phase if configured.

set -e
echo "Installing requirements..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Build complete."
#!/usr/bin/env bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
