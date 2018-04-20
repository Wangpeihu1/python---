import pygal
from die import Die
#创建2个D6
die_1=Die()
die_2=Die()
#掷几次骰子，并将结果存放在列表中
results=[]
# for roll_num in range(3000):
# 	result = die_1.roll()+die_2.roll()
# 	results.append(result)
results=[die_1.roll()+die_2.roll() for roll_num in range(3000)]
#分析结果
max_result=die_1.numsides+die_2.numsides
# for value in range(2,max_result+1):
# 	frequency=results.count(value)
# 	frequencies.append(frequency)
frequencies=[results.count(value) for value in range(2,max_result+1)]
#制作X轴列表循环
nums=[num for num in range(2,max_result+1)]

#对结果进行可视化
hist = pygal.Bar()
hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = nums
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'
hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')
