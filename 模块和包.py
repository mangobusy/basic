# 导入模块
# 方法一：import
import math
print(math.sqrt(9))  # >>>3
# 方法二：from 模块名 import 功能1，功能2...
from math import sqrt
print(sqrt(9))   # 写法不一样了
# 方法三：from 模块名 import *
from math import *
print(sqrt(9))

# as定义别名--将来使用时只能使用别名
# 模块定义别名--import 模块名 as 别名
# 功能定义别名--from 模块名 import 功能 as 别名
import time as tt  # 模块定义别名
tt.sleep(2)  # 隔两秒再打印hello
print('hello1')
from time import sleep as sl  # 功能定义别名
sl(2)
print('hello2')

# 制作模块--(1)定义模块--(2)测试模块--(3)调用模块
# (1)定义模块：新建一个python文件，在里面定义函数
# (2)测试模块：if__name__=='__main__':

# 模块定位顺序
# 注意：(1)自己的文件名不要和已有模块名重复，否则模块功能无法使用
#      (2)使用  from 模块名 import功能  时，如果功能名重复，调用到的时最后定义的功能

# __all__
# 当使用 from 模块名 import * 导入时，只能导入__all__列表中的元素（功能）
# 假设这是在我自定义的模块my_module中：
# __all__=['test1']
# def test1():
#     print('test1')
# def test2():
#     print('test2')
# 这是另一个文件导入模块的代码：
# from my_module import *
# test1()   # >>> test1
# test2()   # >>> 报错

# 包——将有联系的模块组织在一起，即放到同一个文件夹下，并且在这个文件夹创建一个名字为__init__.py文件，这个文件夹就是包
# 制作包——右键[New]——[Python Package]——输入包名——[OK]——新建功能模块

# 导入包
# 方法一：import 包名.模块名——调用：包名.模块名.功能
# 方法二：from 包名 import * ——调用：模块名.功能——注意：必须在__init__.py文件中添加__all__=[],控制允许导入的模块列表
