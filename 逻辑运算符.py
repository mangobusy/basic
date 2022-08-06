a=0
b=1
c=2
# and:都真才真
print(a<b and c>b)  # 写成 print((a<b) and (c>b)) 结果相同，加括号为了避免歧义。
print(a>b and c>b)

# or:一真则真，都假才假
print(a<b or c>b)
print(a>b or c>b)

# not:取反
print(not False)
print(not a>b)

# 王炸方法：and/or 返回的数取决于 决定真假的那个

# and,只要有一个值为0，则结果为0。否则结果为最后一个非0数字。
print(0 and 1)
print(1 and 2)
print(2 and 1)

# or,只有所有值为0，结果才为0。否则结果为第一个非0数字。
print(0 or 1)
print(0 or 0)
print(3 or 5)