import turtle
pen = turtle.Turtle()
pen.lt(45)
l = 360/2
for im in range(20):
    j = 1
    for i in range(100):
        pen.fd(3)
        pen.lt(1)
        j *= 2
