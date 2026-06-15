import osmnx as ox
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

print('imported')

#Map data lkr Regensburg
lkr = ox.geocode_to_gdf('Landkreis Regensburg, Bavaria, Germany') #erstellt geodataframe von Lkr Regensburg


# Load GeoJSON data with Kita information 
kitas = gpd.read_file('items.json')

#Plot map of Lkr Regensburg with locations of Kitas
f, ax = plt.subplots(figsize = (16, 9))
lkr.boundary.plot(ax=ax, color = 'lightblue')
kitas.plot(ax=ax, marker= 'x', markersize= 10, color = 'black')
plt.show()

#Child under 3 years >> Krippen
krippen = kitas[(kitas['krippe'] == True)]
kitas_ohne_krippe = kitas[(kitas['krippe'] == False)]

#Plot map with Kitas for children < and > 3 years
f, ax = plt.subplots(figsize = (16, 9))
lkr.boundary.plot(ax=ax, color = 'lightblue')
kitas_ohne_krippe.plot(ax=ax, marker= 'x', markersize= 10, color = 'black')
krippen.plot(ax=ax, marker= 'o', markersize= 10, color = 'red')
ax.legend()
plt.show()

#Use Beratzhausen as example
beratzhausen = ox.geocode_to_gdf('Beratzhausen, Landkreis Regensburg, Bavaria, 93176, Germany') #geodataframe Gemeinde Beratzhausen
#Get more details from Beratzhausen (buildings)
beratz_details = ox.features.features_from_place('Beratzhausen, Landkreis Regensburg, Bavaria, 93176, Germany', {"building": True, "amenities": True})

#Get Kitas in Beratzhausen
kitas_beratzhausen = kitas[(kitas['plz_ort'] == '93176 Beratzhausen')]

#Plot Kitas in Beratzhausen
f, ax = plt.subplots(figsize = (16, 9))
beratzhausen.boundary.plot(ax=ax, color = 'black')
beratz_details.plot(ax = ax, color = 'lightblue')
kitas_beratzhausen.plot(ax=ax, marker= 'x', markersize= 10, color = 'green')
plt.show()

#Krippen in Beratzhausen
krippen_beratzhausen = kitas_beratzhausen[(kitas['krippe'] == True)]
kitas_ohne_krippe_beratzhausen = kitas_beratzhausen[(kitas['krippe'] == False)]

#Plot Krippen in Beratzhausen
f, ax = plt.subplots(figsize = (16, 9))
beratzhausen.boundary.plot(ax=ax, color = 'black')
beratz_details.plot(ax = ax, color = 'blue')
kitas_ohne_krippe_beratzhausen.plot(ax=ax, marker= 'x', markersize= 20, color = 'black')
krippen_beratzhausen.plot(ax=ax, marker= 'o', markersize= 20, color = 'red')
#show names of Krippen
for x, y, label in zip(krippen_beratzhausen.geometry.x, krippen_beratzhausen.geometry.y, krippen_beratzhausen.name):
    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")
plt.show()

#Names of Krippen in Beratzhausen
#f, ax = plt.subplots(figsize = (16, 9))
#beratzhausen.boundary.plot(ax=ax, color = 'lightblue')
#kitas_ohne_krippe_beratzhausen.plot(ax=ax, marker= 'x', markersize= 20, color = 'black')
#krippen_beratzhausen.plot(ax=ax, marker= 'o', markersize= 20, color = 'red')
#for x, y, label in zip(krippen_beratzhausen.geometry.x, krippen_beratzhausen.geometry.y, krippen_beratzhausen.name):
#    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")
#plt.show
#
#

##keine_krippen = kitas[(kitas['krippe'] == False)]
##print(len(kitas),len(krippen), len(keine_krippen))
#
#
#
#f, ax = plt.subplots(figsize = (16, 9))
#
#beratzhausen.boundary.plot(ax = ax, color = 'lightblue')
#krippen_beratzhausen.plot(ax = ax, marker = 'o')



#kitas_beratzhausen.plot(ax=ax, marker= 'x', markersize= 20, color = 'black')

#for x, y, label in zip(krippen.geometry.x, krippen.geometry.y, krippen.name):
##    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")
##
#ax = kitas_ohne_krippe_beratzhausen.plot(ax = ax, marker = 'x')
#for x, y, label in zip(kitas_ohne_krippe_beratzhausen.geometry.x, kitas_ohne_krippe_beratzhausen.geometry.y, kitas_ohne_krippe_beratzhausen.name):
#    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")
#    print(label)
#plt.show
##

## Plot the graph





#ax = krippen.plot(figsize = (20, 10))
#
#for x, y, label in zip(krippen.geometry.x, krippen.geometry.y, krippen.name):
#    ax.annotate(label, xy=(x, y), xytext=(3, 3), textcoords="offset points")
#
#plt.show()
print('hjg')