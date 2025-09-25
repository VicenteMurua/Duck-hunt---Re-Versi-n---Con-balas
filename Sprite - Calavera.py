from mblock import event
import time

@event.received('Inicio')
def on_received():
    sprite.hide()


@event.received('Juego')
def on_received1():
    sprite.x = 180
    sprite.y = 150
    sprite.direction = 90
    sprite.hide()





# not supported yet
sprite.x = (sprite.x - sprite.get_variable('Constructor de vida') * sprite.get_variable('Espacio de corazones'))
sprite.y = sprite.y
v = sprite.get_variable('Constructor de vida')
sprite.set_variable('Constructor de vida', v + -1)
sprite.show()
sprite.play('Oops')
sprite.size = 10
for count in range(2):
    sprite.size = sprite.size + 5
    time.sleep(0.25)


# not supported yet
time.sleep(0.2)
while True:
    if sprite.touching('Sprite - Corazon'):
        # not supported yet



# not supported yet
while True:
    if str('I').find(str(sprite.backdrop_index('name')[0])) > -1 or str('F').find(str(sprite.backdrop_index('name')[0])) > -1:
        # not supported yet
