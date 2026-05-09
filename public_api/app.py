from flask import Flask, request
from random import choice, randint
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    phrase = choice([
        'Welcome to the page!',
        'You are looking good today!',
        'The weather is great!'
    ])

    return {
        'phrase': phrase,
        'date': datetime.now()
    }

@app.route('/api/random')
def random():
    input = request.args.get('number', type=int)
    text_input = request.args.get('text', type=str, default='Hello')

    if isinstance(input, int):
        return {
            'input': input,
            'random': randint(0, input),
            'text': text_input,
            'date': datetime.now()
        }
    else:
        return {
            'error': 'Invalid input. Please provide a number.'
        }

if __name__ == "__main__":
    app.run(debug=True)