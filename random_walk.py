from random import choice
#生成随机漫步的类
class RandomWalk():
	def __init__(self,num_points=5000):
		#初始化随机漫步属性
		self.num_points = num_points
		#所有随机漫步都始于（0,0）
		self.x_values = [0]
		self.y_values = [0]
	def get_step(self):
		g_direction = choice([1,-1])
		g_distance = choice([0,1,2,3,4])
		g_step = g_direction*g_distance
		return g_step
	def fill_walk(self):
		#不断漫步，直到列表到达指定长度
		while len(self.x_values)<self.num_points:
			x_step=self.get_step()
			y_step=self.get_step()
			#拒绝原地踏步
			if x_step == 0 and y_step == 0:
				continue
			#计算下一个点的X,Y值
			next_x=self.x_values[-1]+x_step
			next_y=self.y_values[-1]+y_step
			#把下一个点加入到列表中
			self.x_values.append(next_x)
			self.y_values.append(next_y)


			
			


