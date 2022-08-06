# 定义函数
def hhhh():
    print('szh is a shauige')
# 调用函数
hhhh()


def s_func():
    print('显示余额')
    print('存款')
    print('取款')

print('恭喜您登录成功')
s_func()
print('您的月余额是10000')
s_func()
print('取款成功')
s_func()

# 返回值
def sum_num(a,b): #定义函数
    return a+b
result=sum_num(1,2) #调用函数，输入两个实参，
print(result)

def tri(a):
    S=1/2*a*h
    return(S)
a=int(input('please input a length'))
h=int(input('please input a heigh'))
b=tri(a)
print(b)

# 函数嵌套
def testA():
    print('A1')
    print('Aover')
def testB():
    print('B1')
    testA()
    print('Bover')
testB()

# 函数的说明文档
print('*'*50)
def sum(a,b):
    '''求和函数'''
    return a+b
help(sum)

# 函数嵌套———打印图形
def print_lines():
    print('-'*10)
def print_lines2(num):
    i=0
    while i<=num:
        print_lines()
        i+=1
print_lines2(4)

# 函数嵌套————求和
def sum(a,b,c):
    return a+b+c
def average_sum(a,b,c):
    result=sum(a,b,c)
    return result/3
averageResult=average_sum(1,2,3)
print(averageResult)

# 修改全局变量
a=100
def testC():
    print(a)
def testD():
    a=200  # 只修改了局部变量
    print(a)
testC()
testD()
print(a)
def testE():
    global a # global声明a是全局变量
    a=300
    print(a)
testE() # 修改变量的函数要执行，全局变量才会改
print(a)

# *args和**kwargs--当参数数量未知时
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

total = my_sum(1, 2, 3, 5, 7)