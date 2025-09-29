from mblock import event
import time

def Elector_de_numero_N(Numero):
    if Numero == 9:
        sprite.set_costume('ZPixel-9')

    if Numero == 8:
        sprite.set_costume('ZPixel-8')

    if Numero == 7:
        sprite.set_costume('ZPixel-7')

    if Numero == 6:
        sprite.set_costume('zPixel-6')

    if Numero == 5:
        sprite.set_costume('ZPixel-5')

    if Numero == 4:
        sprite.set_costume('ZPixel-4')

    if Numero == 3:
        sprite.set_costume('ZPixel-3')

    if Numero == 2:
        sprite.set_costume('ZPixel-2')

    if Numero == 1:
        sprite.set_costume('ZPixel-1')

    if Numero == 0:
        sprite.set_costume('ZPixel-0')



@event.greenflag
def on_greenflag():
    sprite.hide()


@event.received('Juego')
def on_received():
    sprite.x = 220
    sprite.y = -170
    time.sleep(0.1)
    sprite.show()
    while True:
        if str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
            Elector_de_numero_N((6 - sprite.get_variable('Balas - En cargador')))

        else:
            sprite.hide()
            sprite.stop_this()
