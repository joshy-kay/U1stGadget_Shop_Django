Deployment guide — quick steps to host remotely

Recommended (simple, free-ish): PythonAnywhere

1) Push your project to GitHub:
   - git init
   - git add .
   - git commit -m "Initial"
   - create a GitHub repo and push

2) Create a PythonAnywhere account (free tier)
   - In Web tab, choose "Manual configuration", select Python 3.11
   - Point WSGI file to `u1stgadget.wsgi` and set source path to your project
   - Configure `Virtualenv` to point to a virtualenv and install:
     pip install -r requirements.txt
   - Set `Static files` mapping: URL `/static/` -> path `/home/youruser/yourproject/staticfiles`
   - Run `python manage.py collectstatic` on the server
   - Ensure `ALLOWED_HOSTS` in `u1stgadget/settings.py` includes your PythonAnywhere domain

Alternative: Render / Railway (may require paid plans)
- Add `gunicorn` and `Procfile` (already included)
- Set environment variable `DJANGO_SETTINGS_MODULE=u1stgadget.settings`
- Add build command `pip install -r requirements.txt` and start command `gunicorn u1stgadget.wsgi`

Notes:
- For small presentation use SQLite is fine. For production use a proper DB (Postgres).
- Set `DEBUG = False` and `ALLOWED_HOSTS` appropriately for public hosting.
- Change the `admin` password after deploying.

If you'd like, I can:
- Prepare a `.gitignore` and commit-ready files.
- Help push to a GitHub repo (you'll need to provide credentials or push locally).
- Walk you through the PythonAnywhere web UI step-by-step while you do the signup.

Which option do you want me to prepare next?