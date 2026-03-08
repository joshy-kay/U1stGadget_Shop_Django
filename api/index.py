import os
import sys
import django
from django.conf import settings
from django.core.wsgi import get_wsgi_application

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Configure Django settings
if not settings.configured:
    settings.configure(
        DEBUG=False,
        SECRET_KEY=os.environ.get('DJANGO_SECRET_KEY', 'fallback-key'),
        DJANGO_SETTINGS_MODULE='u1stgadget.settings',
        ALLOWED_HOSTS=['*'],
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'store',
            'admin_dashboard',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        MIDDLEWARE=[
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ],
        ROOT_URLCONF='u1stgadget.urls',
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(os.path.dirname(__file__), '..', 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        }],
        STATIC_URL='/static/',
        STATICFILES_DIRS=[
            os.path.join(os.path.dirname(__file__), '..', 'static'),
        ],
        STATIC_ROOT=os.path.join(os.path.dirname(__file__), '..', 'staticfiles'),
        MEDIA_URL='/media/',
        MEDIA_ROOT=os.path.join(os.path.dirname(__file__), '..', 'media'),
        LOGIN_URL='/admin/login/',
        LOGIN_REDIRECT_URL='/admin/dashboard/',
        LOGOUT_REDIRECT_URL='/admin/login/',
        DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',
    )

django.setup()

# Get WSGI application
app = get_wsgi_application()

def handler(request):
    """
    Vercel serverless function handler for Django
    """
    # Convert Vercel request to WSGI environ
    environ = {
        'REQUEST_METHOD': request.method,
        'SCRIPT_NAME': '',
        'PATH_INFO': request.path,
        'QUERY_STRING': request.query or '',
        'CONTENT_TYPE': request.headers.get('content-type', ''),
        'CONTENT_LENGTH': str(len(request.body or b'')),
        'SERVER_NAME': 'vercel',
        'SERVER_PORT': '443',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': request.body or b'',
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }

    # Add headers
    for key, value in request.headers.items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value

    # Response handling
    status = []
    headers = []
    body_parts = []

    def start_response(status_line, response_headers, exc_info=None):
        status.append(status_line.split()[0])
        headers.extend(response_headers)

    # Call Django WSGI app
    try:
        result = app(environ, start_response)
        body_parts.extend(result)
    except Exception as e:
        # Handle errors gracefully
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        body_parts.append(str(e).encode())

    # Return Vercel response
    return {
        'statusCode': int(status[0]) if status else 500,
        'headers': dict(headers),
        'body': b''.join(body_parts).decode('utf-8', errors='ignore')
    }