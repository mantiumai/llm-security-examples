from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import openai
import time

openai_api_key = 'YOUR-API-KEY-HERE'
openai.api_key = openai_api_key

app = Flask(__name__)

# Basic in-memory store to track request times by IP
request_times = {}

# Flask-Limiter setup
limiter = Limiter(app, key_func=get_remote_address)

def adaptive_rate_limit():
    remote_addr = get_remote_address()
    now = time.time()

    # Track request times in a list
    if remote_addr not in request_times:
        request_times[remote_addr] = []
    request_times[remote_addr].append(now)

    # Remove old request times
    request_times[remote_addr] = [t for t in request_times[remote_addr] if now - t < 60]

    # Calculate requests per minute
    rpm = len(request_times[remote_addr])

    # Set adaptive limit
    if rpm > 30:
        return "1 per minute"
    elif rpm > 20:
        return "5 per minute"
    else:
        return "10 per minute"

@app.route('/ask', methods=['POST'])
@limiter.request_filter(adaptive_rate_limit)
def ask_gpt4():
    # ... same as before ...

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
