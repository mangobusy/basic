# 1. 打开 open('名字'，‘操作’)
f=open('text.txt','w')
# 2. 读写操作 write()  read()
# write()--只能写字符串，其他数据类型都要转化成字符串
f.write('hahaha')
# 3. 关闭 close()
f.close()
# 其他关闭方法--自动关闭
with open("jpsFolder/somefile.txt","r") as f:
    for line in f:
        print (line, end="")
# 其他关闭方法--用try和finally
f = open("jpsFolder/somefile.txt","r")
try:
    l = list(f)
    for line in l:
        print(line, end="")
except: # balabala:
    pass
finally:
    f.close()

# 主访问模式
# r: 如果文件不存在，报错：不支持写入，只读（文件指针在开头）
# f=open('text1','r')
# f.close()  报错

# w: 如果文件不存在，新建文件：执行写入，会覆盖原有内容 （文件指针在开头）
# f=open('text2','w')
# f.write('aaa')  会自动新建一个text2文件夹，里面有内容‘aaa’   # write()只接受str
# f.close()

# a: 如果文件不存在，新建文件:在原有内容基础上，追加新内容 （文件指针在结尾）
# f=open('text3','a')
# f.close()

# 带b的(rb/wb/ab/rb+/wb+/ab+): 都是以二进制打开文件
# 带+号的(r+/w+/a+/rb+/wb+): 都是可读可写
# r/w相关的访问模式指针都在开头
# a相关的访问模式指针都在结尾

# 访问模式可以省略，如果省略表示访问模式为r

f=open('text2','w') # 创建新文件
f.write('aaa')
# read() 读取文件中的内容
f=open('text2','r')
print(f.read())  # read()括号中可有可无，有的话表示读取的字节数量  换行符\n占一个字节
f.close()

# readlines() 按照‘行’的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
f=open('text2')
con=f.readlines()
print(con)
f.close()

# readline() 一次读取一行的内容，第一次调用--读取第一行，第二次调用--读取第二行
f=open('text2')
con=f.readline()
print(con)
f.close()

# seek() 用来移动文件指针--文件对象.seek(偏移量，起始位置)--起始位置：0开头，1当前，2结尾
# tell()--返回整数，告诉你现在的指针位置
with open("text.txt","a+") as f:
    print(f.tell())   # 返回16--在文件尾

# 备份--格式：原文件名+【备份】+后缀--找后缀可用find()/rfind()
#           找原文件名--切片【开始位置:结束位置:步长】
# 备份文件写入数据:打开原文件和备份文件--原文件读取，备份文件写入--关闭文件

old_name=input('请输入要备份的文件名')
index=old_name.rfind('.')

if index>0:  # 要确保原文件名是有效的
    postfix=old_name[index:]

new_name=old_name[:index]+'备份'+old_name[index:]  # 备份文件命名ing
print(new_name)

old_f=open(old_name,'rb')
new_f=open(new_name,'wb')

while True:  # 这是因为不确定文件大小
    con=old_f.read(100) # 一次从原文件中读取的字符数
    if len(con)==0:  # 如果读取到字符串数为0--即为已经读到最后了
        break  # 停止读取
    new_f.write(con)   
old_f.close
new_f.close

'''
# 文件操作函数--导入模块os，使用模块内功能--import os
# 1. 重命名--os.rename('旧名'，'新名')
# 2. 删除文件--os.remove(文件名)--(只有在文件夹是空的时才能删文件夹)
# --创建文件夹--os.mkdir(文件夹名)
# --删除文件夹--os.rmdir(文件夹名)
# --获取当前目录--os.getcwd()--print(os.getcwd)
# --改变默认目录--os.chdir(目录)
# --获取目录列表--os.listdir(目录)--print(os.listdir)
'''
'''
# shutil module--shell utilities--文件和文件夹的高级操作，是对os模块的补充--import shutil
# 1.复制文件--shutil.copy(源文件,目标地址)--返回复制之后的路径
# 2.复制文件和状态信息--shutil.copy2(源文件,目标地址)--返回复制之后的路径
# 3.复制文件夹(及一个文件夹下所有文件)--shutil.copytree(源,目标)
# 4.移动文件或文件夹--shutil.move(原,目标)
# 5.删除文件--rmtree()
'''
import os, shutil                     #import statements
print(os.getcwd())                    #show the current directory
os.chdir("dir1")                      #change directory
with open("copyme.txt","w") as f:     #create the file
    f.write("Going to copy this file")    #Write a string for fun
src = os.getcwd()+"/copyme.txt"       #set source of the file to copy
dest = "../dir2"                      #set the destination
shutil.copy(src,dest)                 #copy the file from src to dest
os.chdir(dest)                        #change to the dest directory
print(os.listdir())                   #print list of the contents of dest


# 使用remove前，可以先检查一下文件存不存在
import os
if os.path.exists("text.txt"):
    os.remove("text.txt")
else:
    print("File doesn't exist")
# ls?
