#+TITLE: Laboratorios para PHCT
Este repositorio tiene algunos ejercicios para practicar el temario de PumaHat. Por ahora, solo hay uno.

** Ejercicios
*** Ruleta
- [[http://localhost/ruleta][Jugar]]
Tienes una ruleta con varias letras, una de ellas -la X- está premiada. Cada vez que gira la ruleta, la página envía una petición al servidor con la letra y tu nombre, y te devuelve un premio. Has de engañar al servidor haciéndloe creer que has obtenido X en la ruleta tres veces seguidas. En la consola que se abre al ejecutar el programa, puedes ver si lo has conseguido.

** Requisitos
- **Python3** :: Bajo Windows, asegúrate de tener instalado Python 3, y que esté en el PATH. Si abres una terminal, ejecutas el comando `python`, y te devuelve una consola, está listo. De lo contrario, [[https://www.python.org/downloads/windows/][descárgalo]]. Bajo Linux, seguramente ya está instalado.

** Ejecución
En Windows, desde la interfaz gráfica, ejecuta el archivo `iniciar.bat`; o abre una consola en el directorio y ejecuta `python controlador.py`.

En Linux, abre una consola y ejecuta `python3 controlador.py` o `python controlador.py`.
