SleepyFib
=========

SleepyFib is a REST API for producing numbers of the fibonacci sequence.

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

##Setting Up

Setting up SleepyFib requires some knowledge of git & linux based systems.

This set up assumes you:
* Want to run this locally on your machine
* Are familiar with using virtualenv
* Are familiar with basic linux commands

###Pre-Install

1. virtualenv sleepyfib
2. source sleepyfib/bin/activate

###Installation steps
1. Clone the repository to desired location
--* <pre>git clone https://github.com/chelseawinfree/sleepyfib.git</pre>

2. Navigate to directory where you cloned SleepyFib

3. Install necessary packages
--* <pre>pip install -r requirements.txt</pre>

4. Set file permissions to all and execute
--* <pre>chmod a+x app.py

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