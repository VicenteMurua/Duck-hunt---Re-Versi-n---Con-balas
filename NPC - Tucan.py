from mblock import event
import time
import random

@event.greenflag
def on_greenflag():
    sprite.x = 0
    sprite.y = -180
    sprite.hide()


@event.received('Inicio')
def on_received():
    sprite.x = 0
    sprite.y = -180
    sprite.hide()


@event.received('Fin')
def on_received1():
    sprite.x = 0
    sprite.y = -180
    sprite.hide()


@event.received('Juego')
def on_received2():
    while True:
        time.sleep(float(random.uniform(4, (15 - sprite.get_variable('Dificultad')))))
        sprite.clone('_myself_')
        if not str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
            time.sleep(1)
            sprite.stop_other()
            sprite.stop_this()









# not supported yet
sprite.z_index = 256
sprite.show()
sprite.size = 10
sprite.x = -240
sprite.y = random.uniform(sprite.get_variable('Linea de horizonte'), (sprite.get_variable('Tope Vertical') - 100))
while True:
    if not str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
        # not supported yet

    else:
        if -180 > sprite.x:
            sprite.size = sprite.size + 5
            sprite.x = sprite.x + 5

        else:
            sprite.x = sprite.x + 3
            if sprite.touching('edge') and sprite.x > sprite.get_variable('Tope horizontal'):
                # not supported yet





# not supported yet
while True:
    if sprite.x > -180:
        sprite.left(15)
        for count in range(2):
            sprite.y = sprite.y + 20
            sprite.set_costume('Toucan - Elevación')
            time.sleep(0.1)
            sprite.set_costume('Toucan - Medio')
            time.sleep(0.1)
            sprite.set_costume('Toucan - Caida')

        sprite.right(15)
        sprite.right(15)
        for count2 in range(15):
            sprite.y = sprite.y + -2

        sprite.left(15)
        time.sleep(0.1)
