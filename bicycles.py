bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])


#修改列表中的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

#添加列表中的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
#插入元素
motorcycles.insert(0,'ducati')
print(motorcycles)

#删除元素。del 后面跟上索引，元素删除后消失
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
#使用pop（）删除元素.列表就像是一个栈，pop（）弹出栈顶元素。元素从列表中消失，但是放在了变量内
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
#需要弹出1位置的元素使用pop（1），例如
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)
#根据值删除元素，remove（）
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)

#练习
guest = ['wang','li','zhang','zhao']
print('宾客名单:\n\t',guest)
guest_no = 'li'
print(guest_no+'无法赴约')
guest[1] = 'qian'
print('宾客名单:\n\t',guest)
print('找到更大的餐桌，增加嘉宾')
guest.insert(0,'zhou')
guest.insert(3,'wu')
guest.append('liu')
print('宾客名单:\n\t',guest)
print('没钱了，减少宾客，只邀请2个')
popped_guest = guest.pop()
print('抱歉，没钱了，回家吧'+popped_guest)
popped_guest = guest.pop()
print('抱歉，没钱了，回家吧'+popped_guest)
popped_guest = guest.pop()
print('抱歉，没钱了，回家吧'+popped_guest)
popped_guest = guest.pop()
print('抱歉，没钱了，回家吧'+popped_guest)
popped_guest = guest.pop()
print('抱歉，没钱了，回家吧'+popped_guest)
print('宾客名单:\n\t',guest)
del guest[0]
del guest[0]
print('宾客名单:\n\t',guest)