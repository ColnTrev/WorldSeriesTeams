
# importing data visualization and manipulation libraries
import pandas     as pd
import numpy      as np
import matplotlib.pyplot as plt

# importing machine learning data processing tools
from sklearn import preprocessing as skp
from sklearn import metrics
from sklearn.model_selection import cross_val_score, train_test_split
# importing models
from sklearn.svm            import SVC
from sklearn.neighbors      import KNeighborsClassifier       as KNC
from sklearn.ensemble       import GradientBoostingClassifier as GBC
from sklearn.ensemble       import AdaBoostClassifier         as ABC
# parsing command line args

#importing dataset
attr_list = ['win_percent','ab','bb','e','er','era','fp','h','ha','hr','hra','run_diff','so','soa','double','triple']
feat      = pd.read_csv('features.csv')
labels    = pd.read_csv('labels.csv')

# converting the dataset to a numpy array to work with scikit learn algos
f_data  = np.array(feat)[:,1:]
l_data  = np.array(labels)[:,1:]


# scale centered on zero
f_adjust = skp.scale(f_data)
# formatting labels to the right format
l_data = l_data.ravel()
scoring = 'accuracy'
cv = 30
models = [('GradientTree', GBC(n_estimators=100, learning_rate=1.0)), 
          ('Linear', SVC(kernel='linear', C=1)), 
          ('Polynomial', SVC(kernel='poly', C=1)),
          ('AdaBoost', ABC(n_estimators=150)),
          ('KNN', KNC(algorithm='ball_tree'))]
means = []
error = []
names = []
X_train, X_test, Y_train, Y_test = train_test_split(f_adjust, l_data, test_size = 0.5, random_state = 0)
for name, model in models:
    score = cross_val_score(model,X_train, Y_train, cv = cv, scoring=scoring)
    means.append(score.mean())
    error.append(score.std())
    names.append(name)
    print("Model: " + name + " Mean: " + str(score.mean()) + " Standard Deviation: " + str(score.std()))
width = 0.35
index = np.arange(5)
figure = plt.figure()
figure.suptitle('Test Harness Results')
ax = figure.add_subplot(111)
plt.bar(np.arange(5), means, width)
ax.set_xticks(index)
ax.set_xticklabels(names)
plt.show()