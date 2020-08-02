import folium 
import pandas as pd
import numpy as np



map_hooray = folium.Map(location=[51.5074, 0.1278],
                   zoom_start=12,tiles='Stamen Terrain')
map_hooray.save('generatedMap.html')