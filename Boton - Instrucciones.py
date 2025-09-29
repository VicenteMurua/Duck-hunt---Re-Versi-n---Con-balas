from mblock import event

@event.greenflag
def on_greenflag():
    sprite.hide()
    sprite.x = 0
    sprite.y = -35


@event.received('Inicio')
def on_received():
    sprite.x = 0
    sprite.y = (sprite.get_variable('Menú - Poscición') + sprite.get_variable('Menú - Separacion') * 1)
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.play('pop')
            sprite.broadcast(str('Instrucciones'))
            sprite.hide()
            sprite.stop_this()




@event.received('Opciones')
def on_received1():
    sprite.stop_other()
    sprite.hide()


@event.received('Juego')
def on_received2():
    sprite.stop_other()
    sprite.hide()


@event.received('Creditos')
def on_received3():
    sprite.stop_other()
    sprite.hide()


@event.received('Instrucciones')
def on_received4():
    sprite.show()
    sprite.x = 0
    sprite.y = 160
    sprite.stop_other()
