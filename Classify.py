import numpy as np 
import pickle



def Main():

	pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\train8.dat.p", "rb")
	train8 = pickle.load(pickle_in)
	print(train8)
	pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\train9.dat.p", "rb")
	train9 = pickle.load(pickle_in)
	print(train9)
	pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\test8.dat.p", "rb")
	test8 = pickle.load(pickle_in)
	print(test8)
	pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\test9.dat.p", "rb")
	test9 = pickle.load(pickle_in)
	print(test9)

def ReshapeData(set1,set2):
	X = np.zeros((2000,5*4*6),dtype='f')
	for row in range(0,1000):
		col = 0
		for j in range(0,5):
			for k in range(0,4):
				for m in range(0,6):
					X[row,col] = set1[j,k,m,row]
					col = col + 1
	return X
	trainX = ReshapeData(trainM,trainN)
	print trainX
	print trainX.shape



Main()