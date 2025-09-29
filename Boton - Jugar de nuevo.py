from mblock import event
import time

@event.greenflag
def on_greenflag():
    sprite.hide()


@event.received('Fin')
def on_received():
    sprite.show()
    time.sleep(0.1)
    sprite.x = 0
    sprite.y = -120
    while True:
        if str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
            if sprite.is_mousedown and sprite.touching('mouse'):
                sprite.play('pop')
                sprite.broadcast(str('Juego'))
                sprite.hide()
                sprite.stop_this()


        else:
            sprite.hide()
            sprite.stop_this()
