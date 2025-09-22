from mblock import event

@event.received('Inicio')
def on_received():
    sprite.direction = 90
    sprite.stop_other()
    sprite.set_costume('Shield1')
    while True:
        sprite.goto('mouse')
        sprite.left(8)



@event.received('Juego')
def on_received1():
    sprite.direction = 90
    sprite.stop_other()
    sprite.set_costume('Mira de Arma')
    while True:
        sprite.goto('mouse')



@event.received('Fin')
def on_received2():
    sprite.direction = 90
    sprite.stop_other()
    sprite.set_costume('Shield1')
    while True:
        sprite.goto('mouse')
        sprite.left(8)
