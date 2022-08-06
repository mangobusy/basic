# 用’类‘去创建一个’对象‘， 一个“类”可创建多个对象
# 定义类-->创建对象-->调用

# 面对对象三大特征
# 一：封装
#    将属性和方法书写到类里面的操作即为封装
#    封装可以为属性添加私有权限
# 二：继承
#    子类默认继承父类的所有属性和方法
#    子类可以重写父类属性和方法
# 三：多态
#    传入不同的对象，产生不同的结果

'''class Washer():  # 类名要符合大驼峰命名习惯
    def wash(self):  # self是调用函数的对象
        print('能洗衣服')
haier=Washer()   # 对象名=类名()
haier.wash()   # 调用--实例方法--对象名.函数名()
print(haier)  # 打印内存地址

haier.height=100  # 给对象添加属性--对象名.属性名=值
print(f'the height is {haier.height}')  # "类"外面获取属性



class Washer():  # 类名要符合大驼峰命名习惯
    def wash2(self):  # self是调用函数的对象
        print(f'the height is {self.height}')  # "类"里面获取对象属性 self.属性
haier=Washer()
haier.height=300
haier.wash2()

# 魔法方法1：__init__()--设置初始化对象--默认被调用
class Washer2():
    def __init__(self):
        self.height=400
    def wash3(self):
        print(f'the height is {self.height}')
haier=Washer2()
haier.wash3()'''

class Washer2():
    def __init__(self,height):   # 带参数的init
        self.height=height
    def wash3(self):
        print(f'the height is {self.height}')
haier=Washer2(80)
haier.wash3()
haier.height=90   # 通过对象修改数据，但改不了类的属性
print(haier.wash3())
del haier.height  # 删除数据


# __str__ --当print(对象)时，默认打印内存地址。若定义了 __str__ ，那么就会打印return的数据
'''class Washer3():
    def __init__(self):
        self.height=900
    def __str__(self):
        return '哈哈哈哈'
haier=Washer3()
print(haier)

# __del__删除，默认被调用
class Washer4():
    def __init__(self):
        self.height=700
    def __del__(self):
        print('已经被删除')
haier=Washer4()


class SweetPotato:
    def __init__(self):
        self.cook_time=0
        self.cook_state='生的'
        # self.condiments=[]  添加调料用列表
    def cook(self,time):
        self.cook_time+=time
        if 0<self.cook_time<5:
            self.cook_state = '生的'
        if 5<=self.cook_time<=9:
            self.cook_state = '差不多熟了'
    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟,状态是{self.cook_state}'
a=SweetPotato()
a.cook(1)
print(a)  # 地瓜烤了1分钟，状态是生的
a.cook(4)
print(a)   # 地瓜烤了5分钟，状态是差不多熟了


class Furniture():
    def __init__(self,name,area):
        self.name=name
        self.area=area
    # def __str__(self):
    #     return f'家具是{self.name},占地面积{self.fur_area}'

class Home():
    def __init__(self,area):
        self.free_area=area
        self.furniture=[]
    def fur_contain(self,item):
        if item.area<=self.free_area:
            self.furniture.append(item.name)
            self.free_area = self.free_area - item.area
        else:
            print('家具太大，无法容纳')

    def __str__(self):
        return f'家剩余的面积是{self.free_area}，家具有{self.furniture}'

bed=Furniture('床',4)
house1=Home(150)
print(house1)
house1.fur_contain(bed)  # 相当与把bed赋到item
print(house1)


#经典类--class 类名:
#新式类--class 类名(object):

# 单继承--一个子类继承一个夫类
# class 夫类(object):
#   balabala
# class 子类(夫类):
#   pass
# a=子类
# print(a)'''
class Polygon:
    def __init__(self, n_sides):
        self.n_sides = n_sides
        # self.l_sides = [0 for i in range(n_sides)]
    def setSideLength(self):
        self.l_sides = [float(input("Enter length of side "+str(i+1)+" : "))  for i in range(self.n_sides)]
        print(self.l_sides)
    def viewSides(self):
        for i in range(self.n_sides):
            print("Side", i+1, "is",self.l_sides[i])
class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,4)
s = Square()
s.setSideLength()
s.viewSides()
# 也可用super()
class Square(Polygon):
    def __init__(self):
        super().__init__(4)
s = Square()
s.setSideLength()
s.viewSides()
print(isinstance(s,Square))  # isinstance()
# 多继承--一个子类继承多个夫类--当有多个父类时，默认使用第一个父类的同名属性和方法
# class 夫类1(object):
#   balabala1
# class 夫类2(object):
#   balabala2
# class 子类(夫类1,夫类2):  # 以这里的顺序为主
#   pass
# a=子类
# print(a)

# 子类重写父类同名方法和属性--当子类有和父类同名的属性和方法，子类调用时，调用的是子类的属性和方法

# 多层继承

# 查看继承关系.__mro__

# print(类名.__mro__)

# super()--调用父类方法
# 方法一：super(当前类名，self).函数()
#    super(prentice, self).__init__()
#    super(prentice,self).make_cake()
# 方法二：super().函数()
#    super().__init__()
#    super().make_cake()

# 定义私有属性和方法--在属性名和方法名前加两个下划线__

'''class Dog(object):
    def work(self):
        pass
class AD(Dog):
    def work(self):
        print('AD work')
class DD(Dog):
    def work(self):
        print('DD work')
class People():
    def work_with(self,dog):
        dog.work()
ad=AD()
dd=DD()
szh=People()
szh.work_with(ad)'''