# 递归的特点：time--O(n)
# 函数内部自己调用自己
# 必须要有出口
def sum_numbers(num):    # 从num以此累加到1
    # 出口
    if num==1:
        return 1
    return num+sum_numbers(num-1)
print(sum_numbers(5))

def factorial(n):
    print(f"factorial() called with {n}")
    if n == 0 or n == 1:
        return 1
    else:
        returned = n * factorial(n - 1)   # 累乘
        print(f"factorial({n}) returns {returned}")
        return returned
print(factorial(4))

# 计算列表里有多少元素，但是列表里还嵌套有列表时，用递归
students = ["Emelia",["Jim",["Violet","Bob",],"Kara","Alex"],"Nia",["Ivan","Sarah"],"Bill"]

def leaf_count(aList):
    count = 0
    for item in aList:
        if isinstance(item, list):  # 判断，如果是列表的话。。。
            count += leaf_count(item)
    else:
        count +=1
    return count
print(leaf_count(students))
# lambda（匿名函数）: 如果函数有一个返回值，并且只有一句代码，可以使用lambda简化
# 语法： lambda 参数列表 ： 表达式  （参数列表可有可无；表达式可接受任何数量的参数，但只能返回一个表达式的值）
'''例1'''
def func1():
    return 100
print(func1())
# 用lambda来表示：(无参数的情况)
func2=lambda:100
print(func2)   # 返回的是内存地址
print(func2())   # 返回的是100
'''例2'''
def sum(a,b):
    return a+b
print(sum(1,2))
# 用lambda来表示：
sum2=lambda a,b:a+b
print(sum2(6,2))

# 一个参数
func3=lambda a:a
print(func3('一个参数'))
# 默认参数(缺省参数)
func4=lambda a,b,c=100:a+b+c  # c=100是默认的，如果没有调用时赋值则还是100，若重新赋值则覆盖默认值
print(func4(20,30))
# 可变参数：*args---返回元组
func5=lambda *args:args
print(func5(10,20,30))
# 可变参数：*kwargs---返回字典
func6=lambda **kwargs:kwargs
print(func6(age='18',name='szh'))
# 带判断的lambda
func7=lambda a,b:a if a>b else b
print(func7(100,20))

# 列表数据排序--sort(key=lambda...,reverse=bool)
students=[{'name':'Tom','age':'18'},{'name':'Rose','age':'22'},{'name':'Jack','age':'19'}]
students.sort(key=lambda x:x['name'])  # 对name值进行排序
print(students) # 验证——因为列表顺序可变，所以直接print列表就可以了
students.sort(key=lambda x:x['age'])   # 对age值进行排序
print(students)

# Reversing an Array
def reverse(S,start,stop):
    if start<stop-1:
        S[start],S[stop-1]=S[stop-1],S[start]
        reverse(S,start+1,stop-1)

# 求指数
def power(x,n):
    if n==0:
        return 1
    else:
        partial=power(x,n//2)
        result=partial*partial
        if n%2==1:
            result *=x
        return result