name='szh'
age=18
weight=45.5
stu_id=36

print('my name is %s' %name)    # %s 是占位符
print('i am %d years old' %age )
print('my weight is %f' %weight)
# 若文本里出现百分比，要写两个百分号，不然电脑会当作占位符

# %是old fasion way,现在用法：(注意 . 表示调用格式化符号)
print('my name is {}'.format(name))
print('i am {} years old'.format(age))

# %和f之间加.（小数点）和一个数字，表示保留几位小数
print('my weight is %.2f' %weight)

print('my student id is %d' %stu_id)
print('my student id is %03d' %stu_id)  # 3表示学号为三位数，0表示不足的位数用0补齐。超出的原样输出。

print('my name is %s,i am %d years old '%(name,age))

print('my name is %s,i am %d years old,my weight is %.2f,my student id is %03d' %(name,age,weight,stu_id))

 # %s也可以代替%d和%f
print('my name is %s,i am %s years old' %(name,age))

# f格式化字符串 语法 f'{表达式}‘  (python3.6中新增了f格式化字符串)
print(f'my name is {name},i am {age} years old' )

name='zby'
print(f'my name is {name},i am a 巨佬')