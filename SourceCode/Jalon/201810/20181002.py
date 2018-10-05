
n = int(input('请输入你想知道的数字的乘法口诀:'))

for x in range(n):    
    for i in range(x+1):
        print('%d*%d=%d' % (i+1, x+1, (i+1)*(x+1)), end = ' ')

    print('')    


