from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt

proportion = [0.261,0.239,0.217,0.152,0.043,0.087]
boundary = [0,1000,2000,3000,4000,5000,6000]
plt.hist(proportion,boundary,histtype='bar',rwidth=1)
plt.legend()
plt.xlabel('total length')
plt.ylabel('proportion')

plt.show()
'''
plt.figure(6)
rects = plt.bar(x=(10,20,30,40,50),height=(126,210,67,54,131),width=10,align='edge',yerr=0.000001,edgecolor='red')
plt.title('Histogram')
def autolabel(rects):  # 在每个长方形上加标注
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/3.5,1.01*height,'%s'%float(height))
autolabel(rects)
plt.show()
'''