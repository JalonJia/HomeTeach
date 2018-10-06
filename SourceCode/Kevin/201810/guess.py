import random
jkl = random.randint(1,100)
print('猜猜我爸爸的岁数，是在1—100之间的数,一共有六次机会：')
for i in range(6):
    iop = int(input())
    if iop == jkl:
        print('你猜对了!')
        quit()
    if iop < jkl:
        print('你猜的数小了。')
    if iop > jkl:
        print('你猜的数大了。')
print('你输了。')
