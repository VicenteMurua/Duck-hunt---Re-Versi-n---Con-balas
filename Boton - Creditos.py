from mblock import event

@event.greenflag
def on_greenflag():
    sprite.hide()
    sprite.x = 0
    sprite.y = 0


@event.received('Inicio')
def on_received():
    sprite.x = 0
    sprite.y = (sprite.get_variable('Menú - Poscición') + sprite.get_variable('Menú - Separacion') * 3)
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.play('pop')
            sprite.broadcast(str('Creditos'))
            sprite.hide()
            sprite.stop_this()




@event.received('Creditos')
def on_received1():
    sprite.hide()
    sprite.stop_other()


@event.received('Juego')
def on_received2():
    sprite.hide()
    sprite.stop_other()


@event.received('Opciones')
def on_received3():
    sprite.hide()
    sprite.stop_other()


@event.received('Instrucciones')
def on_received4():
    sprite.hide()
    sprite.stop_other()
