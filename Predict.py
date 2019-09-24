import matplotlib.pyplot as plt
from knn import KNN
import numpy as np


knn = KNN()
knn.Load_Dataset('iris.csv')

x = knn.data[:, 0]
y = knn.data[:, 1]
trainX = knn.data[::2, 1:3]
testX = knn.data[1::2, 1:3]
trainy = knn.target[::2]
testy = knn.target[1::2]

knn.Use_K_Of(15)
knn.Fit(trainX,trainy)
for i in range(75):
	actualClass = testy[i]
	prediction = knn.Predict(testX[i,:])
	print(actualClass, prediction)

colors = np.zeros((3,3),dtype='f')
colors[0,:] = [1,0.5,0.5]
colors[1,:] = [0.5,1,0.5]
colors[2,:] = [0.5,0.5,1]

plt.figure()

plt.scatter(trainX[:, 0], trainX[:, 1], c=trainy)
plt.scatter(testX[:, 0], testX[:, 1], c=trainy)

[numItems,numFeatures] = knn.data.shape
for i in range(0,numItems/2):
	itemClass = int(trainy[i])
	currColor = colors[itemClass,:]
	plt.scatter(trainX[i,0],trainX[i,1], facecolor=currColor, s=50, lw=2)

correct = 0
for i in range(0,numItems/2):
	itemClass = int(testy[i])
	currColor = colors[itemClass,:]
	prediction = int( knn.Predict( testX[i,:] ) )
 	edgeColor = colors[prediction,:]
	plt.scatter(testX[i,0],testX[i,1], facecolor=currColor, s=50, lw=2, edgecolor=edgeColor)
	if(itemClass == prediction):
		correct = correct + 1
print(correct)
percentage = (float(correct)/float(75))*100
print(percentage)


plt.show()
