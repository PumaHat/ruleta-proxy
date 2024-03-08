FROM python:alpine

WORKDIR /srv/phct

COPY src/controlador.py ./
COPY src/ruleta.html ./

EXPOSE 8000/tcp

CMD [ "python", "./controlador.py" ]
