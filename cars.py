#使用sort（）对列表进行永久排序,这位列表的一个属性
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
#函数lower（）、upper（）、title（）不会改变car中的值
#使用sorted（）对列表进行永久排序，这是函数
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('原始列表如下:\n\t',cars)
print('临时排序列表如下:\n\t',sorted(cars,reverse=True))
print('原始列表如下:\n\t',cars)
#reverse倒着打印列表,这是列表的一个属性
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
#确定列表长度
print(len(cars))


#检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
#检查特定值是否不包含在列表中 用not in

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


#if-else语句
age = 17
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

#if-elif-else语句
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

#练习
alien_color = 'red'
if alien_color == 'green':
	print('你获得了五点')
elif alien_color == 'yellow':
	print('你获得了10点')
else:
	print('你获得了15点')

favorite_fruits = ['apple','bananas','pear']
if 'bananas' in favorite_fruits:
	print('我喜欢香蕉')
