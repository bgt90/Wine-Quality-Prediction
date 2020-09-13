# Wine-Quality-Prediction
A Final Project for Purwadhika Data Scientist Course 

This Repository is about exploring and predicting red wine quality. The dataset used in this project can be found [here](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009)

The dataset consist of 11 input variables based on physicochmical analysis of red wines and 1 output variable.

The input variables are:
1.  **Fixed acidity** (g tartaric acid/dm3) : Non volatile acid. Tartaric, malic, citric, and succinic are the most common to be found in wines
2.  **Volatile acidity** (g acetic acid/dm3) : Volatile acid. Acetic acid is one of them, and is unwanted in wine due to unpleasant odors
3.  **citric acid** (g/dm3) : One of the fixed acid in wine, commonly found in citrus. Has a refreshing taste
4.  **residual sugar** (g/dm3) : The remaining sugar content in wine after fermentation. less than 1 g. liter is uncommon
5.  **chlorides** (g sodium chloride/dm3) : indicator for the amount of salt in wine. Too high of chloride usually means salty taste than can deter consumers
6.  **free sulfur dioxide** (mg/dm3) : Free form of SO2. SO2 concentration more that 50ppm can affect wine taste as a rotten egg smell is a signature of SO2 gas
7.  **total sulfur dioxide** (mg/dm3) : The total amount of SO2, bound and free. A small amount of sulfur dioxide is important as antimicrobial agent in wine
8.  **density** (g/dm3) : the density of the liquid. The density of water is close to one. Alcohol concentration, sugar content and otther dissolved compounds affect density
9.  **pH** : The power of hydrogen, commonly used as acidity scale, with 7 as neutral, below 7 indicate acidity and above 7 indicate basicity. Most wines pH are between 3-4 on the pH scale
10.  **sulphates** (g potassium sulphate/dm3): Sulfur based additive used as antimicrobial and anti-oxidant agent. Contribute to SO2 levels
11.  **alcohol** (%) : The alcohol content in wine. It level depends of the initial sudar content before fermentation and the yeast used for fermentation.

The output variable is:  
12. **quality** : Based on sensory test. The score  is between 0 and 10.


The steps I took to do the predictions are: 
1. Exploratory data analysis
2. Preprocessing. Which mainly about outliers handling
3. Model selections. The models used are all regression and regressor models
4. Deployment with flask.

## Model Selection Results

The best model evaluation (least RMSE and highest R square) was actually with Random Forest Regressor, but Random Forest result cannot be extrapolated, therefore, I use Ridge regression instead, a model known for handling multicoliearity, which is prevalent in my data. The best data set was after dropping outliers, with **initial RMSE 10.62% and R square 0.35**. 

I did Hyperparameter tunning, with result as the following:

> {'alpha': 0.5, 'fit_intercept': True, 'max_iter': None, 'solver': 'sparse_cg'}

The tunning results improved the model to **RMSE 10.57 and R square0.36**.

## Dashboard

Flask was used to create the dashboard. There are 5 pages:

### 1. Home


![alt text](https://github.com/bgt90/Wine-Quality-Prediction/blob/master/home.png)

### 2. Prediction

![alt text](https://github.com/bgt90/Wine-Quality-Prediction/blob/master/prediction.png)

### 3. Result

![alt text](https://github.com/bgt90/Wine-Quality-Prediction/blob/master/result.png)

### 4. Dataset

![alt text](https://github.com/bgt90/Wine-Quality-Prediction/blob/master/dataset.png)

### 5. Visualisation

![alt text](https://github.com/bgt90/Wine-Quality-Prediction/blob/master/visualisation.png)



