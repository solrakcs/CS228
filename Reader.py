import pickle

class READER:

	def __init__(self):

		pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 3\\LeapSDK\\lib\\CS228\\userData\\gesture.p", "rb")
		gestureData = pickle.load(pickle_in)
		print gestureData