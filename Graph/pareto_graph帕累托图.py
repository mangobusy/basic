import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = [126,210,67,54,131]
data.sort(reverse=True)
plt.figure(figsize=(12,8))
data = pd.Series(data,index=['failed component','incorrect component','insufficient solder','excess solder','missing component'])

data.sort_values(ascending=False,inplace=True)
p = data.cumsum()/data.sum()
key = p[p>0.8].index[0]
key_num = data.index.tolist().index(key)
plt.figure(figsize=(80,6))
data.plot(kind='bar',color='g',alpha=0.9,width=0.4,rot=0)
p.plot(style='--ko',secondary_y=True)
plt.axvline(key_num,color='r',linestyle='--',alpha=0.8)
plt.text(key_num+0.2,p[key]-0.05,'cumulative proportion:%.3f%%' % (p[key]*100),color='r')
plt.show()