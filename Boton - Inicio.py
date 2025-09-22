from mblock import event

@event.received('Opciones')
def on_received():
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.broadcast(str('Inicio'))




@event.received('Inicio')
def on_received1():
    sprite.hide()
    sprite.stop_other()


@event.received('Juego')
def on_received2():
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.broadcast(str('Inicio'))
