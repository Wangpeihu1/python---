#嵌套 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为 嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)