from mblock import event
import time

@event.greenflag
def on_greenflag():
    while True:
        if sprite.touching('mouse') and sprite.is_mousedown:
            if sprite.get_variable('Dificultad') > 1:
                v = sprite.get_variable('Dificultad')
                sprite.set_variable('Dificultad', v + -1)
                time.sleep(0.25)
