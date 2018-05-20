#字典 是一系列 键 — 值对 。每个 键 都与一个值相关联，你可以使用键来访问与之相关联的值。
#与键相关联的值可以是数字、字符串、列表乃至字典
#键和值之间用冒号分隔，而键 — 值对之间用逗号分隔。
alien_0 = {'color': 'green', 'points': 5,'speed': 'medium'}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print(alien_0)
#添加键 — 值对,字典名[键]=值
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#修改字典中的值，字典名[键]=值
alien_0['color'] = 'yellow'
print(alien_0)
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
#  这个外星人的速度一定很快
	x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
#删除键 — 值对 del
del alien_0['points']
print(alien_0)


#遍历字典键 — 值对 可声明两个变量，用于存储键 — 值对中的键和值。
#对于这两个变量，可使用任何名称。下面的代码使用了简单的变量名
#for语句的第二部分指明字典名和方法items（）
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

#遍历字典键
#for语句的第二部分指明字典名和方法keys(),keys可以省略
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
friends = ['phil', 'sarah',]
for name in favorite_languages.keys():
	if name in friends:
		print(" Hi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")
#方法 keys() 并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键	
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")		
#按顺序遍历字典中的所有键,使用函数 sorted() 来获得按特定顺序排列的键列表的副本
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
#遍历字典中的所有值,可使用方法 values()
for language in favorite_languages.values():
	print(language.title())
#遍历字典中的值时，可能会有很多重复，用set()
for language in set(favorite_languages.values()):
	print(language.title())
	