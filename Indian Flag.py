import turtle
a = turtle.Turtle()
a.speed(3)
a.pensize(5)
a.color('#000080')
def flag(x,y):
    a.penup()
    a.goto(x,y)
    a.pendown()
for i in range(24):
    a.forward(80)
    a.backward(80)
    a.left(15)
flag(0, -80)
a.circle(80, 360)

flag(0,-90)


a.color('#138808')
a.begin_fill()

a.forward(350)
a.backward(700)
a.right(90)
a.forward(200)
a.left(90)
a.forward(700)
a.left(90)
a.forward(200)
a.left(90)

a.end_fill()



a.color('#FF9933')
flag(-350,90)

a.begin_fill()

a.right(180)
a.forward(700)
a.left(90)
a.forward(200)
a.left(90)
a.forward(700)
a.left(90)
a.forward(200)

a.end_fill()

a.hideturtle()

turtle.done()