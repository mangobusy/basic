# 创建集合用{}或()，但创建空集合不能用{}。
# 集合不能用下标
# 集合中的数据不能重复(集合有去重的功能)
# 转换为集合用set()

s1={10,20}
# 增加数据
# add() 增加单一数据,不能追加数据序列（eg.列表）
s1.add(100)
print(s1)
# update() 增加的是数据序列，但会将序列拆开装进集合
s1.update([10,20,30,40])
print(s1)

print('-'*50)
s2={10,20,40,60,70}
# 删除
# remove(数据) 删除指定数据(若数据不存在则报错)
s2.remove(10)
print(s2)
# discard(数据) 删除指定数据(若数据不存在不会报错)
s2.discard(20)
print(s2)
# pop() 随机 删除某个数据，并返回某个数据
del_num=s2.pop()
print(del_num)
print(s2)

print('-'*50)
s2={10,20,40,60,70}
# 查找数据
# 用in和not in来判断数据是否在集合中
print(20 in s2)     # >>> True

print('-'*50)
# 求并集--union()------------------------------
a={1,2,3}
b={'x','y','z'}
c=a.union(b)
print(c)
# 求并集----------------------------------------
# intersection_update()--改变了原集合
c={'ggg','hhh','szh'}
d={'jjj','uuu','szh'}
c.intersection_update(d)
print(c)
# intersection()--创建了一个新集合
c={'ggg','hhh','zzx'}
d={'jjj','uuu','zzx'}
e=c.intersection(d)
print(e)
# 求集合不共同拥有的元素-----------------------------
# symmetric_difference_update()--改变了原集合
c={'ggg','hhh','szh'}
d={'jjj','uuu','szh'}
c.symmetric_difference_update(d)
print(c)
# symmetric_difference()--创建了一个新集合
c={'aaa','sss','zzx'}
d={'rrr','www','zzx'}
e=c.symmetric_difference(d)
print(e)