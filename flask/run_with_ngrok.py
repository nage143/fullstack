from pyngrok import ngrok
from app import app

if __name__ == '__main__':
    try:
        tunnel = ngrok.connect(5000)
        print('ngrok tunnel:', tunnel.public_url)
    except Exception as e:
        print('ngrok error:', e)
    # Run Flask app (blocking)
    app.run(port=5000)
