g = 0
w = 1
q = 1
print('猜数字在1—100里面,猜对才结束')
import random
jkl = random.randint(1,100)
while q == w:
    iop = input()
    while q == w:
            if not iop.isdigit():
                print('你输入的不是数字请重新输入')
                iop = input()
                g += 1
            else:
                g += 1
                break
    if int(iop) == jkl:
        print(f'你猜对了!,你一共猜了{g}次')
        break
    if int(iop) < jkl:
        print('你猜的数小了。')
        print('你应该猜大')
    if int(iop) > jkl:
        print('你猜的数大了。')
        print('你应该猜小')
