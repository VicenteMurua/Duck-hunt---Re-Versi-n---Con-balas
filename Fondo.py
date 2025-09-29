from mblock import event
import time

@event.greenflag
def on_greenflag():
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('Tope horizontal', 240)
    sprite.set_variable('Tope Vertical', 180)
    sprite.set_variable('Linea de horizonte', -45)
    # not supported yet
    # not supported yet
    sprite.set_variable('Posicion resumen eje x', -200)
    sprite.set_variable('Posicion resumen eje y', -15)
    # not supported yet
    # not supported yet
    sprite.set_variable('Menú - Poscición', 0)
    sprite.set_variable('Menú - Separacion', -40)
    sprite.set_variable('Objetivo -  libelulas', 20)


@event.greenflag
def on_greenflag1():
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('Dificultad', 1)
    sprite.set_variable('Vidas extra', 0)
    sprite.set_variable('Multiplicador de puntaje', 1)
    # not supported yet
    sprite.broadcast(str('Inicio'))
    sprite.volume = 100


@event.received('Opciones')
def on_received():
    sprite.set_backdrop('O - Opciones')


@event.received('Inicio')
def on_received1():
    sprite.set_backdrop('Inicio')
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet


@event.received('Inicio')
def on_received2():
    sprite.set_variable('Tiempo Total', ((65 - 5 * sprite.get_variable('Dificultad'))))
    sprite.set_variable('Tiempo Restante', sprite.get_variable('Tiempo Total'))


@event.received('Instrucciones')
def on_received3():
    sprite.set_backdrop('O - Instrucciones')


@event.received('Creditos')
def on_received4():
    sprite.set_backdrop('O - Creditos')


@event.received('Juego')
def on_received5():
    # not supported yet
    sprite.set_variable('Balas disparadas', 0)
    sprite.set_variable('Tiempo Restante', sprite.get_variable('Tiempo Total'))
    # not supported yet
    sprite.set_variable('Puntos', 0)
    # not supported yet
    # not supported yet
    sprite.set_variable('Vidas iniciales', 3)
    sprite.set_variable('Vidas totales', ((sprite.get_variable('Vidas iniciales') + sprite.get_variable('Vidas extra'))))
    sprite.set_variable('Puntaje final', 0)
    # not supported yet
    while True:
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()

        if sprite.get_variable('Bajas de libelulas') > (sprite.get_variable('Objetivo -  libelulas') - 1) or sprite.get_variable('Bajas de libelulas') == sprite.get_variable('Objetivo -  libelulas'):
            sprite.broadcast(str('Fin'))
            sprite.stop_this()




@event.received('Juego')
def on_received6():
    sprite.set_backdrop('juego')
    time.sleep(0.1)
    for count in range(int(sprite.get_variable('Tiempo Total'))):
        time.sleep(1)
        v = sprite.get_variable('Tiempo Restante')
        sprite.set_variable('Tiempo Restante', v + -1)
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()


    sprite.broadcast(str('Fin'))


@event.received('Juego')
def on_received7():
    sprite.set_backdrop('juego')
    time.sleep(0.1)
    while not sprite.get_variable('Vidas totales') < 1:
        if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.stop_this()


    sprite.broadcast(str('Fin'))


@event.received('Fin')
def on_received8():
    sprite.set_backdrop('Fin')
    sprite.set_variable('Puntaje final', (((0.8 + 0.2 * sprite.get_variable('Dificultad'))) * sprite.get_variable('Multiplicador de puntaje')) * round((((sprite.get_variable('Puntos') + sprite.get_variable('Vidas totales') * 10)) * ((sprite.get_variable('Tiempo Total') * 100) / ((sprite.get_variable('Tiempo Total') - sprite.get_variable('Tiempo Restante')))))))
    time.sleep(0.1)
    if sprite.get_variable('Bajas de libelulas') > (sprite.get_variable('Objetivo -  libelulas') - 1) or sprite.get_variable('Bajas de libelulas') == sprite.get_variable('Objetivo -  libelulas'):
        sprite.play('Win')
        sprite.set_backdrop('Fin - Ganador')
        # not supported yet

    if 1 > sprite.get_variable('Tiempo Restante'):
        sprite.set_backdrop('Fin - 0Tienpo')
        # not supported yet

    if 1 > sprite.get_variable('Vidas totales'):
        sprite.set_backdrop('Fin - 0Vidas')
        # not supported yet
