import matplotlib.pyplot as plt

x_value = list(range(1,5000))
y_value = [x**3 for x in x_value]
plt.scatter(x_value,y_value,c = y_value,cmap = plt.cm.Reds,edgecolor = 'none',s=20)
#设置图表标题给坐标加参数
plt.title('squares numbers',fontsize = 24)
plt.xlabel('value',fontsize = 14)
plt.ylabel('squares of value',fontsize = 14)
#设置刻度标记的大小
plt.tick_params(axis = 'both',which = 'major',labelsize = 14)
# plt.axis([0,1100,0,1100000])
# plt.savefig('squares_plot.png',bbox_inches='tight')
plt.show()