#!/usr/bin/env python3
#https://www.circuitbasics.com/web-server-and-raspberry-pi/
from bottle import route, run

@route('/hello')
def hello():
    return "Hello there..."

run(host='192.168.8.39', port=1234, debug=True, reloader=True)