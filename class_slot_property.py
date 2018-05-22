#__slot__限制创建实例的属性
#根据类创建实例后，还可以继续给实例添加其他属性，可以通过__slot__限制添加

from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'set_age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)
print(s.age)

#s.score = 99 # 绑定属性'score'报错

#Python内置的@property装饰器就是负责把一个方法变成属性调用的

class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score)