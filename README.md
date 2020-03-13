# ECE143-Project-
## Analysis and Prediction of Novel Coronavirus (COVID-19) Cases

### RAW Data: https://www.kaggle.com/brendaso/2019-coronavirus-dataset-01212020-01262020

- ### Data Scrap:
1. Weibo
```
->pacakge used:re,json,requests
->location: code/scraper/weibo_scraper.py
->description: scrap data from weibo.com with the posts contain the word we need.
->data generated: data generated is stored in data/RawNutritionData
```

2. XXX

- ### Data Modeling:
```
->pacakge used:scikit-opt, numpy, pandas
->location: code/model/SEIRmodel.py
->description: This function will return fitting and prediction number of COVID-19. It makes use of annealing methond to get important parameters.
->data generated: data generated is stored in data/prediction_data
```

- ### Visualization:
1. real data fitting
```
->pacakge used: plotly, pandas, numpy
->location: code/visualizations/fitting_plot.py
->description: visualize the fitting infected number of people. The graph generated is interactive.
```

2. prediction of future infected and recovered people
```
->pacakge used: plotly, pandas, numpy
->location: code/visualizations/prediction_plot.py
->description: visualize the prediction infected/recovered number of people. The graph generated is interactive.
```

3. Comparation between diseases
```
->pacakge used: plotly, pandas, numpy
->data: data of fataitily and transimissionbility of diseases other than COVID-19 are from Internet
->location: code/visualizations/comparation_of_diseases.py
->description: visualize the comparation of fatality and transmission between differrent diseases. The graph generated is interactive.
```
4. Weibo-Word Cloud
```
->pacakge used: json,jieba.analyse,matplotlib,Image,WordCloud,numpy
->data: form data we get from code/scraper/weibo_scraper.py
->location: code/visualizations/weibo_cloud.py 
->description: for a given key word, create a word cloud shows the highly related words
```





