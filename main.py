import folium
import pandas 

map = folium.Map(location=[56.29274,43.9267452], zoom_start=8, tiles="CartoDB dark_matter")

arrCoordinate = [
  [56.2693454,43.9294157],
  [56.3236587,44.0087915],
  [56.2916225,43.9384277],
]

data = pandas.read_csv('volcanoes_USA.txt')

lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

# array = 

def setMarker(array):
  for lat, lon, elevation in array:

    if(elevation < 1000):
      color = "green"
      radius = 9
    elif(1000 <= elevation < 3000):
      color = "orange"
      radius = 11
    else:
      color = "red"
      radius = 13

    marker = folium.CircleMarker(location=[lat, lon], radius=radius, fill_color=color, color="black", fill_opacity = 0.9, popup=str(elevation)+" m")
    marker.add_to(map)
  return True

setMarker(zip(lat, lon, elevation))

map.save('map1.html')