import pygal
from random_walk import RandomWalk

rw = RandomWalk(1000)
rw.fill_walk()
rw_chart = pygal.XY(storke=False)
rw_chart.title = 'RandomWalk'
rw_chart.add('rw',[(rw.x_values[num],rw.y_values[num]) for num in range(len(rw.x_values))])
rw_chart.render_to_file('123')