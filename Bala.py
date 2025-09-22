import time
from mblock import event

@event.received('Juego')
def on_received():
    sprite.set_draggable(False)
    sprite.x = 0
    sprite.y = -180
    sprite.hide()
    sprite.set_variable('Bandera de disparo', 0)


@event.received('Juego')
def on_received1():
    # not supported yet
    # not supported yet
    # not supported yet



# not supported yet
sprite.goto('Arma')
sprite.towards('mouse')
sprite.size = 70
sprite.x = sprite.x + -50
sprite.y = sprite.y + 50
sprite.set_variable('Posición x de disparo', sprite.mousex)
sprite.set_variable('Posición y de disparo', sprite.mousey)
# not supported yet
# not supported yet
time.sleep(0.5)
# not supported yet



# not supported yet
sprite.show()
sprite.play('Tennis Hit')
sprite.glide(sprite.get_variable('Posición x de disparo'), sprite.get_variable('Posición y de disparo'), 0.25)
sprite.set_variable('Bandera de disparo', 1)
time.sleep(0.1)
sprite.set_variable('Bandera de disparo', 0)
# not supported yet

# not supported yet
time.sleep(0.1)
while True:
    sprite.size = sprite.size + -5
