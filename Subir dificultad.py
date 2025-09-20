from mblock import event
import time

@event.greenflag
def on_greenflag():
    while True:
        if sprite.is_mousedown and sprite.touching('mouse'):
            if sprite.get_variable('Dificultad') < 5:
                v = sprite.get_variable('Dificultad')
                sprite.set_variable('Dificultad', v + 1)
                time.sleep(0.25)
