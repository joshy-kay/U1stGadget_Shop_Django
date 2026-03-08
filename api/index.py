import os
import sys
import django

# Add project to path
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'u1stgadget.settings')
django.setup()

from django.core.wsgi import get_wsgi_application

# Get WSGI app
wsgi_app = get_wsgi_application()

def handler(request):
    """Vercel serverless handler for Django"""
    environ = {
        'REQUEST_METHOD': request.method,
        'SCRIPT_NAME': '',
        'PATH_INFO': request.path,
        'QUERY_STRING': request.query or '',
        'CONTENT_TYPE': request.headers.get('content-type', ''),
        'CONTENT_LENGTH': request.headers.get('content-length', '0'),
        'SERVER_NAME': request.headers.get('host', 'vercel').split(':')[0],
        'SERVER_PORT': '443',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': request.body if hasattr(request, 'body') else b'',
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    
    # Add all headers
    for header, value in request.headers.items():
        header = header.upper().replace('-', '_')
        if header not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            environ[f'HTTP_{header}'] = value
    
    # Response collection
    response_status = [0]
    response_headers = []
    
    def start_response(status, headers, exc_info=None):
        response_status[0] = int(status.split()[0])
        response_headers.extend(headers)
    
    # Call Django
    response_data = b''
    try:
        app_iter = wsgi_app(environ, start_response)
        response_data = b''.join(app_iter)
        if hasattr(app_iter, 'close'):
            app_iter.close()
    except Exception as e:
        response_status[0] = 500
        response_data = f'Error: {str(e)}'.encode()
    
    # Return response
    return {
        'statusCode': response_status[0],
        'headers': dict(response_headers),
        'body': response_data.decode('utf-8', errors='ignore'),
        'isBase64Encoded': False
    }