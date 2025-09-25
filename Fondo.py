from mblock import event
import time

@event.greenflag
def on_greenflag():
    sprite.set_variable('Dificultad', 1)
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('Posicion resumen eje x', -110)
    # not supported yet
    sprite.set_variable('Posicion resumen eje y', -15)
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
    sprite.set_backdrop('Inicio')
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('Tope horizontal', 240)
    sprite.set_variable('Tope Vertical', 180)
    sprite.set_variable('Linea de horizonte', -45)
    # not supported yet
    # not supported yet
    sprite.set_variable('Tiempo Total', 30)
    sprite.set_variable('Tiempo Partida', sprite.get_variable('Tiempo Total'))
    # not supported yet
    sprite.set_variable('Vidas extra', 0)
    # not supported yet


@event.received('Opciones')
def on_received1():
    sprite.set_backdrop('Opciones')


@event.received('Juego')
def on_received2():
    sprite.set_variable('Balas disparadas', 0)
    sprite.set_variable('Tiempo Partida', sprite.get_variable('Tiempo Total'))
    # not supported yet
    sprite.set_variable('Puntos', 0)
    # not supported yet
    # not supported yet
    sprite.set_variable('Vidas iniciales', 3)
    sprite.set_variable('Vidas totales', ((sprite.get_variable('Vidas iniciales') + sprite.get_variable('Vidas extra'))))
    sprite.set_variable('Multiplicador de puntaje', 100)
    sprite.set_variable('Puntaje final', 0)
    # not supported yet
    # not supported yet
    while True:
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()

        if sprite.get_variable('Puntos') > 500 or sprite.get_variable('Puntos') == 500:
            sprite.broadcast(str('Fin'))
            sprite.stop_this()




@event.received('Juego')
def on_received3():
    sprite.set_backdrop('juego')
    time.sleep(0.1)
    # not supported yet
    for count in range(int(sprite.get_variable('Tiempo Total'))):
        time.sleep(1)
        v = sprite.get_variable('Tiempo Partida')
        sprite.set_variable('Tiempo Partida', v + -1)
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()


    sprite.broadcast(str('Fin'))


@event.received('Juego')
def on_received4():
    sprite.set_backdrop('juego')
    time.sleep(0.1)
    # not supported yet
    while not (sprite.get_variable('Vidas totales') < 1 or sprite.get_variable('Vidas totales') == 0):
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()


    sprite.broadcast(str('Fin'))


@event.received('Fin')
def on_received5():
    sprite.set_backdrop('Fin')
    sprite.set_variable('Puntaje final', (sprite.get_variable('Dificultad') * sprite.get_variable('Multiplicador de puntaje')) * round((((sprite.get_variable('Puntos') + sprite.get_variable('Vidas totales') * 10)) * ((30 * 100) / ((30 - sprite.get_variable('Tiempo Partida')))))))
    time.sleep(0.1)
    if sprite.get_variable('Puntos') > 500 or sprite.get_variable('Puntos') == 500:
        sprite.play('Win')
        sprite.set_backdrop('Fin - Ganador')
        # not supported yet

    if 1 > sprite.get_variable('Tiempo Partida') or sprite.get_variable('Tiempo Partida') == 1:
        sprite.set_backdrop('Fin - 0Tienpo')
        # not supported yet

    if 1 > sprite.get_variable('Vidas totales') or sprite.get_variable('Vidas totales') == 0:
        sprite.set_backdrop('Fin - 0Vidas')
        # not supported yet
