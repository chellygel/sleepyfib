#!/usr/bin/env python
from flask import Flask, jsonify
from fibonacci import SleepyFib

app = Flask(__name__)

limitations = [
    {
        'id' : 1,
        'type' : "Maximum Call Length",
        'description' : "User should not call a number larger than 8000"
    },
    {
        'id' : 2,
        'type' : "Positive Integers Only",
        'description' : "User should only use positive whole numbers"
    }
]

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to the SleepyFib API!"

@app.route('/limits', methods = ['GET'])
def get_limits():
    # Explain details of limitations
    return jsonify( {'Limiations' : limitations} )

@app.route('/sleepyfib/fib/<n>', methods = ['GET'])
def get_fib(n):
    number = SleepyFib().fib(int(n))
    return jsonify( { 'The Fibonacci Sequence is': number} )



if __name__ == '__main__':
    app.run(debug = True)