import pygal
import pygal.maps.world as pw
from country_codes import get_country_code
import json

#导入数据
filename = 'world_gdp.json'
with open(filename) as f:
	gdp_data = json.load(f)

#获取每个国家2016年的GDP，做一个字典
gdps_dict={}
for gdp_dict in gdp_data:
	if gdp_dict['Year'] == '2016':
		country_name = gdp_dict['Country Name']
		gdp = int(float(gdp_dict['Value']))
		code = get_country_code(country_name)
		if code:
			gdps_dict[code] = gdp

wg = pw.World()
wg.title = '世界各国GDP'
wg.add('2016',gdps_dict)
wg.render_to_file('各国GDP.svg')
