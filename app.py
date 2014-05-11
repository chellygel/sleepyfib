#!/usr/bin/env python
from flask import Flask, jsonify
from fibonacci import SleepyFib

app = Flask(__name__)

limitations = [
    {
        'id' : 1,
        'type' : "Maximum Call Length",
        'description' : "User should not call a number larger than 9000"
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

@app.route('/sleepyfib/api/limits', methods = ['GET'])
def get_limits():
    # Explain details of limitations
    return jsonify( {'Limiations' : limitations} )

@app.route('/sleepyfib/api/fib/<n>', methods = ['GET'])
def get_fib(n):
    try:
        n = int(n)
    except ValueError:
        return jsonify({"Error!":"Only positive integers, please"})

    response = SleepyFib().validate_fib(n)
    if response is True:
        number = SleepyFib().fib(int(n))
        return jsonify( { 'The Fibonacci Sequence is': number} )
    else:
        return jsonify({'Error!' : response})

if __name__ == '__main__':
    app.run(debug = True)