import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import geopandas

def plotter(dat_flat,days_since_start,start_date, Cume=True):
    
    """dat_flat: pandas DataFrame with 'Longitude' and 'Latitude' columns of
    floats and a 'Last Update' column of pd.Timestamp
        days_since_start: integer
        start_date: pandas timestamp
        Cume: bool
        
        Plots a map of the 'Longitude' and 'Latitude' points in China.
        If Cume=True, plots all points between and including start_date and 
        start_date + days_since_start.
        If Cume=False plots only the ploints on start_date + days_since_start"""
        
            
            
    assert isinstance(dat_flat,pd.DataFrame)
    assert isinstance(days_since_start,int)
    assert isinstance(start_date,pd.Timestamp)
    assert isinstance(Cume, bool)


    if Cume:
        D=dat_flat[dat_flat['Last Update']<=start_date+ dt.timedelta(days=days_since_start)]
    else:
        D=dat_flat[dat_flat['Last Update']==start_date+ dt.timedelta(days=days_since_start)]
    cords = geopandas.GeoDataFrame(
        D, geometry=geopandas.points_from_xy(D.Longitude, D.Latitude))

    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

    ax = world[world.name == 'China'].plot(
    color='white', edgecolor='black',figsize=(16,16))
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    cords.plot(ax=ax, color='red',markersize=3, alpha=.7)
    plt.annotate('day: '+str(days_since_start),xy=(75, 53),size=25, ha='left', va='top')
    
    plt.show()