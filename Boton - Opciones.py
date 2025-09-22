from mblock import event

@event.greenflag
def on_greenflag():
    sprite.hide()


@event.received('Inicio')
def on_received():
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.play('pop')
            sprite.broadcast(str('Opciones'))
            sprite.hide()
            sprite.stop_this()




@event.received('Opciones')
def on_received1():
    sprite.hide()
    sprite.stop_other()


@event.received('Juego')
def on_received2():
    sprite.hide()
    sprite.stop_other()
