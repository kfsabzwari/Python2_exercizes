""" Goal: Learn to build small web apps and REST APIs.

# https://bottlepy.org/

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
import subprocess
import algebra
import monkey_patch

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

@get('/interfaces')
def netstat_service():
    response.content_type = 'text/plain'
    return subprocess.check_output(['netstat', '-i'])

@get('/circle/area')
def circle_area_microservice():
    try:
        radius = float(request.query.get('radius', '0'))
    except ValueError:
        radius = 0
    area = algebra.area(radius)
    return dict(service=request.path, radius=radius, area=area)

if __name__ == '__main__':
    run(host='localhost', port=5050, debug=True)
    # $ python -m pip install gunicorn
    # run(host='localhost', port=5055, server='gunicorn', workers=4)



