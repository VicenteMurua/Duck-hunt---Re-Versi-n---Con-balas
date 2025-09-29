from mblock import event
import time
import random
import math

Distancia_de_buho_final_eje_x = 0
Cuadrado_de_la_distancia_de_buho_final_eje_x = 0
Distancia_de_buho_final_eje_y = 0
Cuadrado_de_la_distancia_de_buho_final_eje_y = 0
Distancia_vectorial_de_buho = 0
Distancia_de_tucan_final_eje_x = 0
Distancia_de_tucan_final_eje_y = 0
Cuadrado_de_la_distancia_de_tucan_final_eje_x = 0
Cuadrado_de_la_distancia_de_tucan_final_eje_y = 0
Distancia_vectorial_tucan = 0

@event.greenflag
def on_greenflag():
    global Distancia_de_buho_final_eje_x, Cuadrado_de_la_distancia_de_buho_final_eje_x, Distancia_de_buho_final_eje_y, Cuadrado_de_la_distancia_de_buho_final_eje_y, Distancia_vectorial_de_buho, Distancia_de_tucan_final_eje_x, Distancia_de_tucan_final_eje_y, Cuadrado_de_la_distancia_de_tucan_final_eje_x, Cuadrado_de_la_distancia_de_tucan_final_eje_y, Distancia_vectorial_tucan
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.x = 0
    sprite.y = -180
    sprite.hide()


@event.received('Inicio')
def on_received():
    global Distancia_de_buho_final_eje_x, Cuadrado_de_la_distancia_de_buho_final_eje_x, Distancia_de_buho_final_eje_y, Cuadrado_de_la_distancia_de_buho_final_eje_y, Distancia_vectorial_de_buho, Distancia_de_tucan_final_eje_x, Distancia_de_tucan_final_eje_y, Cuadrado_de_la_distancia_de_tucan_final_eje_x, Cuadrado_de_la_distancia_de_tucan_final_eje_y, Distancia_vectorial_tucan
    sprite.x = 0
    sprite.y = -180
    sprite.hide()
    # not supported yet
    sprite.set_variable('Bajas de tucanes', 0)
    # not supported yet
    sprite.set_variable('Creacion de tucanes', 0)


@event.received('Juego')
def on_received1():
    global Distancia_de_buho_final_eje_x, Cuadrado_de_la_distancia_de_buho_final_eje_x, Distancia_de_buho_final_eje_y, Cuadrado_de_la_distancia_de_buho_final_eje_y, Distancia_vectorial_de_buho, Distancia_de_tucan_final_eje_x, Distancia_de_tucan_final_eje_y, Cuadrado_de_la_distancia_de_tucan_final_eje_x, Cuadrado_de_la_distancia_de_tucan_final_eje_y, Distancia_vectorial_tucan
    sprite.hide()
    sprite.x = 0
    sprite.y = -180
    # not supported yet
    sprite.set_variable('Bajas de tucanes', 0)
    # not supported yet
    sprite.set_variable('Creacion de tucanes', 0)
    while True:
        time.sleep(float(random.uniform((3 - 0.3 * sprite.get_variable('Dificultad')), (10 - sprite.get_variable('Dificultad')))))
        sprite.clone('_myself_')
        v = sprite.get_variable('Creacion de tucanes')
        sprite.set_variable('Creacion de tucanes', v + 1)
        if not str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
            time.sleep(1)
            sprite.stop_other()
            sprite.stop_this()




@event.received('Fin')
def on_received2():
    global Distancia_de_buho_final_eje_x, Cuadrado_de_la_distancia_de_buho_final_eje_x, Distancia_de_buho_final_eje_y, Cuadrado_de_la_distancia_de_buho_final_eje_y, Distancia_vectorial_de_buho, Distancia_de_tucan_final_eje_x, Distancia_de_tucan_final_eje_y, Cuadrado_de_la_distancia_de_tucan_final_eje_x, Cuadrado_de_la_distancia_de_tucan_final_eje_y, Distancia_vectorial_tucan
    sprite.hide()
    sprite.x = (sprite.get_variable('Posicion resumen eje x') + -27)
    sprite.y = (sprite.get_variable('Posicion resumen eje y') + -20)
    sprite.size = 40
    if (100 * ((sprite.get_variable('Creacion de tucanes') - sprite.get_variable('Bajas de tucanes')))) / sprite.get_variable('Creacion de tucanes') > 70:
        sprite.set_costume('Toucan - Normal')

    else:
        sprite.set_costume('Toucan - Llorando')

    sprite.show()
    sprite.z_index = 256
    time.sleep(0.05)
    sprite.say(str(str('Han pasado ') + str((sprite.get_variable('Creacion de tucanes') - sprite.get_variable('Bajas de tucanes')))) + str(str(' de ') + str(sprite.get_variable('Creacion de tucanes'))))







# not supported yet
while True:
    if sprite.x > -180:
        sprite.left(15)
        for count in range(2):
            sprite.y = sprite.y + 25
            sprite.set_costume('Toucan - Elevación')
            time.sleep(0.1)
            sprite.set_costume('Toucan - Medio')
            time.sleep(0.1)
            sprite.set_costume('Toucan - Caida')

        sprite.right(15)
        sprite.right(15)
        for count2 in range(15):
            sprite.y = sprite.y + -3

        sprite.left(15)
        time.sleep(0.1)



# not supported yet
sprite.z_index = 256
sprite.set_costume('Toucan - Caida')
sprite.z_index = sprite.z_index-1
sprite.play('Squawk')
sprite.show()
sprite.size = 10 * sprite.get_variable('Dificultad')
sprite.x = -240
sprite.y = random.uniform((sprite.get_variable('Linea de horizonte') - 40), (sprite.get_variable('Tope Vertical') - 100))
while True:
    if not str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
        # not supported yet

    else:
        if -180 > sprite.x:
            sprite.size = sprite.size + 3
            sprite.x = sprite.x + 5

        else:
            sprite.x = sprite.x + 3
            if sprite.touching('edge') and sprite.x > sprite.get_variable('Tope horizontal'):
                v = sprite.get_variable('Puntos')
                sprite.set_variable('Puntos', v + 20)
                sprite.play('Coin')
                # not supported yet





# not supported yet
Distancia_de_tucan_final_eje_x = ((sprite.get_property('Bala', 'x') - sprite.x))
Cuadrado_de_la_distancia_de_tucan_final_eje_x = Distancia_de_tucan_final_eje_x * Distancia_de_tucan_final_eje_x
Distancia_de_tucan_final_eje_y = ((sprite.get_property('Bala', 'y') - sprite.y))
Cuadrado_de_la_distancia_de_tucan_final_eje_y = Distancia_de_tucan_final_eje_y * Distancia_de_tucan_final_eje_y
Distancia_vectorial_tucan = math.sqrt((Cuadrado_de_la_distancia_de_tucan_final_eje_y + Cuadrado_de_la_distancia_de_tucan_final_eje_x))
while True:
    if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
        # not supported yet

    if sprite.get_variable('Bandera de disparo') == 1:
        if sprite.touching('Bala') or Distancia_vectorial_tucan < 1:
            v = sprite.get_variable('Puntos')
            sprite.set_variable('Puntos', v + -25)
            v = sprite.get_variable('Vidas totales')
            sprite.set_variable('Vidas totales', v + -1)
            v = sprite.get_variable('Bajas de tucanes')
            sprite.set_variable('Bajas de tucanes', v + 1)
            sprite.play('Glass Breaking')
            sprite.clone('Sprite - Calavera')
            # not supported yet
