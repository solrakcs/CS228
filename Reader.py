import pickle
import os

class READER:

	def __init__(self):

		self.Determine_Num_Gestures()

	def Determine_Num_Gestures(self):

		path, dirs, files = next(os.walk('userData'))
		self.numGestures = len(files)

	def Print_Gestures(self):
		
		for i in range(0, self.numGestures):
			pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 3\\LeapSDK\\lib\\CS228\\userData\\gesture"+str(i)+".p", "rb")
			gestureData = pickle.load(pickle_in)
			print("\n")
			print (gestureData)