import matplotlib.pyplot as plt
from knn import KNN


knn = KNN()
knn.Load_Dataset('iris.csv')

x = knn.data[:, 0]
y = knn.data[:, 1]
trainX = knn.data[::2, 0:2]
trainy = knn.target[::2]
plt.figure()
plt.scatter(trainX[:, 0], trainX[:, 1], c=trainy)
plt.show()
