from mblock import event

@event.greenflag
def on_greenflag():
    sprite.hide()


@event.received('Inicio')
def on_received():
    sprite.show()
    sprite.x = 0
    sprite.y = 0
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.play('pop')
            sprite.broadcast(str('Juego'))
            sprite.hide()
            sprite.stop_this()




@event.received('Opciones')
def on_received1():
    sprite.x = 100
    sprite.y = 0
    sprite.hide()
    sprite.stop_other()
