import turtle #导入乌龟画图模块
import math

pen = turtle.Turtle() #初始化一个画布，并生成画笔，画笔变量名为pen
pen._delay(0.01)

def draw_circle(pen, r, degree):
    total_len = 2 * math.pi * r * degree / 360
    step_len = 2
    steps = int(total_len / step_len)
    for i in range(steps):
        pen.fd(step_len)
        pen.lt(degree/steps)




r = 100
pen.fd(r)
pen.lt(90)
for i in range(6):
    draw_circle(pen, r, 180)
    r += 50

turtle.mainloop()
