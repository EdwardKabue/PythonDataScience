import pandas as pd
import sklearn.model_selection as skm
import sklearn.linear_model as skl
from sklearn import metrics
import numpy as np

df_adv_data = pd.read_csv("Advertising.csv", index_col=0)

#print(df_adv_data.head())

# print(df_adv_data.size) #get the size of the data set

# print(df_adv_data.shape) #get the shape of the data set

# print(df_adv_data.columns) #get the columns of the data set

#create a feature object from 3 of the columns
X_feature = df_adv_data[["Newspaper", "Radio", "TV"]]

# print(X_feature.head())

#create target object based on Sales column of data set
Y_target = df_adv_data[["Sales"]]
# print(Y_target.head())

#split training and test data.
#by default 75% becomes training data and 25% test data.
x_train, x_test, y_train, y_test = skm.train_test_split(X_feature, Y_target, random_state=1)

#View the shape of the training and test data sets for both feature and response.
# print("Y train shape", y_train.shape)
# print("X train shape", x_train.shape)
# print("X test shape", x_test.shape)
# print("Y test shape", y_test.shape)

#linear regression model
linreg = skl.LinearRegression()

linreg.fit(x_train, y_train)

#print the intercept and coefficients
# print(linreg.intercept_)
# print(linreg.coef_)

#prediction
y_pred = linreg.predict(x_test)
print(y_pred)

#Calculate the mean square error (MSE)
print(np.sqrt(metrics.mean_squared_error(y_test,y_pred)))