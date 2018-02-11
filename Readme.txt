This project is about to develop a model which can predict the popularity of a car based on some
predefined features about the car. Following points should be followed to succesfully develop the
model and prepare the prediction.csv file.

i). I have done the whole process on Jupyter notebook. So save the jupyter notebook file you are 
    working on in the same folder in which you have saved test and train data files named test.csv 
    and train.csv .
ii). Import necessary libraries like numpy, pandas .
iii). Import and fit the test and train data using pandas in proper format.
iv). Using sklearn import the KNN classifier . Fit it to train data and use it on predict data 
     for prediction.
v). Also import GridsearchCV from sklearn so as to optimize the classifier for optimization.
vi). Now convert the popularity array using pandas into prediction.csv file.