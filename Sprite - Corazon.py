from mblock import event
import time

@event.received('Juego')
def on_received():
    sprite.x = 180
    sprite.y = 150
    sprite.direction = 90
    sprite.hide()
    sprite.set_variable('Constructor de vida', 0)
    sprite.set_variable('Espacio de corazones', 30)
    time.sleep(1)
    if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
        sprite.set_variable('Constructor de vida', 0)
        sprite.stop_this()

    for count in range(int(sprite.get_variable('Vidas totales'))):
        sprite.clone('_myself_')
        time.sleep(0.2)



@event.received('Inicio')
def on_received1():
    # not supported yet
    # not supported yet
    sprite.hide()


def Animaci_C3_B3n_de_corazon():
    time.sleep(0.3)
    sprite.left(20)
    time.sleep(0.3)
    sprite.right(20)
    time.sleep(0.3)
    sprite.right(20)
    time.sleep(0.3)
    sprite.left(20)


def Salto():
    time.sleep(0.2)
    sprite.y = sprite.y + 10
    time.sleep(0.05)
    sprite.y = sprite.y + -10
    time.sleep(0.05)






# not supported yet
while True:
    if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
        # not supported yet



# not supported yet
v = sprite.get_variable('Constructor de vida')
sprite.set_variable('Constructor de vida', v + 1)
sprite.show()
sprite.play('pop')
sprite.size = 10
sprite.x = (sprite.x - sprite.get_variable('Constructor de vida') * sprite.get_variable('Espacio de corazones'))
sprite.y = sprite.y
Animaci_C3_B3n_de_corazon()
sprite.size = 20
Salto()
while True:
    time.sleep(3)
    Animaci_C3_B3n_de_corazon()
    Salto()


# not supported yet
time.sleep(0.2)
while True:
    if sprite.touching('Sprite - Calavera'):
        # not supported yet
