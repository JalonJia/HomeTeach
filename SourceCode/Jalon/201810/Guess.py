#Guess.py -- 猜数字

import random

number = random.randint(1, 10) #产生一个1到10之间的随机整数

#print(number)

print('猜数字，猜一个1到10之间的数字，如果6次以内你猜对了，你就赢了；否则，你就输了')
guess = int(input('请输入你猜测的数字：'))
if guess == number :
    print('恭喜你，你猜对了！')
    quit()
else:
    print('就差一点点了，继续猜吧！')
    
guess = int(input('请输入你猜测的数字'))
if guess == number :
    print('恭喜你，你猜对了！')
    quit()
else:
    print('就差一点点了，继续猜吧！')

guess = int(input('请输入你猜测的数字'))
if guess == number :
    print('恭喜你，你猜对了！')
    quit()
else:
    print('就差一点点了，继续猜吧！')

guess = int(input('请输入你猜测的数字'))
if guess == number :
    print('恭喜你，你猜对了！')
    quit()
else:
    print('就差一点点了，继续猜吧！')

guess = int(input('请输入你猜测的数字'))
if guess == number :
    print('恭喜你，你猜对了！')
    quit()
else:
    print('就差一点点了，继续猜吧！')

guess = int(input('请输入你猜测的数字'))
if guess == number :
    print('恭喜你，你猜对了！')
    quit()
else:
    print('就差一点点了，继续猜吧！')
