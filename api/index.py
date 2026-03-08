import os
import sys
from pathlib import Path

# Setup path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Configure Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'u1stgadget.settings')
os.environ.setdefault('DJANGO_SECRET_KEY', os.environ.get('DJANGO_SECRET_KEY', 'vercel-key-please-set-env-var'))

import django
django.setup()

from django.core.wsgi import get_wsgi_application
from io import BytesIO

app = get_wsgi_application()

def handler(request):
    """
    Vercel Python Handler - Convert HTTP request to WSGI
    """
    try:
        # Extract request components
        method = request.get('httpMethod', 'GET')
        path = request.get('path', '/')
        headers = request.get('headers', {})
        body = request.get('body', '')
        
        # Handle query string
        query_string = ''
        if request.get('rawQueryString'):
            query_string = request['rawQueryString']
        elif request.get('queryStringParameters'):
            from urllib.parse import urlencode
            query_string = urlencode(request['queryStringParameters'])
        
        # Convert body
        if isinstance(body, str):
            body = body.encode('utf-8')
        elif body is None:
            body = b''
        
        # Build WSGI environ
        environ = {
            'REQUEST_METHOD': method,
            'SCRIPT_NAME': '',
            'PATH_INFO': path,
            'QUERY_STRING': query_string,
            'CONTENT_TYPE': headers.get('content-type', ''),
            'CONTENT_LENGTH': str(len(body)),
            'SERVER_NAME': headers.get('host', 'localhost').split(':')[0],
            'SERVER_PORT': '443',
            'SERVER_PROTOCOL': 'HTTP/1.1',
            'wsgi.version': (1, 0),
            'wsgi.url_scheme': 'https',
            'wsgi.input': BytesIO(body),
            'wsgi.errors': sys.stderr,
            'wsgi.multithread': False,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False,
        }
        
        # Add HTTP headers
        for key, value in (headers or {}).items():
            key = key.upper().replace('-', '_')
            if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
                environ[f'HTTP_{key}'] = value
        
        # Capture response
        status_code = [200]
        response_headers = []
        
        def start_response(status, headers, exc_info=None):
            status_code[0] = int(status.split()[0])
            response_headers.extend(headers)
            return lambda s: None
        
        # Call Django app
        response_body = b''
        try:
            result = app(environ, start_response)
            if result:
                for data in result:
                    response_body += data
            if hasattr(result, 'close'):
                result.close()
        except Exception as e:
            status_code[0] = 500
            response_body = f'Django Error: {str(e)}'.encode()
        
        # Format response
        resp_headers = {}
        for name, value in response_headers:
            resp_headers[name.lower()] = value
        
        return {
            'statusCode': status_code[0],
            'headers': resp_headers,
            'body': response_body.decode('utf-8', errors='replace'),
            'isBase64Encoded': False
        }
        
    except Exception as e:
        import traceback
        return {
            'statusCode': 500,
            'headers': {'content-type': 'text/plain'},
            'body': f'Handler Error: {str(e)}\n{traceback.format_exc()}',
            'isBase64Encoded': False
        }