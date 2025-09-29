from mblock import event
import time

@event.received('Inicio')
def on_received():
    sprite.hide()


@event.received('Opciones')
def on_received1():
    sprite.set_costume('Aumentar')
    sprite.show()
    sprite.z_index = 256
    sprite.x = 40
    sprite.y = 70
    sprite.clone('_myself_')
    time.sleep(0.1)
    while True:
        if str('O').find(str(sprite.backdrop_index('name')[0])) > -1:
            if sprite.is_mousedown and sprite.touching('mouse'):
                if sprite.get_variable('Dificultad') < 5:
                    v = sprite.get_variable('Dificultad')
                    sprite.set_variable('Dificultad', v + 1)
                    while not not sprite.is_mousedown:
                        pass

                    sprite.say(sprite.get_variable('Dificultad'), 0.5)

                else:
                    sprite.say(str(sprite.get_variable('Dificultad')) + str(' es la dificultad maxima!'), 1)



        else:
            sprite.say('Error paro de ejecutarse', 2)
            sprite.stop_this()







# not supported yet
sprite.x = -40
sprite.y = sprite.y
sprite.set_costume('Disminuir')
sprite.show()
while True:
    if str('o').find(str(sprite.backdrop_index('name')[0])) > -1:
        if sprite.is_mousedown and sprite.touching('mouse'):
            if 1 < sprite.get_variable('Dificultad'):
                v = sprite.get_variable('Dificultad')
                sprite.set_variable('Dificultad', v + -1)
                while not not sprite.is_mousedown:
                    pass

                sprite.say(sprite.get_variable('Dificultad'), 0.5)

            else:
                sprite.say(str(sprite.get_variable('Dificultad')) + str(' es la dificultad minima!'), 1)



    else:
        # not supported yet
