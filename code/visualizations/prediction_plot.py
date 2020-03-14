import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np

def prediction_plot():
    '''
    visualize the prediction infected number of people an ral infected number
    '''
    # load data 
    data_1 = pd.read_csv('../../data/prediction_data/no action.txt', header = None)
    data_2 = pd.read_csv('../../data/prediction_data/traffic.txt', header = None)
    data_3 = pd.read_csv('../../data/prediction_data/newhospital.txt', header = None)
    recover_2 = pd.read_csv('../../data/prediction_data/traffic_recover.txt', header = None)
    recover_3 = pd.read_csv('../../data/prediction_data/newhospital_recover.txt', header = None)
    real_infected = pd.read_csv('../../data/real_population_data/real_infected_data_of_Hubei.csv', header = None)

    assert isinstance(data_1, pd.DataFrame)
    assert isinstance(data_2, pd.DataFrame)
    assert isinstance(data_3, pd.DataFrame)
    assert isinstance(recover_2, pd.DataFrame)
    assert isinstance(recover_3, pd.DataFrame)
    assert isinstance(real_infected, pd.DataFrame)

    fig = go.Figure()
    # plot
    fig.add_trace(go.Scatter(x = list(range(1, 230)),y=5.7*np.array(data_1[0]), mode="lines", name = "No action"))
    fig.add_trace(go.Scatter(x = list(range(25, 230)),y=data_2[0], mode="lines", name = "Traffic restriction"))
    fig.add_trace(go.Scatter(x = list(range(25, 230)),y=recover_2[0], mode="lines", name = "Traffic restrction_recover"))
    fig.add_trace(go.Scatter(x = list(range(40, 230)),y=data_3[0], mode="lines", name = "New Hospital"))
    fig.add_trace(go.Scatter(x = list(range(40, 230)),y=recover_3[0], mode="lines", name = "New Hospital_recover"))

    #fig.update_yaxes(type="log")
    # change the layout of figure
    fig.update_layout(
        title="Prediction of infected people over time",
        xaxis_title="days",
        yaxis_title="number of people",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#292424"
        )
    )
    fig.show()

prediction_plot()
