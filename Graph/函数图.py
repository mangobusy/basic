import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,50,1)
y=(200-5*x)(0.65-0.01*x+0.00004*x*x)-45*x
#z=0.65-0.01*x
plt.xlabel('x')
plt.ylabel('y')
plt.title("price graph")
plt.plot(x,y,label="new")
#plt.plot(x,z,label="original")
# plt.legend()
plt.show()