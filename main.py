from flask import Flask, jsonify, render_template
import random

app = Flask(__random_number__)

@app.route('/')
def home():
    return render_template('app.html')


@app.route('/random-number')
def get_random_number():
    random_number = random.randint(1, 100)
    return jsonify({'random_number': random_number})

if __name__ == '__main__':
    app.run(debug=True)