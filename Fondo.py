from mblock import event
import time

@event.greenflag
def on_greenflag():
    sprite.set_variable('Bandera - Inicio', 0)
    sprite.set_variable('Bandera - Juego', 0)
    sprite.set_variable('Bandera - Fin', 0)
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('Dificultad', 1)
    sprite.broadcast(str('Inicio'))
    sprite.volume = 100


def Reset_de_Estado():
    if 2 < sprite.get_variable('Bandera - Inicio') or 2 < sprite.get_variable('Bandera - Juego') or 2 < sprite.get_variable('Bandera - Fin'):
        v = sprite.get_variable('Bandera - Inicio')
        sprite.set_variable('Bandera - Inicio', v + -1)
        v = sprite.get_variable('Bandera - Juego')
        sprite.set_variable('Bandera - Juego', v + -1)
        v = sprite.get_variable('Bandera - Fin')
        sprite.set_variable('Bandera - Fin', v + -1)
        if 0 > sprite.get_variable('Bandera - Inicio'):
            v = sprite.get_variable('Bandera - Fin')
            sprite.set_variable('Bandera - Fin', v + 1)

        if 0 > sprite.get_variable('Bandera - Juego'):
            v = sprite.get_variable('Bandera - Fin')
            sprite.set_variable('Bandera - Fin', v + 1)

        if 0 > sprite.get_variable('Bandera - Fin'):
            v = sprite.get_variable('Bandera - Fin')
            sprite.set_variable('Bandera - Fin', v + 1)


    time.sleep(0.1)


@event.received('Inicio')
def on_received():
    v = sprite.get_variable('Bandera - Inicio')
    sprite.set_variable('Bandera - Inicio', v + 1)
    sprite.set_backdrop('Inicio')
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('Tope horizontal', 240)
    sprite.set_variable('Tope Vertical', 180)
    sprite.set_variable('Linea de horizonte', -45)
    sprite.set_variable('Tiempo Partida', 30)
    # not supported yet
    # not supported yet


@event.received('Opciones')
def on_received1():
    sprite.set_backdrop('Opciones')


@event.received('Juego')
def on_received2():
    sprite.set_variable('Bandera - Juego', 1)
    sprite.set_variable('Puntos', 0)
    # not supported yet
    while True:
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()

        if sprite.get_variable('Puntos') > 100 or sprite.get_variable('Puntos') == 100:
            sprite.broadcast(str('Fin'))
            sprite.stop_this()




@event.received('Juego')
def on_received3():
    # not supported yet
    sprite.set_backdrop('juego')
    while not (sprite.get_variable('Tiempo Partida') < 1 or sprite.get_variable('Tiempo Partida') == 0):
        time.sleep(1)
        v = sprite.get_variable('Tiempo Partida')
        sprite.set_variable('Tiempo Partida', v + -1)
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()


    sprite.broadcast(str('Fin'))


@event.received('Fin')
def on_received4():
    sprite.set_variable('Bandera - Fin', 1)
    sprite.set_backdrop('Fin')
