''' Goal: Learn to build small web apps and REST APIs.

Balancer/Manager:    Nginx, HAProxy

Webserver:           gunicorn, uwsgi

Web framework:       bottle, flask, cherrypy, ...  django, pylons, zope
                     [-- lightweight or micro --]  [-- heavyweight ---]

The file:            from bottle import get
                     @get('/quadratic')
                     def quad():
                         return somemod.quadratic()

Application:         algebra.py            <== Standalone Python Package

'''

from notes.bottle import run, get, response, request, template, static_file
import time
import subprocess
import algebra
import monkey_patch
import os


@get('/')
def welcome():
    if 'text/html' in request.headers.get('Accept', ''):
        # ^-- Content negotiation
        return '<h1>Howdy!</h1>'
    response.content_type = 'text/plain'
    return 'Hello'

# http://localhost:8080/now
@get('/now')
def time_microservice():
    response.set_header('Cache-Control', 'max-age=1')
    response.content_type = 'text/plain'
    return time.ctime()

# http://localhost:8080/interfaces
@get('/interfaces')
def netstat_service():
    response.content_type = 'text/plain'
    return subprocess.check_output(['netstat', '-i'])

# http://localhost:8080/upper/cisco
@get('/upper/<word>')
def uppercasing_service(word):
    response.content_type = 'text/plain'
    return word.upper()

# http://localhost:8080/area/circle?radius=10.0
@get('/area/circle')
def circle_area_microservice():
    try:
        radius = float(request.query.get('radius', '0.0'))
    except ValueError:
        radius = 0.0
    area = algebra.area(radius)
    return dict(service=request.path, radius=radius, area=area)


## Quadratic equation service  #################################

# http://localhost:8080/quadratic?a=25&b=80&c=4  ==>  JSON
@get('/quadratic')
def quadratic_solver():
    a = float(request.query.get('a', '0'))
    b = float(request.query.get('b', '0'))
    c = float(request.query.get('c', '0'))

    try:
        x1, x2 = algebra.quadratic(a, b, c)
    except ZeroDivisionError:
        x1 = x2 = 0

    if 'text/html' in request.headers.get('Accept', ''):
        return template('notes/quadratic.tpl',
                        a=a, b=b, c=c, x1=x1, x2=x2)

    x1 = complex(x1)
    x2 = complex(x2)

    return dict(service = request.path,
                a=a, b=b, c=c,
                x1 = dict(real=x1.real, imag=x1.imag),
                x2 = dict(real=x2.real, imag=x2.imag))


## File Server #################################################

file_template = '''
<h1> List of files in the <em> notes </em> directory </h1>
<hr>
<ol>
% for filename in files:
    <li> <a href="files/{{filename}}"> {{filename}} </a> </li>
% end
</ol>
'''

@get('/files')
def show_files():
    files = os.listdir('notes')
    return template(file_template, files=files)

@get('/files/<filename>')
def serve_file(filename):
    return static_file(filename, root='./notes')


if __name__ == '__main__':
    run(host='localhost', port=5050, debug=True)
    # run(host='localhost', port=5055, server='gunicorn', workers=4)
