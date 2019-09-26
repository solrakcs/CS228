import numpy as np 
import pickle



def Main():

	pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\gesture0.p", "rb")
	gestureData = pickle.load(pickle_in)
	print(gestureData.shape)


Main()