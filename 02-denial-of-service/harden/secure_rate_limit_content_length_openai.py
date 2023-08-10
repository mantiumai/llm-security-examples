from flask import Flask, request, jsonify
from flask_limiter import Limiter
import openai

# Replace with your OpenAI API key
openai_api_key = 'YOUR-API-KEY-HERE'

# Configure OpenAI
openai.api_key = openai_api_key

app = Flask(__name__)

# Set up rate limiting
limiter = Limiter(app, key_func=lambda: request.remote_addr, default_limits=["5 per minute"])

# Content-Length limit in bytes (32,000 tokens should generally fit within this, though exact size may vary)
MAX_CONTENT_LENGTH = 32000 * 4

@app.before_request
def content_length_limit():
    if request.content_length and request.content_length > MAX_CONTENT_LENGTH:
        return jsonify(error="Content-Length exceeds maximum size"), 400

@app.route('/ask', methods=['POST'])
@limiter.limit("2 per second") # Limit to 2 requests per second per IP
def ask_gpt4():
    question = request.json.get('question', '')

    # Estimate the number of tokens in the question; this is a very rough estimate
    token_count = len(question.split())

    if token_count > 32000:
        return jsonify(error="Question exceeds maximum token size"), 400

    try:
        response = openai.Completion.create(
          engine="gpt-4-32k", # (gpt-4, gpt-3.5-turbo, etc)
          prompt=question,
          max_tokens=32000
        )
        return jsonify(answer=response.choices[0].text)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
