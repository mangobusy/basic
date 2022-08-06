# 语法
# if 条件：
#     条件成立执行代码1 （前面4个空格，或一个Tab键）
#     条件成立执行代码2
#      ......
age=23
if age>=18:
    print('已经成年，可以上网')

age=int(input('what is your age')) #注意加 int （注意数据类型）
if age>=18:
    print(f'you are {age} years old,you can go to the 网吧')

# if...else...语法
# if 条件：
#     条件成立执行1
# else：
#     条件不成立执行2

age=int(input('what is your age')) #注意加 int （注意数据类型）
if age>=18:
    print(f'you are {age} years old,you can go to the 网吧')
else:
    print(f'you are not old enough,you should go home and do your homework')

# 多重判断
age=int(input('please input your age'))  # 注意int
if age<18:
    print('you are not old enough,you are 童工,it is illegal ')
elif (age>=18) and (age<=60):  #也可以写成 18<=age<=60
    print('you can work')
elif age>=60:
    print('you are too old,you can not work')

# if嵌套
money=1
seat=1
if money==1:
    print('you can get into the car')
    if seat==1:
        print('you can sit')
    else:
        print('please stand')
else:
    print('you can not get into the car')

# 猜拳游戏
player=int(input('请出拳：0--石头，1--剪刀，2--布'))
compu=1
if ((player==0)and(compu==1))or((player==1)and(compu==2))or ((player==2)and(compu==0)): #注意==
    print('player win')
elif (player==1):
    print('平局')
else:
    print('computer win')
# 猜拳游戏之随机数（使用模块）
# 导入（随机）模块 --import
import random
compu=random.randint(0,2)


player=int(input('请出拳：0--石头，1--剪刀，2--布'))

if ((player==0)and(compu==1))or((player==1)and(compu==2))or ((player==2)and(compu==0)): #注意==
    print('player win')
elif ((player==1)and(compu==1))or ((player==1)and(compu==1))or((player==1)and(compu==1)):
    print('平局')
else:
    print('computer win')

# 三目运算符
# 条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
a=1
b=2
c=a if a>b else b
print(c)



