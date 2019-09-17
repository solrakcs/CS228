import matplotlib.pyplot as plt
from knn import KNN


knn = KNN()

knn.Load_Dataset('iris.csv')
x = knn.data[:, 0]
y = knn.data[:, 1]
plt.figure()
plt.scatter(x, y, c=knn.target)
plt.show()
