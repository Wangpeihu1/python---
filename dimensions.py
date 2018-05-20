#元组看起来像列表，但是不能修改,使用圆括号
dimensions = (200, 50)
print(dimensions[0],dimensions[1])
for dimension in dimensions:
	print(dimension)
#虽然不可修改元组中的元素，但是可以给元组变量赋值
dimensions = (400, 100)
print(dimensions[0],dimensions[1])
for dimension in dimensions:
	print(dimension)