#使用sort（）对列表进行永久排序,这位列表的一个属性
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

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