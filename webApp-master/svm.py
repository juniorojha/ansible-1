import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
import random

dataset_1 = pd.read_csv('FeatureDictionary.csv')

#dataset_1.info()

X= dataset_1.iloc[:,0:15]
Y= dataset_1.iloc[:,15]

random.seed( 30 )

from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
Xm = sc.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test,Y_train, Y_test = train_test_split(Xm, Y, test_size=0.1)




from sklearn.svm import SVC
classifier=SVC(kernel ='rbf',C=4.01, gamma=0.11 )#C=4.01, gamma=0.1133   #C=18.047, gamma=0.18047
classifier.fit(X_train, Y_train)

y_pred= classifier.predict(X_test)


from sklearn.model_selection import cross_val_score
scores = cross_val_score(classifier, Xm, Y, cv=10)
print(sum(scores)/len(scores))
print(scores)


from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, y_pred))