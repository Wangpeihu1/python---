magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title()+', that was a great trick!')
	print("I can't wait to see your next trick,"+magician.title()+'\n')
print("Thank you, everyone. That was a great magic show!")




#创建数值列表,使用list（）将range（）的结果转换列表，range是前闭后开的
#使用range几乎可以创建任何数据集
for value in range(1,5):
	print(value)

numbers = list(range(1,5))
print(numbers)

#range还可以指定步长，默认是1
numbers = list(range(1,10,2))
print(numbers)
squares = []
for value in range(10):
	squares.append(value**2)
print(squares)

#对数字进行简单的统计
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits),min(digits),sum(digits))

#列表解析
squares = [value**2 for value in range(8)]
print(squares)

#练习
for value in range(1,21):
	print(value)

list_1 = range(1,1000001)
print(min(list_1),max(list_1),sum(list_1))

for value in range(1,20,2):
	print(value)
list_2 = list(range(3,31,3))
for value in list_2:
	print(value)

list_3 = [value**3 for value in range(1,11)]
print(list_3)

#切片,切片也是前闭后开
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[0:3]:
	print(player)

#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for food in my_foods:
	print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)
#如果使用以下方式
friend_foods = my_foods
print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)

#可以看到friend_foods与my_foods相同，这其实是将新变量friend_foods关联到my_foods上，他们指向一致