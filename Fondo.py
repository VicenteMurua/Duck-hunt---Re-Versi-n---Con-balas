from mblock import event
import time

@event.greenflag
def on_greenflag():
    sprite.set_backdrop('Desert3')
    sprite.set_variable('Tope horizontal', 240)
    # not supported yet
    sprite.set_variable('Tope Vertical', 180)
    # not supported yet
    sprite.set_variable('Linea de horizonte', -45)
    # not supported yet
    sprite.set_variable('Tiempo Partida', 30)
    sprite.set_variable('Dificultad', 1)
    sprite.set_variable('Puntos', 0)
    while True:
        if sprite.get_variable('Puntos') > 100 or sprite.get_variable('Puntos') == 100:
            sprite.set_backdrop('Desert2')
            sprite.stop_all()




@event.greenflag
def on_greenflag1():
    for count in range(int(sprite.get_variable('Tiempo Partida'))):
        time.sleep(1)
        v = sprite.get_variable('Tiempo Partida')
        sprite.set_variable('Tiempo Partida', v + -1)

    sprite.set_backdrop('Desert2')
    sprite.stop_all()
