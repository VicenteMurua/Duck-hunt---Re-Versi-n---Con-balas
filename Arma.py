import time
from mblock import event

def Animaci_C3_B3n_de_disparo():
    while True:
        if str('j').find(str(sprite.backdrop_index('name')[0])) > -1:
            if sprite.is_mousedown:
                sprite.clone('Bala')
                sprite.right(15)
                time.sleep(0.1)
                while not not sprite.is_mousedown:
                    pass

                sprite.left(15)
                time.sleep(0.1)


        else:
            sprite.stop_this()




def Posicionamiento_de_Arma():
    sprite.show()
    if str('j').find(str(sprite.backdrop_index('name')[0])) > -1:
        while True:
            sprite.goto('mouse')
            sprite.towards('mouse')
            sprite.x = sprite.x + 120
            sprite.y = sprite.y + -120


    else:
        sprite.stop_this()



@event.greenflag
def on_greenflag():
    sprite.hide()


@event.received('Inicio')
def on_received():
    sprite.stop_other()


@event.received('Fin')
def on_received1():
    sprite.hide()
    sprite.stop_other()


@event.received('Juego')
def on_received2():
    time.sleep(0.1)
    Posicionamiento_de_Arma()


@event.received('Juego')
def on_received3():
    time.sleep(0.1)
    Animaci_C3_B3n_de_disparo()
