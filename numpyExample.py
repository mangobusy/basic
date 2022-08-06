import numpy as np

# numpy.mean()--求平均值
l=np.array([1,2,3,4,5])
print(np.mean(l))   # 3

# numpy.median()--求中位数
l=np.median([1,2,3,4,5])
print(l)
# 通常我们这样求中位数：
import math
l2=[1,3,5,7,9]
print(l2[math.ceil((len(l2)/2)-1)]) # so麻烦

# numpy.std()--算标准差
l=[1,2,3,4,5]
print(np.std(l))

k = 25
l = [1, 3, 3, 4, 5, 6, 6, 7, 8, 8]
print(np.percentile(l,k))

# import scipy as stats
# # stats.mode()--求众数
# l = [19, 8, 29, 35, 19, 28, 15]
# print(stats.mode(l))