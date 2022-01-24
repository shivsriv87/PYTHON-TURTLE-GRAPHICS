from turtle import *

state = {'turn': 0}


def spinner():
    "Draw fidget spinner."
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(200, 'red')
    back(100)
    right(120)
    forward(100)
    dot(200, 'green')
    back(100)
    right(120)
    forward(100)
    dot(200, 'yellow')
    back(100)
    right(120)
    update()


def animate():
    "Animate fidget spinner."
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)


def flick():
    "Flick fidget spinner."
    state['turn'] += 20


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'w')
listen()
animate()
done()