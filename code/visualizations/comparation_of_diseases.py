import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np

def comp():
    '''
    visualize the comparation of fatality and transmission between differrent diseases

    '''
    fig = go.Figure()

    # getting the fatality rate
    fatal = [0.6,0.35,0.001,0,0,0.5,0.028,0.1,0.0007,0.35,0,0.002]
    # change it to percent %
    fatal = [100*i for i in fatal]

    fig.add_trace(go.Scatter(x = [0,0.8,1.2,1.5,2,2,2.15,3,3.5,4.8,8.5,15],
                            y = fatal, 
                            mode = "markers+text", 
                            # getting the name of diseases
                            text = ['Bird Flu','MERS','Seasonal Flu',"2009 Flu",'Common Cold','Ebola','Spanish Flu','SARS','Polio','Smallpox','Chickenpox','Measles'], 
                            textposition = "bottom center",
                            line = go.scatter.Line(color = "orange"), 
                            name = 'other'))
    
    #change the font size 
    fig.update_traces(textfont_size = 15)

    fig.add_trace(go.Scatter( x = [2.437], 
                            y = [100*2948/80303], 
                            text = "COVID-19", 
                            mode = "markers+text", 
                            textposition = "top right", 
                            line = go.scatter.Line(color = "purple"), 
                            marker = dict(size = [10]), name = 'COVID-19'))

    # change the layout of figure
    fig.update_yaxes(type="log")
    fig.update_layout(
        title="Comparation of fatality rate and R0 bewteen COVID-19 and other diseases",
        xaxis_title="R0 (Average number of people infected by each sick person)",
        yaxis_title="Fatality rate/%(log scale)",
        font=dict(
            family="Courier New",
            size=15,
            color="#292424"
        ),
        showlegend = False
    )
    # show the plot
    fig.show()

comp()