from wsgiref.simple_server import make_server
import time

cont = {}
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
                cont[d.get("alumno", "Anonimo")] = 0
            elif v == "X":
                if d.get("alumno", "Anonimo") in cont:
                    cont[d.get("alumno", "Anonimo")] += 1
                else:
                    cont[d.get("alumno", "Anonimo")] = 1
                if cont[d.get("alumno", "Anonimo")] == 3:
                    salida = '{"premio": "$10000"}'
                    print("Ganador: "+d.get("alumno", "Anonimo")+"; Tiempo: "+time.asctime());
                    cont[d.get("alumno", "Anonimo")] = 0
                else:
                    salida = '{"premio": "$0"}'
                    print("NoGanador: "+d.get("alumno", "Anonimo")+"; Tiempo: "+time.asctime());
            else:
                salida = '{"premio": "$0"}'
                print("NoGanador: "+d.get("alumno", "Anonimo")+"; Tiempo: "+time.asctime());
                cont[d.get("alumno", "Anonimo")] = 0
    else:
        tipo = 'text/plain'
        codigo = "404 Not Found"
        salida = "Especifica una página"

    headers = [('Content-Type', tipo+'; charset=utf-8')]
    start_response(codigo, headers)
    return [salida.encode('utf-8')]

server = make_server('', PUERTO, application)
server.serve_forever()
