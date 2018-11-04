import turtle #导入乌龟画图模块

pen = turtle.Turtle() #初始化一个画布，并生成画笔，画笔变量名为pen

#正方形
pen.fd(100) #向前
pen.lt(90)

n.lt(90) #拐弯
pen.fd(100) 
pen.lt(90) #拐弯
pen.fd(100) 
pen.lt(90) #拐弯
pen.fd(100)
pen.lt(90) #拐弯



#清楚屏幕
pen.clear()

#长方形
pen.fd(200) #向前
pen.lt(90) #拐弯
pen.fd(100) 
pen.lt(90) #拐弯
pen.fd(200) 
pen.lt(90) #拐弯
pen.fd(100)

pen.clear()


#用for循环画正方形
for i in range(4):
    pen.fd(100)
    pen.lt(90)



turtle.mainloop()
