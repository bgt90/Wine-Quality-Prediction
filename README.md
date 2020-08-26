# Wine-Quality-Prediction
A Final Project for Purwadhika Data Scientist Course 

This Repository is about exploring and predicting red wine quality. The dataset used in this project can be found [here](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009)

The dataset consist of 11 input variables based on physicochmical analysis of red wines and 1 output variable.

The input variables are:
1.  **Fixed acidity** : Non volatile acid. Tartaric, malic, citric, and succinic are the most common to be found in wines
2.  **Volatile acidity** : Volatile acid. Acetic acid is one of them, and is unwanted in wine due to unpleasant odors
3.  **citric acid** : One of the fixed acid in wine, commonly found in citrus. Has a refreshing taste
4.  **residual sugar** : The remaining sugar content in wine after fermentation. less than 1 g. liter is uncommon
5.  **chlorides** : indicator for the amount of salt in wine. Too high of chloride usually means salty taste than can deter consumers
6.  **free sulfur dioxide** : Free form of SO2. SO2 concentration more that 50ppm can affect wine taste as a rotten egg smell is a signature of SO2 gas
7.  **total sulfur dioxide** : The total amount of SO2, bound and free. A small amount of sulfur dioxide is important as antimicrobial agent in wine
8.  **density** : the density of the liquid. The density of water is close to one. Alcohol concentration, sugar content and otther dissolved compounds affect density
9.  **pH** : The power of hydrogen, commonly used as acidity scale, with 7 as neutral, below 7 indicate acidity and above 7 indicate basicity. Most wines pH are between 3-4 on the pH scale
10.  **sulphates** : Sulfur based additive used as antimicrobial and anti-oxidant agent. Contribute to SO2 levels
11.  **alcohol** : The alcohol content in wine. It level depends of the initial sudar content before fermentation and the yeast used for fermentation.

The output variable is:  
12. **quality** : Based on sensory test. The score  is between 0 and 10.


The files in this respositories consist of:
1. The EDA of the wine quality dataset
2. Preprocessing. Which mainly about outliers handling
3. Model selections. The models used are all regression and regressor models
4. A folder for HTML based dashboard by Flask library
