import ephem
import datetime

# mars = ephem.Mars("2021/01/01")
# print(dir(mars))
# print(mars.earth_distance)

now = datetime.datetime.now()
mars = ephem.Mars(now.strftime("%d/%m/%Y"))
const = ephem.constellation(mars)
print(const)

print(mars)



def user_planet(planet_name):
    now = datetime.datetime.now()
    if planet_name == "Mars":
        planet = ephem.Mars(now.strftime("%d/%m/%Y"))
    elif planet_name == "Venus":
        planet = ephem.Venus(now.strftime("%d/%m/%Y"))
    const = ephem.constellation(planet)
    return const
planet_now = user_planet("Venus")
print(planet_now)