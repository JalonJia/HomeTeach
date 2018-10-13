#Guess.py -- 猜数字

import random

number = random.randint(1, 50) #产生一个1到50之间的随机整数
#变量 赋值运算符= 函数调用的返回值
#一盘饺子 = 妈妈.做饺子(饺子皮，饺子馅，火，水，勺子，锅，盘子)


#print(number)

print('猜数字，猜一个1到50之间的数字，如果6次以内你猜对了，你就赢了；否则，你就输了')

for i in range(6): #for循环，i:自增变量，range(6):迭代器
    print(f'第几次循环：{i}')
    get_enter = input('请输入你猜测的数字：')
    if get_enter.isdigit() : #判断输入的是不是数字
        guess = int(get_enter) #将参数转换成数字
    else:
        print('你输入的不是一个数字，请重新输入')        
        continue
        
    if guess == number: #猜对的情况
        print('恭喜你，你猜对了！')
        break
    elif guess > number:  #猜错的情况，其实有两种：猜的数比答案大或者比答案小,这是第一种
        if i == 5:
            print(f'很抱歉，你没有猜出来，你输了！答案是：{number}')
        else:
            print('你猜的数字大了，继续猜吧！')
    else:
        if i == 5:
            print(f'很抱歉，你没有猜出来，你输了！答案是：{number}')
        else:
            print('你猜的数字小了，继续猜吧！')
        
        
