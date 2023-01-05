from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0,20,1000)  # 确定定义域为0~20， 总共插值为1000个点

interval1 = [1 if (i<5) else 0 for i in x]
interval2 = [1 if (i>=5 and i<=10) else 0 for i in x]
interval3 = [0 if (i>10) else 1 for i in x]

y = 1/25*x*interval1+(2/5-1/25*x)*interval2+1*interval3

plt.plot(x,y)
plt.show()