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