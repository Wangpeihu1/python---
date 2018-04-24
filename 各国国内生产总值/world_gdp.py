import pygal
import pygal.maps.world as pw
from country_codes import get_country_code
import csv

#导入数据
filename = 'gdp.csv'
with open(filename,) as f:
	gdp_data = csv.reader(f)
	for i in range(5):
		header = next(gdp_data)
		
#获取每个国家2016年的GDP，做一个字典
	gdps_dict={}
	for gdp_dict in gdp_data:
		try:
			country_name = gdp_dict[0]
			gdp = int(gdp_dict[61])
			print(int(gdp_dict[61]))
		except ValueError:
			print('Error')
		else:
			code = get_country_code(country_name)
			if code:
					gdps_dict[code] = gdp

wg = pw.World()
wg.title = '世界各国GDP'
wg.add('2016',gdps_dict)
wg.render_to_file('各国GDP.svg')
