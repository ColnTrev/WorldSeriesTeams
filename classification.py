# importing data visualization and manipulation libraries
import pandas     as pd
import numpy      as np
import pylab      as pl
# importing machine learning data processing tools
from sklearn import preprocessing as skp
from sklearn.metrics         import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split
# importing models
from sklearn.svm            import SVC
from sklearn.ensemble       import AdaBoostClassifier         as ABC
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

X_train, X_test, Y_train, Y_test = train_test_split(f_adjust, l_data, test_size = 0.5, random_state = 0)

ada = ABC(n_estimators=150)
ada.fit(X_train, Y_train)
ada_results = ada.predict(X_test)
ada_cm = confusion_matrix(Y_test, ada_results)
print(accuracy_score(Y_test, ada_results))

poly = SVC(kernel='poly', decision_function_shape = 'ovr',C=1).fit(X_train, Y_train)
poly_results = poly.predict(X_test)
poly_cm = confusion_matrix(Y_test, poly_results)
print(accuracy_score(Y_test, poly_results))

pl.matshow(ada_cm)
pl.title('Confusion Matrix AdaBoost 50%')
pl.colorbar()
pl.show()

pl.matshow(poly_cm)
pl.title('Confusion Matrix Polynomial SVM 50%')
pl.colorbar()
pl.show()


