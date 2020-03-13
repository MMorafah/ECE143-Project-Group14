get_ipython().system('pip install scikit-opt')
from sko.SA import SA
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def seir_model(N, Initial_data, data, name):
    '''
    This function will return fitting and prediction number of COVID-19

    :param
        Input: N --> The total number of people that is affected by the virus
               Initial_data --> data of first day we are gonna to model, in the form of [suspected people, exposed people, infected people, recovered people]
               data --> Number of infected people data extractd from formal resource
               name --> the filename want to store the data in
        Output : data is written to txt file and stored as well.
    '''
    assert isinstance(Initial_data, list) and all(isinstance(i, int) for int in Initial_data) len(Initial_data) = 4 
    assert isinstance(data, list) and all(isinstance(i, int) for int in data)
    length = len(data)

    def demo_func(x):
        '''
        This function is for choosing parameter.
        :param
            Input: x --> parameters that we need to choose
            Output: least square error is the evaluator for parameter
        '''

        beta,beta2,alpha = x
        #Infection rate, Infection rate during Incubation， Latency conversion rate
        nums = Initial_data
        predicted_data = []
        x = np.array(x).T
        least_square_error = 0

        # latency conversion rate can not be larget than 1
        # infection rate should be larget than Infection rate during Incubation

        # parameter restriction
        if(alpha < 0):
            return float('inf')
        if(beta < beta2):
            return float('inf')
        if(beta2 < 0):
            return float('inf')

        for i in range(length):
            # use 4 functions to iterate in SEIR model
            temp = np.array([[1, -beta2 / N * nums[0], -beta / N * nums[0], 0],
                            [beta / N * nums[2], 1 - alpha, 0, 0],
                            [0, alpha, 1, 0],
                            [0, 0, 0,1 ]])
            nums = temp.dot(nums)
            predicted_data.append(nums[2])
            least_square_error += (predicted_data[i] - data[i]) ** 2

        return least_square_error 

    # calculate parameters using Simulated annealing
    sa = SA(func = demo_func, x0 = [3,0,0])
    x_star, y_star = sa.run()
    np.savetxt('qianqi_canshu.txt', [x_star], delimiter = ',')

    # pass parameters to SEIR model
    beta,beta2,alpha = x_star
    predicted_days = 200
    nums = Initial_data
    predicted_data= []
    recovered = []
    x = np.array(x).T

    least_square_error =0
    for i in range(predicted_days):
        # use 4 functions to iterate in SEIR model
        temp = np.array([[1, -beta2 / N * nums[0], -beta / N * nums[0], 0],
                            [beta / N * nums[2], 1 - alpha, 0, 0],
                            [0, alpha, 1, 0],
                            [0, 0, 0,1 ]])
        nums = temp.dot(nums)
        recovered.append(nums[3])
        predicted_data.append(nums[2])
        recovered_data.append(nums[3])

    np.savetxt(name + '_infected.txt', predicted_data, delimiter=',')
    np.savetxt(name + '_recovered.txt', recovered_data, delimiter=',')


N = 58000000
data = list(pd.read_csv('../../data/', header = None))
seir_model(N, [N,0,0,0], data[:25], 'No_action')
seir_model(N, [N-2762-20-152,20000,2762,152], data[25:41], 'Traffic')
seir_model(N, [N-46057-20000-4769,20000,43437,4769], data[41:], 'New_Hospital')

