from flask import Flask, request, jsonify
import openai

# Replace with your OpenAI API key
openai_api_key = 'YOUR-API-KEY-HERE'

# Configure OpenAI
openai.api_key = openai_api_key

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_gpt4():
    question = request.json.get('question', '')

    if len(question) > 32000:
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
