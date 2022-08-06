# 元组中的数据不能修改,只能查找,元组内数据可以重复，元素的数据类型可以是int/str/bool/及其混合
# 定义多个数据的元组
t1=(10,20,30)
# 定义单数据元组
t2=(10,)  # 单个数据后面也要加个逗号

# 创造一个元组--tuple()
a=tuple(['aa','bb','cc','bb'])
print(a)

# 查找
# 按下标查找
print(a[0])
# .index() 返回元素次序
print(a.index('bb'))
# .count() 统计元素出现次数
print(a.count('bb'))
# len()
print(len(a))

# 修改
# tuple[1]='sss' 会报错
t2=('aa','bb',['cc','dd'])
print(t2[2][0]) #[2]表示元组中第三个数据，[0]表示列表中第一个数据
t2[2][0]='tom'
print(t2)

print('-'*50)
# 打包
a = ('one','two','three')
(szh,zzx,ylw) = a  # (szh,zzx,ylw)是我赋的变量
print(szh)   # >>> one
print(zzx)   # >>> two
print(ylw)   # >>> three
# 若变量数 < 元组中元素数,可添加*在变量前
b = ('one','two','three','four','five')
(szh,zzx,*ylw)=b
print(ylw)    # >>> [three,four,five]
#
def name_get():
    return 'szh','zzx','ylw'
name=name_get()
print(name[0])
#
from collections import namedtuple
def get_name():
    name=namedtuple('name',['first','middle','last'])
    return name('szh','zzx','ylw')
name=get_name()
print(name.middle)

print('-'*50)
# 元组可以与数字相乘
c=('szh','ka')*2
print(c)    # >>> ('szh','ka','szh','ka')