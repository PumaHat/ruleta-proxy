# Writeup

Una vez instalado el repositorio, se abre la página en el navegador de burpsuite, ya que usaremos un proxy.

![burpsuite](images/burpsuite.png)
![burpsuite](images/ruleta.png)

Se gira la ruleta y el proxy intercepta la petición. Si se mandan las peticiones tal cual con la letra que sale, en la consola aparece el mensaje de _No Ganador_

![burpsuite](images/t.png)
![burpsuite](images/T_burpsuite.png)
![burpsuite](images/noganador.png)

Lo que tenemos que hacer es cambiar el valor del parámetro, en este caso se cambia la T por la X. Si se le da en forward para enviar la petición con el valor cambiado, podemos observar que sigue diciendo _No Ganador_ debido a que se debe obtener X en la ruleta 3 veces seguidas

![burpsuite](images/TxX.png)
![burpsuite](images/terminal.png)

Y se repite este proceso tres veces en caso de que las tres veces salgan letras diferentes de X. Finalmente obtenemos el premio en la ruleta y en la consola aparece el mensaje _Ganador_

![burpsuite](images/ganador.png)
![burpsuite](images/premio.png)
