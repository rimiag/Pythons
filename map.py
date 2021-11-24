import folium
import pandas

#Hospitals List
hospital_list= pandas.read_csv("hospitals.txt")
restaurant_list= pandas.read_csv("Restaurants.txt")
universities_list= pandas.read_csv('universities.txt')
lat = list(hospital_list["LAT"])
lon = list(hospital_list["LON"])
name= list(hospital_list["NAME"])
type= list(hospital_list["TYPE"])
map = folium.Map(location=[33.6603989, 73.157061],zoom_start=6)
fgh =  folium.FeatureGroup(name="My Map")
fgr= folium.FeatureGroup(name="ISB_RESTAURANTS")
fgu= folium.FeatureGroup(name="Universities in Islamabad")

def color_maker(types):
    if types=="Govt":
        return "red"
    else:
        return "orange"

for lt,ln,name,type in zip(lat,lon,name,type):

#for coordinates in [[33.6603989,73.157061],[34.6603989,74.157061]]:
    fgh.add_child(folium.Marker(location=[lt,ln],popup=name, icon=folium.Icon(color=color_maker(type),icon_color='white', icon='glyphicon glyphicon-plus-sign', prefix='glyphicon')))
   #fgh.add_child(folium.Marker(location=[lt,ln],radius =8, popup=name, color = 'grey',
    #fill_color=color_maker(type),fill_opacity='red'))
fgh.add_child(folium.GeoJson(data=open('world.json','r', encoding= 'utf-8-sig').read(),
style_function= lambda x:{'fillColor': 'red' if x['properties']['POP2005'] < 20000000
else 'yellow' if 20000000 <= x['properties']['POP2005']< 50000000 else 'brown'}))

# Resaurant  List
restaurant_list= pandas.read_csv("Restaurants.txt")
r_lat= list(restaurant_list["LAT"])
r_lon= list(restaurant_list["LON"])
r_name= list(restaurant_list["Restaurants"])

for rlt,rln,rname in zip(r_lat,r_lon,r_name):
    fgr.add_child(folium.Marker(location=[rlt,rln],popup=rname, icon=folium.Icon(color='purple', icon_color='white', icon='glyphicon glyphicon-glass', prefix='glyphicon')))

u_lat= list(universities_list["LAT"])
u_lon= list(universities_list["LON"])
u_name=list(universities_list["UNIVERSITY"])

for ulat,ulon,uname in zip(u_lat,u_lon,u_name):
    fgu.add_child(folium.Marker(location=[ulat,ulon],popup=uname,icon=folium.Icon(color='blue',icon='ok',prefix='glyphicon')))
map.add_child(fgr)
map.add_child(fgh)
map.add_child(fgu)
map.add_child(folium.LayerControl())
map.save("isb_map.html")
