import matplotlib.pyplot as plt
from datetime import datetime 
import csv
#导入所需模块

filename = '20140105.csv'
with open(filename) as f:
	reader = csv.reader(f)
	head_row = next(reader)

	dates,highs,lows = [],[],[]
	for row in reader:
		try:
			current_date = datetime.strptime(row[0],'%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,'miss data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
#把数据导入到三个列表中

fig = plt.figure()
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
fig.autofmt_xdate()
plt.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.1)
plt.show()
