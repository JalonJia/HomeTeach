f = int(input('请输入几到几的乘法口诀:'))
for i in range(f):
    for u in range(i + 1):
        print('%d * %d = %d'%(u + 1, i + 1, (u + 1) * (i + 1)),end = ' ')
    print('')