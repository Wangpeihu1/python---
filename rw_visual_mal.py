import matplotlib.pyplot as plt

from die import Die
die_1=Die()
#掷骰子并将结果存放在列表在
results=[]
results=[die_1.roll() for roll_num in range(2000)]
max_result=die_1.numsides
frequencies=[results.count(value) for value in range(1,max_result+1)]
nums=[num for num in range(1,max_result+1)]
#对结果作图
plt.figure(figsize=(10,6))
plt.plot(nums,frequencies,c='red',linewidth=1)
plt.show()