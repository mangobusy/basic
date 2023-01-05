from matplotlib import pyplot as plt
import numpy as np

def draw(li1,li2):

    '''plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus']=False
    plt.figure(figsize=(10,4))
    plt.plot((2,2),1,len(li2)+0.5)'''
    plt.xlim(1,45)
    plt.ylim(1,20)
    plt.axis('off')

    plt.vlines(4,0,10)
    # 输出茎
    for i in range(len(li1)):
        plt.text(0,len(li1)-i,str(li1[i]),fontsize=12)
    plt.text(0,len(li1)+1,'stem',fontsize=12)
    # 输出叶
    for j in range(len(li2)):
        plt.text(5, len(li2) - j, ', '.join(map(str, li2[j])), fontsize=12)
    plt.text(5,len(li1)+1,'leaves',fontsize=12)
    plt.show()
#
li1=['.3','.4L','.4H','.5','.6','.7']
li2=[[1,5,6,6,7,8],[0,0,0,1,1,2,2,2,2,2,3,4],[5,6,6,7,8,8,8],[1,4,4,5,8],
     [2,6,6,7,8],[5],]
'''
li1 = [0,1,2,3,4,5]
li2 = [[100,240,340,360,396,450,500,510,530,540,960,960],[000,50,120,240,250,280,320,419,670,850,890],
       [100,109,120,250,320,400,400,460,700,730],[60,150,150,330,350,380,870],
       [390,770],[220,320,770,850]]'''
draw(li1,li2)