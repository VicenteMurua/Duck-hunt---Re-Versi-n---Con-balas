import time
from mblock import event

def Animaci_C3_B3n_recarga():
    sprite.play('Crank')
    sprite.right(45)
    sprite.set_costume('Arma - Cargada5')
    time.sleep(0.1)
    sprite.set_costume('Arma - Cargada6')
    time.sleep(0.1)
    sprite.set_costume('Arma - Cargada7')
    time.sleep(0.1)
    sprite.set_costume('Arma - Cargada6')
    time.sleep(0.1)
    sprite.set_costume('Arma - Cargada')
    sprite.left(45)
    sprite.set_variable('Balas - En cargador', 0)


def Animaci_C3_B3n_de_disparo():
    while True:
        if str('j').find(str(sprite.backdrop_index('name')[0])) > -1:
            if sprite.is_mousedown:
                sprite.clone('Bala')
                sprite.right(15)
                time.sleep(0.1)
                while not not sprite.is_mousedown:
                    pass

                if not sprite.get_variable('Balas - En cargador') == 0 and sprite.get_variable('Balas - En cargador') % sprite.get_variable('Cargador - Balas totales') == 0:
                    Animaci_C3_B3n_recarga()

                sprite.left(15)
                time.sleep(0.1)

            if sprite.is_keypressed('r'):
                Animaci_C3_B3n_recarga()


        else:
            sprite.stop_this()




@event.greenflag
def on_greenflag():
    sprite.hide()
    # not supported yet
    # not supported yet
    sprite.set_variable('Cargador - Balas totales', 6)


@event.received('Juego')
def on_received():
    sprite.set_variable('Balas - En cargador', 0)
    time.sleep(0.1)
    Posicionamiento_de_Arma()


@event.received('Juego')
def on_received1():
    time.sleep(0.1)
    Animaci_C3_B3n_de_disparo()


@event.received('Inicio')
def on_received2():
    sprite.hide()
    sprite.stop_other()


@event.received('Fin')
def on_received3():
    sprite.hide()
    sprite.stop_other()


def Posicionamiento_de_Arma():
    sprite.set_costume('Arma - Cargada')
    sprite.show()
    sprite.z_index = 256
    sprite.direction = 90
    if str('j').find(str(sprite.backdrop_index('name')[0])) > -1:
        while True:
            sprite.goto('mouse')
            sprite.x = sprite.x + 120
            sprite.y = sprite.y + -120


    else:
        sprite.stop_this()
