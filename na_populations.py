import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = 'Population of Countries in North America'
wm.add('North America',{'ca':3412600,'us':309349000,'mx':113423000})
wm.render_to_file('na_population.svg')