from mblock import event
import random
import math
import time

Cuadrado_de_la_distancia_de_libelula_final_eje_x = 0
Cuadrado_de_la_distancia_de_libelula_final_eje_y = 0

@event.greenflag
def on_greenflag():
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
    sprite.set_variable('Distancia vectorial', 100)
    sprite.set_variable('Dirección final de libelula', 0)
    # not supported yet
    # not supported yet
    # not supported yet


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


    sprite.glide(sprite.get_variable('Destino aleatorio en eje x de libelula'), sprite.get_variable('Tope Vertical'), 4 / sprite.get_variable('Dificultad'))


def Generador_de_libelulas():
    global Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y
    while True:
        time.sleep(0.5)
        sprite.clone('_myself_')



@event.greenflag
def on_greenflag1():
    global Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y
    sprite.hide()
    Generador_de_libelulas()







# not supported yet
Movimiento_de_libelulas()
# not supported yet

# Control para evitar sobrecreación
# not supported yet
time.sleep(5)
# not supported yet

# not supported yet
sprite.set_variable('Distancia de libelula-final eje x', ((sprite.get_property('Bala', 'x') - sprite.x)))
Cuadrado_de_la_distancia_de_libelula_final_eje_x = sprite.get_variable('Distancia de libelula-final eje x') * sprite.get_variable('Distancia de libelula-final eje x')
sprite.set_variable('Distancia de libelula-final eje y', ((sprite.get_property('Bala', 'y') - sprite.y)))
Cuadrado_de_la_distancia_de_libelula_final_eje_y = sprite.get_variable('Distancia de libelula-final eje y') * sprite.get_variable('Distancia de libelula-final eje y')
# Raiz de los cuadrados de la suma de coordenadas
# Distancia del modulo del vector de distancia
sprite.set_variable('Distancia vectorial', math.sqrt((Cuadrado_de_la_distancia_de_libelula_final_eje_x + Cuadrado_de_la_distancia_de_libelula_final_eje_y)))
while True:
    if sprite.get_variable('Bandera de disparo') == 1:
        if sprite.touching('Bala') or sprite.get_variable('Distancia vectorial') < 1:
            v = sprite.get_variable('Puntos')
            sprite.set_variable('Puntos', v + 10)
            # not supported yet
