import numpy as np
import pandas as pd
import geopandas
import shapely
def add_gaussian_noise(x):
    '''x:pandas dataframe with columns 'Longitude', 'Latitude/State'
    Add truncated Gaussian noise to x'''
    
    assert isinstance(x,pd.Series)
    
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    x=[x['Longitude'] ,x['Latitude']]
    while True:
        x_hat=list(np.random.multivariate_normal(x,[[1,0],[0,1]]))
        if float(world[world.name == 'China'].boundary.convex_hull.distance(shapely.geometry.Point(x_hat)))<0.001:
            return pd.Series(x_hat)