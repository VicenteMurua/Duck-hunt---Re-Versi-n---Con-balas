from mblock import event

@event.received('Opciones')
def on_received():
    sprite.stop_other()
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.broadcast(str('Inicio'))




@event.received('Inicio')
def on_received1():
    sprite.stop_other()
    sprite.hide()


@event.received('Juego')
def on_received2():
    sprite.stop_other()
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.broadcast(str('Inicio'))




@event.received('Instrucciones')
def on_received3():
    sprite.stop_other()
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.broadcast(str('Inicio'))




@event.received('Fin')
def on_received4():
    sprite.stop_other()
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.broadcast(str('Inicio'))




@event.received('Creditos')
def on_received5():
    sprite.stop_other()
    sprite.show()
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            sprite.broadcast(str('Inicio'))
