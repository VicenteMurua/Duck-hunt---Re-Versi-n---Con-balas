from mblock import event
import time

@event.greenflag
def on_greenflag():
    sprite.x = 0
    sprite.y = -180
    sprite.hide()


@event.received('Inicio')
def on_received():
    sprite.x = 0
    sprite.y = -180
    sprite.hide()


@event.received('Fin')
def on_received1():
    sprite.x = (sprite.get_variable('Posicion resumen eje x') + 150)
    sprite.y = (sprite.get_variable('Posicion resumen eje y') + -50)
    sprite.size = 30
    sprite.show()
    if sprite.get_variable('Balas disparadas') == 0:
        sprite.think('Parece  que no has disparado')

    else:
        sprite.say(str(str('Haz acertado ') + str((sprite.get_variable('Bajas de buhos') + sprite.get_variable('Bajas de libelulas')))) + str(str(' veces, precision  de ') + str(str(round(((((sprite.get_variable('Bajas de buhos') + sprite.get_variable('Bajas de libelulas'))) * 100) / sprite.get_variable('Balas disparadas')))) + str('%'))))



@event.received('Juego')
def on_received2():
    sprite.set_draggable(False)
    sprite.x = 0
    sprite.y = -180
    sprite.hide()
    sprite.set_variable('Bandera de disparo', 0)


@event.received('Juego')
def on_received3():
    # not supported yet
    # not supported yet
    # not supported yet








# not supported yet
v = sprite.get_variable('Balas disparadas')
sprite.set_variable('Balas disparadas', v + 1)
v = sprite.get_variable('Balas - En cargador')
sprite.set_variable('Balas - En cargador', v + 1)
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
time.sleep(0.05)
sprite.set_variable('Bandera de disparo', 0)
# not supported yet

# not supported yet
time.sleep(0.1)
while True:
    sprite.size = sprite.size + -5
