import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def vis_curve_fit():
	'''
		This function reads the data and do the necessay process and plots the curve fit the data

	'''
	hubei_actions2 = {}
	hubei_actions2[444.0] = 'Hubei Province launches secondary emergency response'
	hubei_actions2[444.0] = 'Hubei Elementary and Middle Schools extend school start date'
	hubei_actions2[549.0] = 'Hubei Province initiated a second-level emergency response'
	hubei_actions2[2714.0] = '100,000 beds in hospital are set up'
	hubei_actions2[5806.0] = 'Hubei will extended Lunar New Year holidayHubei will appropriately extend the Spring Festival holidays'
	hubei_actions2[11177.0] = 'Hubei cancels marriage registration on February 2'
	hubei_actions2[11177.0] = 'From February 3, Hubei will suspend all marriage registration services'
	hubei_actions2[16678.0] = 'Hubei once again urgently issued 200 million subsidies for treatment'

	hubei_actions = {}
	hubei_actions['2020-01-11'] = 'Hubei Provincial Congress opens'
	hubei_actions['2020-01-22'] = 'Hubei Province launches secondary emergency response'
	hubei_actions['2020-01-23'] = 'Hubei Elementary and Middle Schools extend school start date'
	hubei_actions['2020-01-27'] = '100,000 beds in hospital are set up'
	hubei_actions['2020-01-31'] = 'Hubei will extended Lunar New Year holidayHubei will appropriately extend the Spring Festival holidays'
	hubei_actions['2020-02-02'] = 'Hubei cancels marriage registration on February 2'
	hubei_actions['2020-02-03'] = 'From February 3, Hubei will suspend all marriage registration services'
	hubei_actions['2020-02-05'] = 'Hubei once again urgently issued 200 million subsidies for treatment'


	wuhan_actions = {}
	wuhan_actions['2020-12-31'] = 'Wuhan municipal health commission publicly notified 27 cases of unknown pneumonia, stating that there is no obvious human-to-human transmission and no medical staff infection.'
	wuhan_actions['2020-01-01'] = 'The suspected virus source Huanan Seafood market is shuted down.'
	wuhan_actions['2020-01-05'] = 'Wei Wuhan Construction Committee publicly notified 59 cases of pneumonia of unknown causes, indicate no obvious person to person, not found among health care workers.'
	wuhan_actions['2020-01-11'] = 'Hubei opening two sessions'
	wuhan_actions['2020-01-20'] = 'Wuhan has set up fever clinics and designated medical institutions: 61 fever clinics, 9 designated medical institutions, and 25 provincial and municipal joint medical treatment experts.'
	wuhan_actions['2020-01-22'] = 'Hubei Province launches secondary emergency response / Wuhan implements epidemic investigation on vehicles entering and leaving the city / Wuhan Tongji and Wuhan Xiehe simultaneously release guidelines for rapid diagnosis and treatment of new coronavirus pneumonia'
	wuhan_actions['2020-01-23'] = 'Wuhan closure of the city / All tourist teams in Wuhan will be canceled / Wuhan New Pneumonia Prevention and Control Headquarters will open a 24-hour phone call to accept donations , Cruise rental single and double number limit line'
	wuhan_actions['2020-01-24'] = 'Wuhan will build hospital in Xiaotangshan mode / Wuhan closes river crossing tunnel'
	wuhan_actions['2020-01-25'] = 'Wuhan Requisitions Ten Thousand Beds in 24 Hospitals for Fever Patients / Motor Vehicle Prohibition in Central Wuhan'
	wuhan_actions['2020-01-26'] = 'All hospitals in Wuhan receive 24-hour hot clinics.'
	wuhan_actions['2020-02-04'] = 'Vulcan Mountain begins to treat patients'
	wuhan_actions['2020-02-06'] = 'Wuchang Fangcai Hospital begins to treat patients with mildly diagnosed disease / Wuhan's national body temperature monitoring'
	wuhan_actions['2020-02-08'] = 'Thunder Mountain begins to treat patients'

	#read data from csv
	data = pd.read_excel('../../data/population_data/population_data.xlsx', usecols=['Last Update','Confirmed', 'Province/State'], parse_dates=['Last Update'])
	#drop nan rows 
	data = data.replace(0, np.nan)
	data = data.dropna()
	# Taking Hubei 
	t = data['Province/State'] == 'Hubei'
	for i in list(t.index):
	    if not t[i]:
	        data = data.drop(i)
	# Removing Repeated Items 
	length = len(list(data.index))
	data.index = range(length)
	dropped = []
	for i in range(length-1):
	    if data.iloc[i]['Last Update'].date() == data.iloc[i+1]['Last Update'].date():
	            if data.iloc[i]['Last Update'] >= data.iloc[i+1]['Last Update']:
	                dropped.append(i+1)
	for i in dropped:
	    data = data.drop(i)
	data.drop('Province/State', axis=1, inplace=True)
	#removing the time from the dates 
	for i in data['Last Update'].index:
	    data['Last Update'][i] = pd.Timestamp(data['Last Update'][i].date())
	#set date as index
	data.set_index('Last Update',inplace=True)

	#set ggplot style
	plt.style.use('ggplot')

	#plot data
	fig, ax = plt.subplots(figsize=(15,7))
	rects = ax.plot(data.index, data['Confirmed'])

	#set ticks every week
	ax.xaxis.set_major_locator(mdates.DayLocator())
	#format date
	ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

	ax.set_title('Number of Confirmed Cases')
	ax.set_ylabel('Confirmed Cases')
	ax.set_xlabel('Date')

	y = pd.read_excel('../../data/real_population_data/real_infected_data_of_Hubei.csv')
	#y = [1,2,3,4,6,9,12,20,28,41,41,41,41,41,41,45,62,121,198,291,440,542,769,1068,1452,2762,3591,5869,7234,9101,11227,13539,16619,19502,21863,24213,26406,28648,30392,31748,43437,46768,48128,48987,49793,50257,50425,49481,48637,47647,46435,45054,43346,41637]
	x = np.arange(len(y))
	z4 = np.polyfit(x, y, 15)
	p4 = np.poly1d(z4)

	plt.style.use('ggplot')

	#plot data
	fig, ax = plt.subplots(figsize=(12,7))

	ax.plot(x, p4(x), '-', color='purple')
	ax.set_facecolor('white')
	ax.tick_params(axis='x', colors='black')
	ax.tick_params(axis='y', colors='black')
	ax.spines['bottom'].set_color('black')
	ax.spines['left'].set_color('black')

	csfont = {'fontname':'Courier New', 'size': 15}
	ax.set_title('Number of Confirmed Cases', **csfont)
	ax.set_ylabel('Confirmed Cases', **csfont)
	ax.set_xlabel('days', **csfont)
	ax.grid('on')
	plt.show()


