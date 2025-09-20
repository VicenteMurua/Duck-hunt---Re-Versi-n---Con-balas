import time
from mblock import event

def Posicionamiento_de_Arma():
    while True:
        sprite.goto('mouse')
        sprite.towards('mouse')
        sprite.x = sprite.x + 120
        sprite.y = sprite.y + -120



def Animaci_C3_B3n_de_disparo():
    while True:
        if sprite.is_mousedown:
            sprite.clone('Bala')
            sprite.right(15)
            time.sleep(0.1)
            while not not sprite.is_mousedown:
                pass

            sprite.left(15)
            time.sleep(0.1)




@event.greenflag
def on_greenflag():
    Posicionamiento_de_Arma()


@event.greenflag
def on_greenflag1():
    Animaci_C3_B3n_de_disparo()
