import json
from wsgiref.simple_server import make_server

def application(environ, start_response):
    headers = [ ('Content-type', 'application/json') ]

    start_response('200 OK', headers)

    response = {
        'mensaje' : 'Hola Mundo desde el servidor!'
    }

    return [ bytes(json.dumps(response), 'utf-8') ]

servidor = make_server('localhost', 8000, application)
servidor.handle_request()