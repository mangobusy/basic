#查找
namelist=['tom','jim','peter']
print(namelist)
print(namelist[0]) # 0代表列表中的第一个

# 查找函数
# index() 返回元素在列表中的顺次
print(namelist.index('jim'))
# count()  返回元素在列表中的个数
print(namelist.count('jim'))
# len()  返回列表元素总个数
print(len(namelist))

# 判断是否存在(in和not in)
print('tom' in namelist) # print括号里没有引号
print('tom' not in namelist)

namelist2=['tom','jim','peter']
name=input('please input your name')
if name in namelist2:
    print(f'there was already a {name}，please input again.')
else:
    print('great name!')

# 增加列表元素
# append (列表结尾增加；若增加的是列表，则将该列表直接增加到原列表）
namelist2=['tom','jim','peter']    # 列表是 可变类型 的
namelist2.append('szh')
print(namelist2)
namelist2.append([1,2])  # 追加一个列表也可
print(namelist2)
# extend (列表结尾增加；若增加的是列表/字符串，则将该列表/字符串 拆开 补到原列表中）
namelist2=['tom','jim','peter']
namelist2.extend('szh')
print(namelist2)
namelist2.extend([1,2])
print(namelist2)
# insert(指定位置新增数据）
namelist2=['tom','jim','peter']
namelist2.insert(1,'szh')
print(namelist2)

# 删除
# del
namelist2=['tom','jim','peter']
# del namelist2  #也可以写 del(namelist2),也可以指定一个元素如 del namelist2[1]
del namelist2[0]
print(namelist2)
# pop()删除指定下标数据，若不指定则默认删除最后一个。但无论如何pop都会返回被删除数据
a=namelist2.pop(1)
print(a)
# remove(数据)
namelist2.remove('peter')  # 注意 . 和’‘
print(namelist2)
# clear清空列表
namelist2.clear()
print(namelist2)

# 改变元素
namelist2=['tom','jim','peter']
namelist2[1]='zby'  # 注意有’‘
print(namelist2)
namelist2[0:2]=['szh','zzx'] #更改0，1号元素
print(namelist2)

# 逆序 reverse()
list3=[1,2,3,6,9,4]
list3.reverse()  # 注意：不是按数字大小逆序，是按原列表顺序来逆序
print(list3)
# sort() 排序：升序（默认）和降序--按首字母排序(1)，数字默认按从小到大排序(2)
list3.sort()
print(list3)
list3.sort(reverse=True) # reverse=True降序； reverse=False升序--
print(list3)

# 列表复制 .copy()
namelist2=['tom','jim','peter']
list4=namelist2.copy()
print(list4)
print(namelist2)

# while遍历
i=0
namelist2=['tom','jim','peter']
while i<len(namelist2):
    print(namelist2[i])
    i+=1

# for遍历
namelist2=['tom','jim','peter']
for i in namelist2:
    print(i)

# 列表嵌套
namelist3=[['小明','小红','小兰'],['tom','jim','petter'],['张三','李四','王五']]
print(namelist3[0][1])  # 第一个中括号代表子列表，第二个中括号代表子列表中的元素

# 分配办公室
import random
teachers=['a','b','c','d','e','f','g','h']
offices=[[],[],[]]
for name in teachers:
    num=random.randint(0,2)
    offices[num].append(name)
print(offices)
i=1
for office in offices:
    print(f'办公室{i}的人数是{len(office)}')
    for name in office:
        print(name)
    i+=1

name=list(('小明','小红','小兰'))
print(name)

namelist3=['小明','小红','小兰']
print(namelist3[0:2])  #左闭右开，表示取 0，1 两个元素
print(namelist3[:2])  #表示取从起始元素到1
print(namelist3[1:])  #表示取从1到最后一个元素

namelist3=['小明','小红','小兰']
[print(a) for a in namelist3]

numList = [x for x in range(1, 11) if x % 2 == 0]
print(numList)

