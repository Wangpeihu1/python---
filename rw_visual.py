import matplotlib.pyplot as plt

from random_walk import RandomWalk
#程序处于活动状态，就不断模拟随机漫步
while True:
	#创建一个RW实例，并绘制
	rw = RandomWalk()
	rw.fill_walk()
	point_number=list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Reds,edgecolor='none',s=15)
	plt.show()

	keep_running = input('Make another walk ? (y/n): ')
	if keep_running =='n':
		break 