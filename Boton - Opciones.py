from mblock import event

@event.greenflag
def on_greenflag():
    sprite.hide()
    sprite.x = 0
    sprite.y = -70


@event.received('Inicio')
def on_received():
    sprite.show()
    sprite.x = 0
    sprite.y = (sprite.get_variable('Menú - Poscición') + sprite.get_variable('Menú - Separacion') * 2)
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


@event.received('Instrucciones')
def on_received3():
    sprite.hide()
    sprite.stop_other()


@event.received('Creditos')
def on_received4():
    sprite.hide()
    sprite.stop_other()
