from mblock import event
import time
import random
import math

Destino_aleatorio_en_el_eje_x_de_buho = 0
Velocidad_de_Buho = 0
Cuadrado_de_la_distancia_de_libelula_final_eje_x = 0
Cuadrado_de_la_distancia_de_libelula_final_eje_y = 0
Distancia_de_buho_final_eje_x = 0
Cuadrado_de_la_distancia_de_buho_final_eje_x = 0
Distancia_de_buho_final_eje_y = 0
Cuadrado_de_la_distancia_de_buho_final_eje_y = 0
Distancia_vectorial_de_buho = 0
Direcci_C3_B3n_de_burla = 0

@event.greenflag
def on_greenflag():
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho, Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y, Distancia_de_buho_final_eje_x, Cuadrado_de_la_distancia_de_buho_final_eje_x, Distancia_de_buho_final_eje_y, Cuadrado_de_la_distancia_de_buho_final_eje_y, Distancia_vectorial_de_buho, Direcci_C3_B3n_de_burla
    sprite.hide()
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet


@event.received('Inicio')
def on_received():
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho, Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y, Distancia_de_buho_final_eje_x, Cuadrado_de_la_distancia_de_buho_final_eje_x, Distancia_de_buho_final_eje_y, Cuadrado_de_la_distancia_de_buho_final_eje_y, Distancia_vectorial_de_buho, Direcci_C3_B3n_de_burla
    sprite.x = 0
    sprite.y = -180
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.hide()


def Generador_de_gravedad_N(Valor_de_gravedad):
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho, Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y, Distancia_de_buho_final_eje_x, Cuadrado_de_la_distancia_de_buho_final_eje_x, Distancia_de_buho_final_eje_y, Cuadrado_de_la_distancia_de_buho_final_eje_y, Distancia_vectorial_de_buho, Direcci_C3_B3n_de_burla
    # not supported yet
    sprite.set_variable('Velocidad Terminal', -30)
    while True:
        if Velocidad_de_Buho > sprite.get_variable('Velocidad Terminal'):
            Velocidad_de_Buho = Velocidad_de_Buho + Valor_de_gravedad
            sprite.y = sprite.y + Velocidad_de_Buho




@event.received('Juego')
def on_received1():
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho, Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y, Distancia_de_buho_final_eje_x, Cuadrado_de_la_distancia_de_buho_final_eje_x, Distancia_de_buho_final_eje_y, Cuadrado_de_la_distancia_de_buho_final_eje_y, Distancia_vectorial_de_buho, Direcci_C3_B3n_de_burla
    sprite.x = 0
    sprite.y = -180
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('Bajas de buhos', 0)
    sprite.set_variable('Creacion de buhos', 0)
    sprite.hide()
    while True:
        time.sleep(float(random.uniform((4.8 - 0.4 * sprite.get_variable('Dificultad')), (4 + 4 / ((1 + math.log(sprite.get_variable('Dificultad'))))))))
        sprite.clone('_myself_')
        v = sprite.get_variable('Creacion de buhos')
        sprite.set_variable('Creacion de buhos', v + 1)
        if not str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()




@event.received('Fin')
def on_received2():
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho, Cuadrado_de_la_distancia_de_libelula_final_eje_x, Cuadrado_de_la_distancia_de_libelula_final_eje_y, Distancia_de_buho_final_eje_x, Cuadrado_de_la_distancia_de_buho_final_eje_x, Distancia_de_buho_final_eje_y, Cuadrado_de_la_distancia_de_buho_final_eje_y, Distancia_vectorial_de_buho, Direcci_C3_B3n_de_burla
    sprite.hide()
    sprite.x = (sprite.get_variable('Posicion resumen eje x') + 0)
    sprite.y = (sprite.get_variable('Posicion resumen eje y') + 0)
    sprite.size = 30
    sprite.show()
    sprite.set_costume('Buho - Llorando')
    sprite.say(str(str('Has abatido ') + str(sprite.get_variable('Bajas de buhos'))) + str(str(' de ') + str(sprite.get_variable('Creacion de buhos'))))








# not supported yet
Distancia_de_buho_final_eje_x = ((sprite.get_property('Bala', 'x') - sprite.x))
Cuadrado_de_la_distancia_de_buho_final_eje_x = Distancia_de_buho_final_eje_x * Distancia_de_buho_final_eje_x
Distancia_de_buho_final_eje_y = ((sprite.get_property('Bala', 'y') - sprite.y))
Cuadrado_de_la_distancia_de_buho_final_eje_y = Distancia_de_buho_final_eje_y * Distancia_de_buho_final_eje_y
Distancia_vectorial_de_buho = math.sqrt((Cuadrado_de_la_distancia_de_buho_final_eje_x + Cuadrado_de_la_distancia_de_buho_final_eje_y))
while True:
    if str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
        if sprite.get_variable('Linea de horizonte') > sprite.y:
            v = sprite.get_variable('Vidas totales')
            sprite.set_variable('Vidas totales', v + -1)
            sprite.play('Low Boing')
            sprite.clone('Sprite - Calavera')
            # not supported yet

        if sprite.get_variable('Bandera de disparo') == 1:
            if sprite.touching('Bala') or Distancia_vectorial_de_buho < 5:
                v = sprite.get_variable('Puntos')
                sprite.set_variable('Puntos', v + 250 * ((0.8 + 0.2 * sprite.get_variable('Dificultad'))))
                v = sprite.get_variable('Bajas de buhos')
                sprite.set_variable('Bajas de buhos', v + 1)
                sprite.play('Chirp')
                # not supported yet



    else:
        sprite.stop_other()
        # not supported yet



# not supported yet
Destino_aleatorio_en_el_eje_x_de_buho = random.uniform(-1 * sprite.get_variable('Tope horizontal'), sprite.get_variable('Tope horizontal'))
sprite.x = Destino_aleatorio_en_el_eje_x_de_buho
sprite.y = sprite.get_variable('Linea de horizonte')
sprite.size = 30
sprite.show()
Velocidad_de_Buho = Velocidad_de_Buho + random.uniform((5 + 5 / sprite.get_variable('Dificultad')), (14 + -1 * sprite.get_variable('Dificultad')))
Generador_de_gravedad_N(-0.4)

# not supported yet
sprite.set_costume('Buho - Salto')
sprite.play('Owl')
Direcci_C3_B3n_de_burla = random.randint(0, 1)
while True:
    if Velocidad_de_Buho < 2:
        if 1 == Direcci_C3_B3n_de_burla:
            sprite.set_costume('Buho - Burla derecha')
            sprite.right(2)

        else:
            sprite.set_costume('Buho - Burla izquierda')
            sprite.left(2)


    if Velocidad_de_Buho < -4:
        sprite.set_costume('Buho - Caida')
