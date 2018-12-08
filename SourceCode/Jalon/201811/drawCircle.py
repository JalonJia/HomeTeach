import turtle #导入乌龟画图模块
import math

pen = turtle.Turtle() #初始化一个画布，并生成画笔，画笔变量名为pen
pen._delay(0.01)

def draw_circle(pen, r, degree):
    total_len = 2 * math.pi * r
    step_len = total_len / 360
    for i in range(degree):
        pen.fd(step_len)
        pen.lt(1)



def draw_helical(r, n, delta):
    pen.fd(r)
    pen.lt(90)
    for i in range(n):
        draw_circle(pen, r, 180)
        r += delta

draw_helical(500, 1, 2)
#draw_helical(10, 20, 5)

turtle.mainloop()
