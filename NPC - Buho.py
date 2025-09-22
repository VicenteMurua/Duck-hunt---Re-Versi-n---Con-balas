from mblock import event
import time
import random

Destino_aleatorio_en_el_eje_x_de_buho = 0
Velocidad_de_Buho = 0

@event.greenflag
def on_greenflag():
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho
    sprite.hide()
    sprite.x = 0
    sprite.y = -180


@event.received('Inicio')
def on_received():
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho
    sprite.hide()


@event.received('Fin')
def on_received1():
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho
    sprite.hide()


@event.received('Juego')
def on_received2():
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho
    sprite.hide()
    while True:
        time.sleep(float(random.uniform(2, ((15 - sprite.get_variable('Dificultad'))) / 2)))
        sprite.clone('_myself_')
        if not str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()




def Generador_de_gravedad_N(Valor_de_gravedad):
    global Destino_aleatorio_en_el_eje_x_de_buho, Velocidad_de_Buho
    while True:
        # not supported yet
        # not supported yet
        sprite.set_variable('Velocidad Terminal', -30)
        if Velocidad_de_Buho > sprite.get_variable('Velocidad Terminal'):
            Velocidad_de_Buho = Velocidad_de_Buho + Valor_de_gravedad
            sprite.y = sprite.y + Velocidad_de_Buho

        if sprite.get_variable('Linea de horizonte') > sprite.y:
            # not supported yet










# not supported yet
Destino_aleatorio_en_el_eje_x_de_buho = random.uniform(-1 * sprite.get_variable('Tope horizontal'), sprite.get_variable('Tope horizontal'))
sprite.x = Destino_aleatorio_en_el_eje_x_de_buho
sprite.y = sprite.get_variable('Linea de horizonte')
sprite.size = 30
sprite.show()
Velocidad_de_Buho = Velocidad_de_Buho + 10
Generador_de_gravedad_N(-0.4)

# not supported yet
while True:
    if not str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
        sprite.stop_other()
        # not supported yet
