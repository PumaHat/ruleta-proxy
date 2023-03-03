from wsgiref.simple_server import make_server
import time

PUERTO = 8000

def application(environ, start_response):
    peticion = environ['PATH_INFO']
    if peticion.startswith('/ruleta'):
        try:
            request_body = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH'])).decode('utf-8')
            d = {}
            for i in request_body.split("&"):
                j = i.partition("=")
                d[j[0]] = j[2]
            v = d.get('letra', "2")
        except:
            tipo = 'application/xhtml+xml'
            codigo = "200 OK"
            salida = open("ruleta.html", encoding="utf8").read()
        else:
            codigo = "200 OK"
            tipo = 'application/json'
            print(v)
            if v == "G":
                salida = '{"premio": "$10"}'
            elif v == "X":
                salida = '{"premio": "$10000"}'
                print("Ganador: "+d.get("alumno", "Anonimo")+"; Tiempo: "+time.asctime());
            else:
                salida = '{"premio": "$0"}'
                print("NoGanador: "+d.get("alumno", "Anonimo")+"; Tiempo: "+time.asctime());
    else:
        tipo = 'text/plain'
        codigo = "404 Not Found"
        salida = "Especifica una página"

    headers = [('Content-Type', tipo+'; charset=utf-8')]
    start_response(codigo, headers)
    return [salida.encode('utf-8')]

server = make_server('', PUERTO, application)
server.serve_forever()
