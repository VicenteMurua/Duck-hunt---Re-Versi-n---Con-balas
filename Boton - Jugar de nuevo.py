from mblock import event

@event.greenflag
def on_greenflag():
    sprite.hide()


@event.received('Fin')
def on_received():
    sprite.show()
    sprite.x = 0
    sprite.y = -120
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.play('pop')
            sprite.broadcast(str('Juego'))
            sprite.hide()
            sprite.stop_this()




@event.received('Juego')
def on_received1():
    sprite.hide()
    sprite.stop_other()


@event.received('Inicio')
def on_received2():
    sprite.hide()
    sprite.stop_other()
