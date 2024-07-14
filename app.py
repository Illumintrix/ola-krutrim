from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = 'https://cloud.olakrutrim.com/v1/chat/completions'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer <Your API Key>'
}

def get_response_from_api(question):
    data = {
        "model": "Mistral-7B-Instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(API_URL, headers=HEADERS, json=data)
    return response.json()['choices'][0]['message']['content']

@app.route('/')
def index():
    return render_template('index.html', messages=[])

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    answer = get_response_from_api(question)
    messages = [
        {'content': f'You: {question}', 'class': 'user-message'},
        {'content': f'ChatGPT: {answer}', 'class': 'assistant-message'}
    ]
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
