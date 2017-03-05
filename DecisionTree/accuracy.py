import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData
from sklearn import tree
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()



#################################################################################
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
########################## DECISION TREE #################################



#### your code goes here


from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test,pred)
### be sure to compute the accuracy on the test set


    
def submitAccuracies():
  return {"acc":round(acc,3)}

