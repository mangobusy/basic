'''list=[]
num=int(input('please input a number'))
while num!=0:
    list.append(num)
    print(list)
    num =int( input('please input a number'))
list.sort()
print(list)'''

'''list2=[]
num2=input('please input some numbers')
for number in num2:
    if (number!='0'):
        list2.append(number)
    else:
        break
list2.reverse()
print(list2)'''

##从用户读取整数，并将他们储存在一个列表中。使用0作为标记值来标记输入的结束。
# 一旦所有值都被读取，程序应以相反的顺序来显示他们。
'''list2=[]
num2=int(input('please input some numbers'))
while num2!=0:
    list2.append(num2)
    print(list2)
    num2 =int(input('please input some numbers'))
list2.reverse()
print(list2)'''


## 编写一个函数，从用户那里读取一个数字列表，从该列表中删除最大的那个数。
'''def main():
    pre_list=input('please input some number')
    list1=list(pre_list)
    print(list1)

    for i in range(len(list1)):
        while list1[i]>list1[i+1]:
            del list1[i]
            i+=1
    return list1
main()'''

## 避免重复：程序从用户读取单词，直到用户输入空行
'''words=[]
word=input('please input some words')
for i in word:
    if i !=' ':
        if i not in words:
            words.append(i)

print(words )'''

list1=[]
number=input('please input some numbers')
while number!=' ':
    number_int=int(number)
    list1.append(number_int)
    print(list1)
    number = input('please input some numbers')






