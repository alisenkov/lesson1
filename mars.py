import ephem
mars = ephem.Mars('2016/09/23')
ephem.constellation(mars)
print(ephem.next_full_moon('2016/06/23'))

