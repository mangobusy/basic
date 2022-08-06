i=1 #一般电脑都从0开始
while i<=5:
    print('我爱学习')
    i=i+1
print('你真是个好孩子')

i=1
result=0
while i<=100:
    result+=i
    i+=1
print(result)

i=1
result=1
while i<=3:
    result=result*2
    i+=1
print(result)

# 1--100的偶数相加
i=0    #i+=2
result=0
while i<=100:
    result+=i
    i+=2
print(result)

i=0    #i和2相处余数为0
result=0
while i<=100:
    if i%2==0:
        result+=i
    i+=1
print(result)

# break终止整个循环；
i=1
while i<=5:
    if i==4:
        print('吃饱了，不吃了')
        break
    print(f'吃了{i}个苹果')
    i+=1

# continue退出当前一次循环，执行下一次循环代码
i=1
while i<=5:
    if i==3:
        print('吃出一个大虫子，这个苹果不吃了')
        i+=1
        continue
    print(f'吃了{i}个苹果')
    i+=1
print('*'*55)
i=0
j=0
while i<2:
    print(i,'outer')
    while j<2:
        print(j,'inner')
        j+=1
        break
    i+=1
print('&'*70)
i=0
j=0
while i<2:
    print(i,'outer')
    while j<2:
        print(j,'inner')
        j+=1
        continue
        print('hhh')
    i+=1


i=0
j=0
while i<2:
    print(i,'outer')
    while j<2:
        print(j,'inner')
        j+=1

    i+=1

i=0
while i<5:
    i+=1
    if not i%2:
        continue
    print(i)

n=1
while n<=5:
    for m in range (0,n):
        print(n,end='')
    n+=1
    print('')

# while循环嵌套
i=1
j=1
while i<=3:
    while j<=3:
        print('对不起我错了')
        j+=1

    print('晚上刷碗')
    print(f'刷了{i}天碗')
    i+=1

j=1
while j<=5:
    i=0
    while i<=5:
        print('*',end='')
        i+=1
    print('')
    j+=1

j=1
while j<=5:
    i = 1
    while i<=j:
        print('*',end='')
        i+=1
    print('')
    j+=1

# 九九乘法表
j=1
while j<=9:
    i=1
    while i<=j:
        print(f'{i}*{j}={i*j}',end='\t') # \t对齐制表
        i+=1
    print('')
    j+=1

i=1
while i<=5:
    if i==3:
         break   # 不执行else
    print('ZBYNB')
    i+=1
else:
    print('我的天哪')

i=1
while i<=5:
    if i==3:
        i+=1
        continue
    print('ZBYNB')
    i+=1
else:
    print('我的天哪')

i=0
namelist2=['tom','jim','peter']
while i<len(namelist2):
    print(namelist2[i])
    i+=1