import time
from mblock import event
import math

@event.received('Inicio')
def on_received():
    sprite.hide()


@event.greenflag
def on_greenflag():
    # not supported yet
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('IU - Sup - Altura', 160)
    sprite.set_variable('IU - Sup - Posicion', -220)
    sprite.set_variable('IU - Temporizador - Separacion', 10)
    sprite.set_variable('IU - Temporizador - Contador', 0)
    sprite.x = (sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Temporizador - Separacion') * sprite.get_variable('IU - Temporizador - Contador'))
    sprite.y = sprite.get_variable('IU - Sup - Altura')
    sprite.hide()


@event.received('Juego')
def on_received1():
    sprite.show()
    sprite.set_costume('Reloj')
    sprite.set_variable('IU - Temporizador - Contador', 0)
    time.sleep(0.1)
    for count in range(3):
        if str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.clone('_myself_')




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




# not supported yet
time.sleep(0.1)
while True:
    if not str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
        # not supported yet






# not supported yet
sprite.set_costume('ZPixel-0')
v = sprite.get_variable('IU - Temporizador - Contador')
sprite.set_variable('IU - Temporizador - Contador', v + 1)
sprite.x = (sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Temporizador - Separacion') * sprite.get_variable('IU - Temporizador - Contador'))
sprite.y = sprite.get_variable('IU - Sup - Altura')
sprite.show()


# Centena
# not supported yet
time.sleep(0.1)
while True:
    if str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
        if sprite.x == (sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Temporizador - Separacion') * 1):
            Elector_de_numero_N(math.floor(sprite.get_variable('Tiempo Restante') / 100) % 10)

        if sprite.x == (sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Temporizador - Separacion') * 2):
            Elector_de_numero_N(math.floor(sprite.get_variable('Tiempo Restante') / 10) % 10)

        if sprite.x == (sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Temporizador - Separacion') * 3):
            Elector_de_numero_N(math.floor(sprite.get_variable('Tiempo Restante') / 1) % 10)


    else:
        sprite.stop_this()



# not supported yet
time.sleep(0.1)
