import json
from worldPopulation.country_codes import get_country_code
import pygal
import pygal_maps_world.maps as map

filename = 'D:\Working\pycharm_workspace\matplotlib_gallery\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            print(country_name + ": " + str(population))
            code = get_country_code(country_name)
            if code:
                cc_populations[code] = population
            else:
                print('ERROR - ' + country_name)


    wm = map.World()
    wm.title = 'World Population in 2010, by Country'
    wm.add('2010', cc_populations)

    wm.render_to_file('world_population.svg')