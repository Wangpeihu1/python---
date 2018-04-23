import csv
import matplotlib.pyplot as plt
from datetime import datetime
#从文件中读取最高温度
filename = '20140105.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates,highs,lows= [],[],[]
	for row in reader:
		try:
			# date_time = datetime.strptime(row[0],'%Y-%m-%d')
			current_date = datetime.strptime(row[0],'%Y-%m-%d')
			high1 = int(row[1])
			low1 = int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high1)
			lows.append(low1)
		
#绘制图形
fig = plt.figure(figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.axis([dates[0],dates[-1],0,150])
plt.title('Daily  temperature')
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
#调用enumerate（）获取元素的索引及值
# for index,column_header in enumerate(header_row):
# 	print(index,column_header)