import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
import geopandas
import datetime as dt
from ipywidgets import interact, fixed
import ipywidgets as widgits
import shapely
##Plot Google trends data

def trend_plot():
    '''
    create a line plot of the google trends data
    '''
    #read data
    Trends=pd.read_csv('../../data/trends_data/All_trends.csv')
    assert isinstance(Trends, pd.DataFrame)
    Trends['Day'] = Trends['Day'].apply(dt.datetime.strptime,args=['%m/%d/%Y'])

    #plot
    pd.plotting.register_matplotlib_converters()
    plt.figure(figsize=(20,12))
    plt.plot( 'Day', 'SARS: (United States)', data=Trends, color='skyblue', linewidth=4)
    plt.plot( 'Day', 'Symptom: (United States)', data=Trends, color='green', linewidth=4)
    plt.plot( 'Day', 'wuhan: (United States)', data=Trends, color='red', linewidth=4)
    plt.plot( 'Day', 'coronavirus: (United States)', data=Trends, color='black', linewidth=4)
    plt.plot( 'Day', 'kobe: (United States)', data=Trends, color='gold', linewidth=4)
    plt.rc('xtick', labelsize=15)
    plt.rc('ytick', labelsize=15)
    plt.axvline(min(dat_flat['Last Update']),linestyle='dashed',label="First known case")
    plt.legend(loc='upper left', fontsize=17)