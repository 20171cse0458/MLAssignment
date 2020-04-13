import numpy as np 
import pandas as pd 
df=pd.read_csv("MLN.csv")


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
X=df[['ID']]
Y=df[['Weak Foot']]
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=1)
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
p1 = dt.predict([[5]])
p1[0]
