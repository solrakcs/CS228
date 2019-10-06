import numpy as np 
import pickle
from knn import KNN




pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable_5\\LeapSDK\\lib\\CS228\\Del6\\userData\\train8.dat.p", "rb")
train8 = pickle.load(pickle_in)
pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable_5\\LeapSDK\\lib\\CS228\\Del6\\userData\\train9.dat.p", "rb")
train9 = pickle.load(pickle_in)
pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable_5\\LeapSDK\\lib\\CS228\\Del6\\userData\\test8.dat.p", "rb")
test8 = pickle.load(pickle_in)
pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable_5\\LeapSDK\\lib\\CS228\\Del6\\userData\\test9.dat.p", "rb")
test9 = pickle.load(pickle_in)

def ReshapeData(set1,set2):
	X = np.zeros((2000,5*2*3),dtype='f')
	y = np.zeros(2000, dtype = 'f')
	for row in range(0,1000):
		y[row] = 8
		y[row+1000] = 9
		col = 0
		for j in range(0,5):
			for k in range(0,2):
				for m in range(0,3):
					X[row,col] = set1[j,k,m,row]
					X[row+1000, col] = set2[j,k,m,row]
					col = col + 1

	return X, y



def ReduceData(X):
	X = np.delete(X,1,1)
	X = np.delete(X,1,1)
	X = np.delete(X,0,2)
	X = np.delete(X,0,2)
	X = np.delete(X,0,2)

def CenterData(X):

	allXCoordinates = X[:,:,0,:]	
	meanValue = allXCoordinates.mean()
	X[:,:,0,:] = allXCoordinates - meanValue
	allYCoordinates = X[:,:,1,:]	
	meanValue = allYCoordinates.mean()
	X[:,:,1,:] = allYCoordinates - meanValue
	allZCoordinates = X[:,:,2,:]	
	meanValue = allZCoordinates.mean()
	X[:,:,2,:] = allZCoordinates - meanValue
	return X


ReduceData(train8)
ReduceData(train9)
ReduceData(test8)
ReduceData(test9)
CenterData(train8)
CenterData(train9)
CenterData(test8)
CenterData(test9)


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
	
pickle.dump(knn, open('userData/classifier.p','wb'))


