from mblock import event

@event.greenflag
def on_greenflag():
    sprite.hide()


@event.received('Inicio')
def on_received():
    sprite.hide()


@event.received('Opciones')
def on_received1():
    sprite.show()


@event.received('Juego')
def on_received2():
    sprite.hide()
