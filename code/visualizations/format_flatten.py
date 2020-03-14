import numpy as np
import pandas as pd
def format_flatten(dat):
    
    '''dat:pandas dataframe with columns 'confirmed', 'Province/State', 'confirmed_on_day'
    Flattens dat file to be casewise'''
    
    assert isinstance(dat,pd.DataFrame)
    
    for place in set(dat['Province/State']):
        A=dat[dat['Province/State']==place]['Confirmed'].to_numpy()
        if(len(A)>0):
            A=np.ediff1d(A,to_begin=A[0])
            A[A<0]=0
            dat.loc[dat['Province/State']==place,'Confirmed_on_day']=A
    return dat.loc[dat.index.repeat(dat.Confirmed_on_day)]