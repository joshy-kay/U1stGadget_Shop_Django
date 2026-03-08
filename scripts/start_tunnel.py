"""Start a pyngrok tunnel to the local Django dev server (port 8000).

Run: python scripts/start_tunnel.py

This will print the public URL and keep the tunnel open until interrupted.
"""
from pyngrok import ngrok, conf
import time

# Optionally set authtoken via environment or conf if you have one
# conf.get_default().auth_token = "YOUR_NGROK_AUTHTOKEN"

print('Starting ngrok tunnel to http://127.0.0.1:8000 ...')
tunnel = ngrok.connect(8000, bind_tls=True)
print('Public URL:', tunnel.public_url)

try:
    while True:
        time.sleep(3600)
except KeyboardInterrupt:
    print('Shutting down tunnel...')
    ngrok.disconnect(tunnel.public_url)
