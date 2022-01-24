import turtle
a=["red","green","blue","yellow","magenta","orange","purple","pink"]
t=turtle.Pen()
turtle.bgcolor("black")
for i in  range(360):
    t.pencolor(a[i%8])
    t.width(i//100+1)
    t.forward(i)
    t.left(59)
