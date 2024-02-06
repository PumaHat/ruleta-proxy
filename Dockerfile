FROM python:alpine

WORKDIR /usr/src/app

COPY controlador.py ./
COPY ruleta.html ./

EXPOSE 8000/tcp

CMD [ "python", "./controlador.py" ]
