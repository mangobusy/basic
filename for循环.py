str='zbyNB'
for i in str:
    print(i)

str='zbyNB'
for i in str:
    if i=='y':
        break
    print(i)
else:
    print('hhh')

str='zbyNB'
for i in str:
    if i=='y':
        continue
    print(i)
else:
    print('hhh')


i=0
for i in range(0,5):
    print(i)

list=[1,23,4]
for i in list:
    print(i)

list=['A','B','C']
for i in list:
    print(i)

list=['A','B','C']
list_iter=iter(list)
print(next(list_iter))

list=['a','b','c']
for i in list:
    j=1
    while j<=5:
        print(i,end='')
        j+=1
    print('')

h=1
list=['a','b','c']
for i in list:
    j=1
    while j<=h:
        print(i,end='')
        j+=1
    print('')
    h+=1

i=1
while i<=5:
    for m in range(0,i):
        print(i,end='')
    print('')
    i+=1

j=1
list22=['a','b','c']
for i in list22:
    j = 1
    while j<=5:
        print(i,end='')
        j+=1
    print('')

