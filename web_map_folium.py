import folium


# Create base map
map = folium.Map(location=[8.373988, 8.402566], zoom_start = 8)

map.save(outfile='map1.html')