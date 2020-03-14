import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np

def fit_plot():
    '''
    visualize the fitting infected number of people 
    '''
    # initialization
    # load data 
    data_1 = pd.read_csv('../../data/prediction_data/no action.txt', header = None)
    data_2 = pd.read_csv('../../data/prediction_data/traffic.txt', header = None)
    data_3 = pd.read_csv('../../data/prediction_data/newhospital.txt', header = None)
    real_infected = pd.read_csv('../../data/prediction_data/real_infected_data_of_Hubei.csv', header = None)
    assert isinstance(data_1, pd.DataFrame)
    assert isinstance(data_2, pd.DataFrame)
    assert isinstance(data_3, pd.DataFrame)
    assert isinstance(real_infected, pd.DataFrame)

    fig = go.Figure()
    # plot
    fig.add_trace(go.Scatter(x = list(range(1, 60)),y = real_infected[0], mode="markers", name = "Infected"))
    fig.add_trace(go.Scatter(x = list(range(1, 25)),y = data_1[0], mode="lines", line=go.scatter.Line(color="orange"),name = "No action"))
    fig.add_trace(go.Scatter(x = list(range(25, 41)),y = data_2[0], mode="lines", name = "Traffic restrcition"))
    fig.add_trace(go.Scatter(x = list(range(41, 201)),y = data_3[0], mode="lines", line=go.scatter.Line(color="red"), name = "New Hospital"))
    # change the layout of figure
    fig.update_layout(
        title="Fitting curve",
        xaxis_title="days",
        yaxis_title="number of people",
        font=dict(
            family="Courier New",
            size=15,
            color="#292424"
        )
    )
    fig.show()

fit_plot()
