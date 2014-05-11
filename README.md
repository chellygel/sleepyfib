SleepyFib
=========

SleepyFib is a REST API for producing numbers of the fibonacci sequence and returning them in JSON format.

##Requirements

SleepyFib requires the usage of the following python packages:

<pre>
Flask==0.10.1
Jinja2==2.7.2
MarkupSafe==0.23
Werkzeug==0.9.4
argparse==1.2.1
distribute==0.7.3
itsdangerous==0.24
py==1.4.20
pytest==2.5.2
requests==2.2.1
wsgiref==0.1.2
</pre>

This list is available in the [requirements.txt](https://github.com/chelseawinfree/sleepyfib/blob/master/requirements.txt) file for easy installation.

For more information on Flask you can go to their [main page](http://flask.pocoo.org/).

##Setting Up

Setting up SleepyFib requires some knowledge of git & linux based systems.

This set up assumes you:
* Want to run this locally on your machine
* Are familiar with using virtualenv
* Are familiar with basic linux commands

This set up is a casual step by step guide to getting SleepyFib up and running. I will post links to better, more in-depth guides in each section for reference.

###Pre-Install

1. Create a new virtual environment for sleepyfib
<pre>$virtualenv sleepyfib</pre>
2. Source the virtual environment so that it is running
<pre>source sleepyfib/bin/activate</pre>

For more information visit the [virtualenv docs](http://virtualenv.readthedocs.org/en/latest/). Or checkout the [python guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

###Installation steps
1. Clone the repository to desired location
<pre>git clone https://github.com/chelseawinfree/sleepyfib.git</pre>

2. Navigate to directory where you cloned SleepyFib

3. Install necessary packages
<pre>pip install -r requirements.txt</pre>

4. Set file permissions to all and execute
<pre>chmod a+x app.py

## Starting up the App

To start up the app, all we have to do now is launch it! Using the command ./app.py you should see the following:

<pre>
$ ./app.py
* Running on http://127.0.0.1:5000/
* Restarting with reloader
</pre>

Congratulations! It should be running. Navigate to [http://localhost:5000](http://localhost:5000) to make sure it is running successfully. You should see welcome message in browser.

<pre>
Welcome to the SleepyFib API!...
</pre>

## Calling the API
In these examples I will be using curl.

Here are a list of the calls available to you:

1. [GET] To view the home index page with general information about SleepyFib 
<pre>
$ curl "http://localhost:5000/index"
Welcome to the SleepyFib API!
</pre>

2. [GET] To retrieve a Fibonacci Sequence for a number that is submitted
<pre>
$ curl "http://localhost:5000/sleepyfib/api/fib/5"
{
  "The Fibonacci Sequence is": [
    0, 
    1, 
    1, 
    2, 
    3
  ]
}
</pre>

3. [GET] To retreive the limitations of the API
<pre>
$ curl "http://localhost:5000/sleepyfib/api/limits"
{
  "Limiations": [
    {
      "description": "User should not call a number larger than 9000", 
      "id": 1, 
      "type": "Maximum Call Length"
    }, 
    {
      "description": "User should only use positive integers only", 
      "id": 2, 
      "type": "Positive Integers Only"
    }
  ]
}
</pre>



