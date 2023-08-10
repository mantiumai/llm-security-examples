from flask import Flask, request, jsonify
from flask_limiter import Limiter
import openai
import time
import logging
import smtplib
from email.message import EmailMessage

# Configure OpenAI
openai_api_key = 'YOUR-API-KEY-HERE'
openai.api_key = openai_api_key

app = Flask(__name__)

# Basic logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Flask-Limiter and request tracking setup
limiter = Limiter(app, key_func=lambda: request.remote_addr)
request_times = {}

# Hardcoded API key for authentication (Replace this with a proper authentication system in production)
API_KEY = "your-secret-api-key"

# Email settings for alerting
ALERT_EMAIL = "youremail@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_USERNAME = "username"
SMTP_PASSWORD = "password"

def send_alert(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = ALERT_EMAIL
    msg["To"] = ALERT_EMAIL

    with smtplib.SMTP(SMTP_SERVER) as server:
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)

    logger.info(f"Alert sent: {subject}")

# ... Adaptive rate limiting code here ...

@app.before_request
def require_api_key():
    if request.headers.get("X-API-Key") != API_KEY:
        return jsonify(error="Authentication required"), 401

@app.route('/ask', methods=['POST'])
@limiter.request_filter(adaptive_rate_limit)
def ask_gpt4():
    question = request.json.get('question', '')
    # ... same as before ...

    # Monitor the request for any unusual patterns (this is a very naive example)
    if len(question.split()) > 30000:
        send_alert("Suspicious Request Detected", f"Suspicious request from {request.remote_addr}: {question[:100]}...")

    # ... rest of the code ...

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
