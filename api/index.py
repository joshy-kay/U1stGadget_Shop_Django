import os
import sys
from pathlib import Path
from urllib.parse import urlencode

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Configure Django BEFORE any imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'u1stgadget.settings')

# Set required env vars if not present
if not os.environ.get('DJANGO_SECRET_KEY'):
    os.environ['DJANGO_SECRET_KEY'] = 'vercel-temporary-key-change-in-env'

import django
django.setup()

from django.core.wsgi import get_wsgi_application
from io import BytesIO

# Get WSGI application
django_app = get_wsgi_application()

def handler(request):
    """
    Vercel serverless handler for Django WSGI
    """
    try:
        # Parse query string
        query_params = request.get('queryStringParameters') or {}
        query_string = urlencode(query_params) if query_params else ''
        
        # Get request body
        body = request.get('body', '')
        if isinstance(body, str):
            body = body.encode('utf-8')
        
        # Build environ dict for WSGI
        environ = {
            'REQUEST_METHOD': request.get('httpMethod', 'GET'),
            'SCRIPT_NAME': '',
            'PATH_INFO': request.get('path', '/'),
            'QUERY_STRING': query_string,
            'CONTENT_TYPE': request.get('headers', {}).get('content-type', ''),
            'CONTENT_LENGTH': request.get('headers', {}).get('content-length', str(len(body))),
            'SERVER_NAME': request.get('headers', {}).get('host', 'vercel').split(':')[0],
            'SERVER_PORT': '443',
            'SERVER_PROTOCOL': 'HTTP/1.1',
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'https',
            'wsgi.input': BytesIO(body),
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.multiprocess': False,
            'wsgi.run_once': False,
        }
        
        # Add all headers to environ
        headers = request.get('headers', {}) or {}
        for header_name, header_value in headers.items():
            header_key = header_name.upper().replace('-', '_')
            if header_key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
                environ[f'HTTP_{header_key}'] = header_value
        
        # Response handling
        response_status = [None]
        response_headers = []
        
        def start_response(status, headers, exc_info=None):
            response_status[0] = status
            response_headers.extend(headers)
        
        # Call Django WSGI app
        app_iter = django_app(environ, start_response)
        response_body = b''.join(app_iter)
        
        if hasattr(app_iter, 'close'):
            app_iter.close()
        
        # Extract status code
        status_code = int(response_status[0].split(' ')[0]) if response_status[0] else 500
        
        # Build response headers dict
        headers_dict = {}
        for header_name, header_value in response_headers:
            headers_dict[header_name.lower()] = header_value
        
        # Ensure content-type
        if 'content-type' not in headers_dict:
            headers_dict['content-type'] = 'text/html; charset=utf-8'
        
        # Return Vercel response format
        return {
            'statusCode': status_code,
            'headers': headers_dict,
            'body': response_body.decode('utf-8', errors='replace'),
            'isBase64Encoded': False
        }
        
    except Exception as e:
        import traceback
        error_msg = f'Error: {str(e)}\n\n{traceback.format_exc()}'
        print(error_msg, file=sys.stderr)
        return {
            'statusCode': 500,
            'headers': {'content-type': 'text/plain'},
            'body': error_msg,
            'isBase64Encoded': False
        }