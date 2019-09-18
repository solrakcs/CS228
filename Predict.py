import matplotlib.pyplot as plt
from knn import KNN
import numpy as np


knn = KNN()
knn.Load_Dataset('iris.csv')

x = knn.data[:, 0]
y = knn.data[:, 1]
trainX = knn.data[::2, 0:2]
testX = knn.data[1::2, 0:2]
trainy = knn.target[1::2]

colors = np.zeros((3,3),dtype='f')
colors[0,:] = [1,0.5,0.5]
colors[1,:] = [0.5,1,0.5]
colors[2,:] = [0.5,0.5,1]

plt.figure()

#plt.scatter(trainX[:, 0], trainX[:, 1], c=trainy)
#plt.scatter(testX[:, 0], testX[:, 1], c=trainy)

[numItems,numFeatures] = knn.data.shape
for i in range(0,numItems/2):
	itemClass = int(trainy[i])
	currColor = colors[itemClass,:]
	plt.scatter(trainX[i,0],trainX[i,1], facecolor=currColor, s=50, lw=2)

plt.show()
