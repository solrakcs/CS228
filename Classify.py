import numpy as np 
import pickle
from knn import KNN


pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\train8.dat.p", "rb")
train8 = pickle.load(pickle_in)
pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\train9.dat.p", "rb")
train9 = pickle.load(pickle_in)
pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\test8.dat.p", "rb")
test8 = pickle.load(pickle_in)
pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\test9.dat.p", "rb")
test9 = pickle.load(pickle_in)



def ReshapeData(set1,set2):
	X = np.zeros((2000,5*4*6),dtype='f')
	y = np.zeros(2000, dtype = 'f')
	for row in range(0,1000):
		y[row] = 8
		y[row+1000] = 9
		col = 0
		for j in range(0,5):
			for k in range(0,4):
				for m in range(0,6):
					X[row,col] = set1[j,k,m,row]
					X[row+1000, col] = set2[j,k,m,row]
					col = col + 1

	return X, y


trainX, trainy = ReshapeData(train8, train9)
#print trainX
#print trainX.shape
#print trainy
#print trainy.shape

testX, testy = ReshapeData(test8, test9)
#print testX
#print testX.shape
#print testy
#print testy.shape



knn = KNN()
knn.Use_K_Of(15)

knn.Fit(trainX,trainy)
counter = 0
for row in range(0,2000):
	prediction = int(knn.Predict(testX[row]))
	actualClass = int(testy[row])

	if(actualClass == prediction):
		counter += 1

print(counter)
percentage = (float(counter)/float(2000))*100
print(percentage)
	


