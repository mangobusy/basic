# 开平方--import math--math.sqrt()
import math
print(math.sqrt(9))  # >>>3
# -------------------------------------------------
# 随机取--import random--random.randint(,)
import random
print(random.randint(1,5))  # 在一到五随机取数字
# -------------------------------------------------
isinstance(object,type) # object:表示的是需要判断的对象； # type:表示需要判断的类型
# 若object是这个type，就会返回true；反之false

issubclass(class1, class2)
# 若class1是class2的子类，则返回true; 反之false
# -------------------------------------------------
# + : 合并--可用于字符串、列表、元组
# * : 复制--可用于字符串、列表、元组; 集合、字典不行
print([2]+[3])   # >>> [2,3]
print('2'+'3')   # >>> 23
print((2,)+(3,))  # >>> (2,3)
# -------------------------------------------------
# 取最大值/最小值--max()/min()--英文字母按字母顺序
str='szhissobeautiful'
list=[1,7,2,9,4,6]
print(min(str))
print(max(list))
# -------------------------------------------------
# range(start,end,step步长)
for i in range(0,10,2):
    print(i)
# -------------------------------------------------
# enumerate()枚举--返回(元素顺序，元素,start=num)--start 后面的数字表示打印时‘元素顺序’从num开始，默认为0
seasons = ['spring','summer','autumn','winter']
for i in enumerate(seasons,start=1):
    print(i)
# -------------------------------------------------
# tuple()--将某个序列转换成元组
# list()--将某个序列转换成列表
# set()--将某个序列转换成集合--集合有去重功能
# -------------------------------------------------
# math.ceil()--返回数字的上入整数
a=[1,2,3,4,5]
mid=math.ceil((len(a)/2)-1)
print(a[mid])  # 返回中位数
# -------------------------------------------------
# 用try--except语句测试你的代码，减少报错
try:
    print(a)  # 若你的代码中有a,就打印a
except:  # 若没有a，就执行下面的语句
    print("you didn't initialise a")
    a = input("set a please:")
else:
    pass
finally:
    pass
# --------------------------------------------------
# 切片--可用于字符串、列表、元组--语法：序列[开始位置下标:结束位置下标:步长]--开始位置下标、结束位置下标（左闭右开）
str1='abcdefghij'
print(str1[2:5:1])
print(str1[::-1])  # 倒叙
# --------------------------------------------------
elem=[1,2,3]
elem1,elem2,elem3=elem
print(elem1)

a, *middle, c = [1, 2, 3, 4]   # >>> a=1; *middle=2,3; c=4
# --------------------------------------------------
# 用join()来将list/tuple变成str
li=['z','b','y','泰','剧','啦']
print(''.join(li))
# --------------------------------------------------
# 交换两个元素的值时，用：
a=1
b=2
a,b=b,a
# --------------------------------------------------
# lambda函数
# 语法： lambda 参数列表：参数表达式
mul=lambda x, y: x*y
print(mul(6,2))  # >>>12
# --------------------------------------------------
# setdefault()方法用于设置key的默认值。
# 该方法接收两个参数，第1个参数表示key，第2个参数表示默认值。
# 如果key在字典中不存在，那么setdefault方法会向字典中添加这个key，并用第2个参数作为key的值。
dic={}
dic.setdefault("zby","泰剧啦")
print(dic)   # >>> {'zby': '泰剧啦'}
# --------------------------------------------------
# a.capitalize()来大写首字母，a是要大写的对象字符串
b='asddfgh'
print(b.capitalize())   # >>> Asddfgh
# --------------------------------------------------
# a.split()遇到空格，把a中的字符串分开,返回一个列表
a='zby tai ju la'
print(a.split())   # >>> ['zby', 'tai', 'ju', 'la']