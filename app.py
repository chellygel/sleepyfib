#!/usr/bin/env python
from flask import Flask, jsonify
from fibonacci import SleepyFib

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Welcome to the SleepyFib API!"


@app.route('/sleepyfib/fib/<num>', methods = ['GET'])
def call_fib(num):
    number = SleepyFib().fib(int(num))
    return jsonify( { 'The fib number is': number})


if __name__ == '__main__':
    app.run(debug = True)