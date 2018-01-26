""" Goal: Learn to build small web apps and REST APIs.

Balancer/manager:   Apache, Ngninx, HAProxy

Webserver:          gunicorn, uwsgi, cherrypy

Web framework:      bottle, flask, cherrypy ... django, pylons, zope
                    [-- lightweight --]         [-- heavyweight --]

This file:          from bottle import get
                    @get('/quadratic')
                    def quad():
                        return algebra.quadratic(...)

Application:        algebra.py      <== Standalone Python Package

"""

from notes.bottle import run, get, response, request
import time

@get('/')
def welcome():
    if 'text/html' in request.headers.get('Accept', ''):
        # ^-- Content negotiation
        return '<h1>Howdy!</h1>'
    response.content_type = 'text/plain'
    return 'Hello World!'

# http://localhost:5050/now
@get('/now')
def time_microservice():
    response.content_type = 'text/plain'
    return time.ctime()

if __name__ == '__main__':
    run(host='localhost', port=5050, debug=True)
