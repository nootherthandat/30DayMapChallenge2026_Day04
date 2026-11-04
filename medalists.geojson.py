import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

df = pd.read_csv("#30DayMapChallenge2026 (Day 04_ Clusters) - Birthplaces of Summer Olympics Medalists.csv")
df['Region'] = df['Region'].ffill()
df_valid = df.dropna(subset=['Name']).copy()

coords = {
    "National Capital Region (NCR)": [121.0223, 14.6091], 
    "IX - Zamboanga Peninsula": [122.8637, 8.1541],
    "VI - Western Visayas": [122.5667, 10.7333],
    "I - Ilocos Region": [120.4667, 17.2000],
    "IV-A - CALABARZON": [121.1333, 14.1000],
    "V - Bicol Region": [123.3667, 13.4167],
    "VIII - Eastern Visayas": [125.0000, 11.9167],
    "X - Northern Mindanao": [124.9000, 8.1833],
    "XI - Davao Region": [125.5333, 7.1500]
}

df_valid['Lon'] = df_valid['Region'].map(lambda x: coords.get(x, [None, None])[0])
df_valid['Lat'] = df_valid['Region'].map(lambda x: coords.get(x, [None, None])[1])
df_valid = df_valid.dropna(subset=['Lon', 'Lat'])

geometry = [Point(xy) for xy in zip(df_valid['Lon'], df_valid['Lat'])]
gdf = gpd.GeoDataFrame(df_valid, geometry=geometry, crs="EPSG:4326")

gdf.to_file("medalists.geojson", driver="GeoJSON")