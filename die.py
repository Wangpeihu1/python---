from random import randint

class Die():
	#创建die类
	def __init__(self,numsides=6):
		#骰子面数为6
		self.numsides = numsides
	def roll(self):
		return randint(1,self.numsides)