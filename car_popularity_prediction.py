
# coding: utf-8

# In[10]:


# Import libraries necessary for this project
import numpy as np
import pandas as pd
from time import time
from IPython.display import display # Allows the use of display() for DataFrames

get_ipython().magic(u'matplotlib inline')
# Load the car popularity train data
train_data = pd.read_csv("train.csv")
test_data=pd.read_csv("test.csv")
# Success - Display the first record

display(train_data.head(n=10))
display(test_data.head(n=10))


# In[17]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.grid_search import GridSearchCV
import numpy as np
import pandas as pd
X_train= train_data.iloc[0:,0:6]
y_train= train_data['popularity']
X_test= test_data
clf = KNeighborsClassifier()
parameters = {"n_neighbors": np.arange(1, 31, 2),
               "metric": ["euclidean", "cityblock"],
                "weights": ['distance']}

grid_obj = GridSearchCV(clf, parameters)
grid_fit = grid_obj.fit(X_train,y_train)
best_clf = grid_fit.best_estimator_
predictions = (clf.fit(X_train, y_train)).predict(X_test)
best_predictions = best_clf.predict(X_test)
popularity= np.array(best_predictions)[np.newaxis]
df = pd.DataFrame(popularity.T)
df.to_csv("prediction.csv",index=False, header=None)


