from mblock import event

@event.greenflag
def on_greenflag():
    while True:
        sprite.goto('mouse')
