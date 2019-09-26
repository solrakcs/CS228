import pickle
import os
import pygame
import sys
import time

class READER:

	def __init__(self, pygameWindow):

		self.Determine_Num_Gestures()
		self.pygameWindow = pygameWindow

	def Determine_Num_Gestures(self):

		path, dirs, files = next(os.walk('userData'))
		self.numGestures = len(files)

	def Print_Gestures(self):
		
		for i in range(0, self.numGestures):
			pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\gesture"+str(i)+".p", "rb")
			gestureData = pickle.load(pickle_in)
			print("\n")
			print (gestureData)

	def Draw_Gestures(self):
		
		while True:

			self.Draw_Each_Gesture_Once()

	def Draw_Each_Gesture_Once(self):

		for event in pygame.event.get(): #With this for loop pygame window do not crash
			if event.type == pygame.QUIT:
				sys.exit(0)

		for x in range(0, self.numGestures-4, 5):

			self.pygameWindow.Prepare(self.pygameWindow)
			self.Draw_Gesture(x)
			self.pygameWindow.screen.fill((255, 255, 255))
			self.Draw_Gesture(x+1)
			self.pygameWindow.screen.fill((255, 255, 255))
			self.Draw_Gesture(x+2)
			self.pygameWindow.screen.fill((255, 255, 255))
			self.Draw_Gesture(x+3)
			self.pygameWindow.screen.fill((255, 255, 255))
			self.Draw_Gesture(x+4)
			self.pygameWindow.Reveal()
			time.sleep(0.5)


	def Draw_Gesture(self, x):
		
		pickle_in = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 3\\LeapSDK\\lib\\CS228\\userData\\gesture"+str(x)+".p", "rb")
		gestureData = pickle.load(pickle_in)

		for i in range(5):
			for j in range(4):

 				xBaseNotYetScaled = -gestureData[i, j, 0]
 				yBaseNotYetScaled = -gestureData[i, j, 2]
 				xTipNotYetScaled = -gestureData[i, j, 3]
 				yTipNotYetScaled = -gestureData[i, j, 5]

 				xBase = self.Scale(xBaseNotYetScaled, 1000.0, -1000.0, 0, 1080)
 				yBase = self.Scale(yBaseNotYetScaled, 1000.0, -1000.0, 0, 720)
 				xTip = self.Scale(xTipNotYetScaled, 1000.0, -1000.0, 0, 1080)
 				yTip = self.Scale(yTipNotYetScaled, 1000.0, -1000.0, 0, 720)

 				self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, 5, 3)


	def Scale(self, value, minValue, maxValue, newMinValue, newMaxValue):
	
		if maxValue == minValue:
			return self.befValue
	
		percentage_scaling = (value - minValue) / (maxValue - minValue)
		self.befValue = ((newMaxValue - newMinValue) * percentage_scaling) + newMinValue
		return self.befValue