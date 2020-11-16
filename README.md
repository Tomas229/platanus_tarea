## Instrucciones de ejecución
El programa se ejecuta con python Tournament.py
Creará un torneo de 8 pokémon al azar los cuales se elegirán entre los primeros 151 y Torterra que se le fue dada una invitación al torneo por parte del organizador.
Los pokémon invitados utilizarán sus tipos y sus estadísticas base para determinar al ganador de una batalla, el ganador será quien lleve la vida del contrincante a cero.

Las batallas se organizarán en brackets como un campeonato típico y se obtendra un ganador. 
Se podrá leer en consola a los participantes del torneo y también cuando una ronda de brackets comienza.
La consola también mostrará cuando un par de pokémon comiencen a luchar y quien va atacando, además de un indicador si el movimiento es super efectivo!

Cuando terminen todas las batallas se anunciará al ganador.
Para tener un poco más de detalles visitar: https://github.com/Tomas229/platanus_tarea

## Sobre las decisiones tomadas
### ¿Por qué Python?
Utilicé Python simplemente porque lo tengo instalado en mi computador. Mis otras opciones eran Ruby, ya que me dijeron que se utliza mucho en Platanus, y Java, ya que tenía pensado usar double dispatch. Terminé utilizando Python, debido a que el tiempo es oro y la universidad consume mucho de este tiempo.

### Double Dispatch
Originalmente quería utilizar double dispatch para tratar de manera distinta a los movimientos que son súper eficaces o no muy eficaces y poder reflejar la diferencia del daño. Sin embargo, me di cuenta que la API podía mostrarme esa información y que estaría actualizada conforme los juegos iban cambiando, por lo que preferí no hacerlo. 

### Testing
Se ve que comencé un archivo para poder testear si todo funciona correctamente, sin embargo no pude terminarlo debido a la falta de tiempo. Se planeaba utilizar semillas para los test que utilizan números aleatorios y testear de mejor manera posible.

## Análisis
### ¿Quién es el mejor Pokémon?
Lamentablemente no hay una respuesta para ello y eso se debe a que en términos de combates pokémon no se cumple transitividad porque la efectividad de tipos no la cumple. Por ejemplo, si un Pokémon tipo planta vence a uno tipo agua, el cual a su vez venció a uno tipo fuego, no implica que el tipo planta vencerá al tipo fuego. A pesar de esto Pokémon que han sido ganadores en muchas iteraciones de torneos han sido Vaporeon y Rhydon.

### El torneo más largo
Un análisis preliminar indica que las batallas más largas se librarían entre dos Chanseys, lo cuales cuentan con mucho hp y defensa especial, además de poco ataque, por lo que una batalla entre dos podría llevar de 125 a 250 rondas de ataques. Si se llega a dar la suerte (o mala suerte) de tener una lista de participantes compuesta por ocho Chanseys se podrá presencia el torneo más largo de todos.
