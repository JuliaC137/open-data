import osmnx as ox
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

print('imported')

#Map data lkr Regensburg
lkr = ox.geocode_to_gdf('Landkreis Regensburg, Bavaria, Germany') #erstellt geodataframe von Lkr Regensburg

# Load GeoJSON data with Kita information 
kitas = gpd.read_file('items.json')

#Define map colors
boundary_color = "black"
street_color = "black"
landuse_color = 'lightgreen'
buildings_color = 'orange'
building_edges = "black"
water_color = 'lightblue'
marker_kita_color = 'blue'
marker_krippe_color = 'red'


#Plot map of Lkr Regensburg with locations of Kitas
f, ax = plt.subplots(figsize = (16, 9))
lkr.boundary.plot(ax = ax, color = boundary_color, linewidth = 0.5)
kitas.plot(ax = ax, marker = 'x', markersize = 25, color = marker_kita_color, label = 'Kita')
ax.legend()
plt.show()
f.savefig(
    "figures/lkr_regensburg_kitas.svg",
    dpi = 400,
    bbox_inches = "tight"
)

#Child under 3 years >> Krippen
krippen = kitas[(kitas['krippe'] == True)]
kitas_ohne_krippe = kitas[(kitas['krippe'] == False)]

#Plot map with Kitas for children < and > 3 years
f, ax = plt.subplots(figsize = (16, 9))
lkr.boundary.plot(ax = ax, color = boundary_color, linewidth = 0.5)
kitas_ohne_krippe.plot(ax = ax, marker = 'x', markersize= 10, color = marker_kita_color, label = 'Kita ohne Krippe')
krippen.plot(ax = ax, marker = 'x', markersize = 25, color = marker_krippe_color, label = 'Krippe')
ax.legend()
plt.show()
f.savefig(
    "figures/lkr_regensburg_krippen.svg",
    dpi = 400,
    bbox_inches = "tight"
)

#Use Beratzhausen as example
beratzhausen_geocode = 'Beratzhausen, Landkreis Regensburg, Bavaria, 93176, Germany'
beratzhausen = ox.geocode_to_gdf(beratzhausen_geocode) #geodataframe Gemeinde Beratzhausen
#Get more details from Beratzhausen (buildings, streets)
beratz_buildings = ox.features.features_from_place(beratzhausen_geocode, {"building": True})
beratz_landuse = ox.features.features_from_place(beratzhausen_geocode, {"landuse": True})
beratz_streets = ox.features.features_from_place(beratzhausen_geocode, {"highway": True})
beratz_water = ox.features.features_from_place(beratzhausen_geocode, {"water": True, "waterway": True, "natural": "water"})

#Get Kitas in Beratzhausen
kitas_beratzhausen = kitas[(kitas['plz_ort'] == '93176 Beratzhausen')]

#Plot Kitas in Beratzhausen
f, ax = plt.subplots(figsize = (16, 9))
beratzhausen.boundary.plot(ax = ax, color = boundary_color, linewidth = 0.5)
#beratz_streets.plot(ax = ax, color = street_color, linewidth = 0.5)
beratz_landuse.plot(ax = ax, color = landuse_color, alpha = 0.35)
beratz_water.plot(ax = ax, color = water_color, alpha = 0.35)
beratz_buildings.plot(ax = ax, color = buildings_color, alpha = 0.6)
kitas_beratzhausen.plot(ax = ax, marker = 'x', markersize= 25, color = marker_kita_color, label = 'Kita')
ax.legend()
plt.show()
f.savefig(
    "figures/beratzhausen_kitas.svg",
    dpi = 400,
    bbox_inches = "tight"
)

#Krippen in Beratzhausen
krippen_beratzhausen = kitas_beratzhausen[(kitas_beratzhausen['krippe'] == True)]
kitas_ohne_krippe_beratzhausen = kitas_beratzhausen[(kitas['krippe'] == False)]

#Plot Krippen in Beratzhausen
f, ax = plt.subplots(figsize = (16, 9))
beratzhausen.boundary.plot(ax = ax, color = boundary_color, linewidth = 0.5)
#beratz_streets.plot(ax = ax, color = street_color, linewidth = 0.5)
beratz_landuse.plot(ax = ax, color = landuse_color, alpha = 0.35)
beratz_water.plot(ax = ax, color = water_color, alpha = 0.35)
beratz_buildings.plot(ax = ax, color = buildings_color, alpha = 0.6)
kitas_ohne_krippe_beratzhausen.plot(ax = ax, marker = 'x', markersize= 30, color = marker_kita_color, label='Kita ohne Krippe')
krippen_beratzhausen.plot(ax = ax, marker = 'x', markersize = 30, color = marker_krippe_color, label = 'Krippe')
ax.legend()
#show names of Krippen
for x, y, label in zip(krippen_beratzhausen.geometry.x, krippen_beratzhausen.geometry.y, krippen_beratzhausen.name):
    ax.annotate(label, xy = (x, y), xytext = (3, 3), textcoords = "offset points", color = 'black', fontsize = 10)
plt.show()
f.savefig(
    "figures/beratzhausen_krippen.svg",
    dpi = 400,
    bbox_inches = "tight"
)

#Plot Krippen in Beratzhausen
f, ax = plt.subplots(figsize = (16, 9))
beratzhausen.boundary.plot(ax = ax, color = boundary_color, linewidth = 0.5)
beratz_streets.plot(ax = ax, color = street_color, linewidth = 0.5)
beratz_landuse.plot(ax = ax, color = landuse_color, alpha = 0.35)
beratz_water.plot(ax = ax, color = water_color, alpha = 0.35)
beratz_buildings.plot(ax = ax, color = buildings_color, edgecolor = building_edges, alpha = 0.6)
kitas_ohne_krippe_beratzhausen.plot(ax = ax, marker= 'x', markersize= 30, color = marker_kita_color, label = 'Kita ohne Krippe')
krippen_beratzhausen.plot(ax = ax, marker = 'x', markersize= 30, color = marker_krippe_color, label = 'Krippe')
#Nur Ausschnitt mit Krippen
xmin, ymin, xmax, ymax = krippen_beratzhausen.total_bounds
dx = xmax - xmin
dy = ymax - ymin
ax.set_xlim(xmin - 0.5 * dx, xmax + 0.5 * dx)
ax.set_ylim(ymin - 0.5 * dy, ymax + 0.5 * dy)
ax.legend()
#show names of Krippen
for x, y, label in zip(krippen_beratzhausen.geometry.x, krippen_beratzhausen.geometry.y, krippen_beratzhausen.name):
    ax.annotate(label, xy = (x, y), xytext = (3, 3), textcoords = "offset points", color = 'black', fontsize = 20)
plt.show()
f.savefig(
    "figures/beratzhausen_krippen_ausschnitt.svg",
    dpi=400,
    bbox_inches = "tight"
)


f, ax = plt.subplots(figsize = (16, 9))
lkr.plot(ax = ax, color = 'lightblue', linewidth = 0.5)
plt.show()
f.savefig(
    "figures/lkr_regensburg.svg",
    dpi = 400,
    bbox_inches = "tight"
)

print('fertig')