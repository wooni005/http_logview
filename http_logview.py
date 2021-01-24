#!/usr/bin/python3
from time import sleep
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_page():
    return "Met http_logview is het mogelijk om de logfiles in de hdd/log directory te bekijken door de logfile achter de / in te vullen."


@app.route('/<logfilename>')
def file_display(logfilename):
    def generate():
        with open('/home/pi/log/%s' % logfilename) as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype='text/plain')


app.run(threaded=True, host='0.0.0.0')
