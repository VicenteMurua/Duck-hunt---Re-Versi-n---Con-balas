import random
import math
import time
from mblock import event

Cuadrado_de_la_distancia_de_libelula_final_eje_x = 0
Cuadrado_de_la_distancia_de_libelula_final_eje_y = 0

def Movimiento_de_libelulas():
    global Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y
    sprite.set_variable('Destino aleatorio en eje x de libelula', random.uniform(-1 * sprite.get_variable('Tope horizontal'), sprite.get_variable('Tope horizontal')))
    sprite.x = sprite.get_variable('Destino aleatorio en eje x de libelula')
    sprite.y = sprite.get_variable('Linea de horizonte')
    sprite.show()
    sprite.set_variable('Destino aleatorio en eje x de libelula', random.uniform(-1 * sprite.get_variable('Tope horizontal'), sprite.get_variable('Tope horizontal')))
    sprite.set_variable('Distancia de libelula-final eje x', ((sprite.get_variable('Destino aleatorio en eje x de libelula') - sprite.x)))
    sprite.set_variable('Distancia de libelula-final eje y', ((sprite.get_variable('Tope horizontal') - sprite.y)))
    sprite.set_variable('Dirección final de libelula', -1 * ((math.atan(sprite.get_variable('Distancia de libelula-final eje y') / sprite.get_variable('Distancia de libelula-final eje x')) / math.pi * 180 + 0)))
    sprite.direction = sprite.get_variable('Dirección final de libelula')
    if sprite.get_variable('Distancia de libelula-final eje x') == 0:
        sprite.direction = 0

    else:
        if sprite.get_variable('Dirección final de libelula') < 0:
            sprite.direction = (180 + sprite.get_variable('Dirección final de libelula'))

        else:
            sprite.direction = sprite.get_variable('Dirección final de libelula')


    sprite.glide(sprite.get_variable('Destino aleatorio en eje x de libelula'), sprite.get_variable('Tope Vertical'), 6 / math.sqrt(sprite.get_variable('Dificultad')))


def Generador_de_libelulas():
    global Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y
    while True:
        time.sleep(0.5)
        sprite.clone('_myself_')
        v = sprite.get_variable('Creacion de libelulas')
        sprite.set_variable('Creacion de libelulas', v + 1)
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()




@event.received('Juego')
def on_received():
    global Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y
    sprite.x = 0
    sprite.y = -180
    sprite.hide()
    # not supported yet
    sprite.set_variable('Bajas de libelulas', 0)
    # not supported yet
    sprite.set_variable('Creacion de libelulas', 0)
    Generador_de_libelulas()


@event.received('Juego')
def on_received1():
    global Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y
    sprite.set_variable('Distancia de libelula-final eje x', 0)
    sprite.set_variable('Distancia de libelula-final eje y', 0)
    Cuadrado_de_la_distancia_de_libelula_final_eje_x = 0
    Cuadrado_de_la_distancia_de_libelula_final_eje_y = 0
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('Destino aleatorio en eje x de libelula', 0)
    sprite.set_variable('Distancia vectorial de libelula', 100)
    sprite.set_variable('Dirección final de libelula', 0)
    # not supported yet
    # not supported yet
    # not supported yet


@event.greenflag
def on_greenflag():
    global Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y
    sprite.set_costume('Libelula - Normal')
    sprite.x = 0
    sprite.y = -180
    sprite.hide()
    # not supported yet
    sprite.set_variable('Bajas de libelulas', 0)
    # not supported yet
    sprite.set_variable('Creacion de libelulas', 0)
    # not supported yet


@event.received('Fin')
def on_received2():
    global Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y
    sprite.hide()
    sprite.x = (sprite.get_variable('Posicion resumen eje x') + 10)
    sprite.y = (sprite.get_variable('Posicion resumen eje y') + -70)
    sprite.size = 30
    sprite.direction = 165
    sprite.show()
    sprite.set_costume('Libelula - Llorando')
    sprite.z_index = 256
    time.sleep(0.1)
    sprite.say(str(str('Haz abatido ') + str(sprite.get_variable('Bajas de libelulas'))) + str(str(' de ') + str(sprite.get_variable('Creacion de libelulas'))))


@event.received('Inicio')
def on_received3():
    global Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y
    sprite.x = 0
    sprite.y = -180
    sprite.hide()










# not supported yet
sprite.set_variable('Aleatotiedad de libelula', random.randint(1, 25))
Movimiento_de_libelulas()
# not supported yet

# not supported yet
sprite.set_variable('Distancia de libelula-final eje x', ((sprite.get_property('Bala', 'x') - sprite.x)))
Cuadrado_de_la_distancia_de_libelula_final_eje_x = sprite.get_variable('Distancia de libelula-final eje x') * sprite.get_variable('Distancia de libelula-final eje x')
sprite.set_variable('Distancia de libelula-final eje y', ((sprite.get_property('Bala', 'y') - sprite.y)))
Cuadrado_de_la_distancia_de_libelula_final_eje_y = sprite.get_variable('Distancia de libelula-final eje y') * sprite.get_variable('Distancia de libelula-final eje y')
sprite.set_variable('Distancia vectorial de libelula', math.sqrt((Cuadrado_de_la_distancia_de_libelula_final_eje_x + Cuadrado_de_la_distancia_de_libelula_final_eje_y)))
if sprite.get_variable('Aleatotiedad de libelula') == 1:
    while True:
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            # not supported yet

        if sprite.get_variable('Bandera de disparo') == 1:
            if sprite.touching('Bala') or sprite.get_variable('Distancia vectorial de libelula') < 5:
                v = sprite.get_variable('Puntos')
                sprite.set_variable('Puntos', v + 5)
                v = sprite.get_variable('Bajas de libelulas')
                sprite.set_variable('Bajas de libelulas', v + 1)
                v = sprite.get_variable('Vidas totales')
                sprite.set_variable('Vidas totales', v + 1)
                sprite.clone('Sprite - Corazon')
                sprite.play('Low Whoosh')
                # not supported yet




else:
    while True:
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            # not supported yet

        if sprite.get_variable('Bandera de disparo') == 1:
            if sprite.touching('Bala') or sprite.get_variable('Distancia vectorial de libelula') < 5:
                v = sprite.get_variable('Puntos')
                sprite.set_variable('Puntos', v + 5)
                v = sprite.get_variable('Bajas de libelulas')
                sprite.set_variable('Bajas de libelulas', v + 1)
                sprite.play('Low Whoosh')
                # not supported yet





# not supported yet
if sprite.get_variable('Aleatotiedad de libelula') == 1:
    sprite.play('Magic Spell')
    sprite.size = 20
    while True:
        sprite.set_costume('Libelula - Normal2')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Medio2')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Abajo2')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Medio2')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Normal2')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Arriba2')
        time.sleep(0.01)


else:
    sprite.size = 30
    while True:
        sprite.set_costume('Libelula - Normal')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Medio')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Abajo')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Medio')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Normal')
        time.sleep(0.01)
        sprite.set_costume('Libelula - Arriba')
        time.sleep(0.01)



# not supported yet
sprite.play_until_done('Aletear')

# not supported yet
time.sleep(5)
# not supported yet
