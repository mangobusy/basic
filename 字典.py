# 3.7版本字典是有序的; 3.6及以前的版本字典是无序的，不能用index
# 字典：符号为大括号；数据以键值对的形式出现；用逗号隔开
dic1={'name':'tom','age':'20','gender':'female'}
print(len(dic1))

#新增数据
dic1={'name':'tom','age':'20','gender':'female'}
dic1['id']=110  #若key不存在，则新增
print(dic1)
dic1['name']='rose'  #若key存在，则修改
print(dic1)
# setdefault(key,value)--用于新增键值对
# setdefault(key,[]).append(value)--
s={}
print(s.setdefault('name',[]).append('szh'))  # >>>{'name':['szh']}

# 删除
# del 删除指定的键值对
dic1={'name':'tom','age':'20','gender':'female'}
# del dic1 # 也可以写成 del(dic1)
del dic1['name']
# clear 清空字典
dic1.clear()
# popitem() 删除并返回最后一个数据(python3.7)
dic1={'name':'tom','age':'20','gender':'female'}
print(dic1.popitem())
# pop(key)  删除指定数据

# 修改(key存在 则修改，key不存在则新增)
dic1={'name':'tom','age':'20','gender':'female'}
dic1['name']='lily'
print(dic1)
dic1['id']='hhh'
print(dic1)
# update()
dic1.update({'school':'SCNU'})
print(dic1)

# 查找
# key值查找
print('*'*55)
dic1={'name':'tom','age':'20','gender':'female'}
print(dic1['name'])   # 返回对应的value
# 函数查找
# get()  get(key,默认值)若查找当前key不存在则返回默认值，若无默认值则返回None
dic1={'name':'tom','age':'20','gender':'female'}
print(dic1.get('name'))   # 返回对应的value
print(dic1.get('id',110))
print(dic1.get('id'))
# keys()
dic1={'name':'tom','age':'20','gender':'female'}
print(dic1.keys()) #返回了可迭代对象
# values()
dic1={'name':'tom','age':'20','gender':'female'}
print(dic1.values()) #返回了可迭代对象
# items()  返回元组为元素的列表[(key1,value1),(key2,value2)]
dic1={'name':'tom','age':'20','gender':'female'}
print(dic1.items())

# copy() 复制字典
aaa={'abc':'adc','123':'456'}
bbb=aaa.copy()
print(bbb)
# 如果直接让aaa=bbb(两字典相对)，那么改变一个字典，另一个也会变，其实这两个字典是一个东西
# dict() 也可用来复制字典
ccc=dict(aaa)
print(ccc)

# 遍历key
dic1={'name':'tom','age':'20','gender':'female'}
for key in dic1:  # 也可以写成 for key in dic1.keys():
    print(key)
# 遍历value
dic1={'name':'tom','age':'20','gender':'female'}
for value in dic1.values():
    print(value)
# 遍历items--返回键值对的元组
dic1={'name':'tom','age':'20','gender':'female'}
for item in dic1.items():
    print(item)
# 遍历键值对
dic1={'name':'tom','age':'20','gender':'female'}
for key,value in dic1.items():
    print(key)
    print(value)
for key,value in dic1.items():
    print(f'{key}={value}')

x={i:str(i+3) for i in range(5)}
print(x)
print(x.items())
print(sum(item[0] for item in x.items()))