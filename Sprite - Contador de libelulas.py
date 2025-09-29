from mblock import event
import time
import math

@event.received('Inicio')
def on_received():
    sprite.hide()


@event.greenflag
def on_greenflag():
    # not supported yet
    # not supported yet
    # not supported yet
    sprite.set_variable('IU - Libelulas - Separacion', 50)
    sprite.hide()


@event.received('Juego')
def on_received1():
    sprite.set_variable('IU - Libelulas - Contador', 0)
    sprite.size = 10
    sprite.set_costume('Dragonfly')
    sprite.show()
    time.sleep(0)
    sprite.x = (((sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Libelulas - Separacion'))) + sprite.get_variable('IU - Temporizador - Separacion') * sprite.get_variable('IU - Libelulas - Contador'))
    sprite.y = sprite.get_variable('IU - Sup - Altura')
    for count in range(5):
        if str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
            sprite.clone('_myself_')




@event.received('Fin')
def on_received2():
    pass

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
sprite.size = 20
v = sprite.get_variable('IU - Libelulas - Contador')
sprite.set_variable('IU - Libelulas - Contador', v + 1)
sprite.x = (((sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Libelulas - Separacion'))) + sprite.get_variable('IU - Temporizador - Separacion') * sprite.get_variable('IU - Libelulas - Contador'))
sprite.y = sprite.get_variable('IU - Sup - Altura')
sprite.set_costume('ZPixel-0')
sprite.show()





# not supported yet
time.sleep(0.1)
while True:
    if str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
        if sprite.x == (((sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Libelulas - Separacion'))) + sprite.get_variable('IU - Temporizador - Separacion') * 1):
            Elector_de_numero_N(math.floor(sprite.get_variable('Bajas de libelulas') / 10) % 10)

        if sprite.x == (((sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Libelulas - Separacion'))) + sprite.get_variable('IU - Temporizador - Separacion') * 2):
            Elector_de_numero_N(math.floor(sprite.get_variable('Bajas de libelulas') / 1) % 10)

        if sprite.x == (((sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Libelulas - Separacion'))) + sprite.get_variable('IU - Temporizador - Separacion') * 3):
            sprite.set_costume('ZPixell-Barra')

        if sprite.x == (((sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Libelulas - Separacion'))) + sprite.get_variable('IU - Temporizador - Separacion') * 4):
            Elector_de_numero_N(math.floor(sprite.get_variable('Objetivo -  libelulas') / 10) % 10)

        if sprite.x == (((sprite.get_variable('IU - Sup - Posicion') + sprite.get_variable('IU - Libelulas - Separacion'))) + sprite.get_variable('IU - Temporizador - Separacion') * 5):
            Elector_de_numero_N(math.floor(sprite.get_variable('Objetivo -  libelulas') / 1) % 10)


    else:
        # not supported yet




# not supported yet
time.sleep(0.1)
while True:
    if not str('J').find(str(sprite.backdrop_index('name')[0])) > -1:
        pass



sprite.stop_this()
