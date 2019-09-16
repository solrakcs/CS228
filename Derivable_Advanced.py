import sys
sys.path.insert(0, "..")
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW
import random
import pygame
import numpy as np
import pickle

class DERIVABLE:


	def __init__(self, pygameWindow, controller, x, y, befValue, xMin, xMax, yMin, yMax):

		self.pygameWindow = pygameWindow
		self.controller = controller
		self.x = x
		self.y = y
		self.befValue = befValue
		self.xMin = xMin
		self.xMax = xMax
		self.yMin = yMin
		self.yMax = yMax
		self.gestureData = np.zeros((5,4,6),dtype=’f’)
		self.file = 0


	def Handle_Vector_From_Leap(self, v):
	
		self.x = v[0]
		self.y = v[2]

		if (self.x < self.xMin):
			self.xMin = self.x
		if (self.x > self.xMax):
			self.xMax = self.x
		if (self.y < self.yMin):
			self.yMin = self.y
		if (self.y > self.yMax):
			self.yMax = self.y

	def Scale(self, value, minValue, maxValue, newMinValue, newMaxValue):
	
		if maxValue == minValue:
			return self.befValue
	
		percentage_scaling = (value - minValue) / (maxValue - minValue)
		self.befValue = ((newMaxValue - newMinValue) * percentage_scaling) + newMinValue
		return self.befValue	

	def Handle_Bone(self, b, c):
		global bone
		global base, tip
	
		bone = finger.bone(b)
		base = bone.prev_joint
		tip = bone.next_joint
		self.Handle_Vector_From_Leap(base)
		pygameXBase = self.Scale(self.x, self.xMin, self.xMax, 0, 1080)
		pygameYBase = self.Scale(self.y, self.yMin, self.yMax, 0, 720)
		self.Handle_Vector_From_Leap(tip)
		pygameXTip = self.Scale(self.x, self.xMin, self.xMax, 0, 1080)
		pygameYTip = self.Scale(self.y, self.yMin, self.yMax, 0, 720)
		self.pygameWindow.Draw_Line(pygameXBase, pygameYBase, pygameXTip, pygameYTip, b, c)
		if self.Recording_Is_Ending():
			self.gestureData[i,j,0] = (x coordinate of the base of bone j in finger i)
	 		self.gestureData[i,j,1] = (y coordinate of the base of bone j in finger i)
	 		self.gestureData[i,j,2] = (z coordinate of the base of bone j in finger i)
	 		self.gestureData[i,j,3] = (x coordinate of the tip of bone j in finger i)
	 		self.gestureData[i,j,4] = (y coordinate of the tip of bone j in finger i)
	 		self.gestureData[i,j,5] = (z coordinate of the tip of bone j in finger i)

	 		self.file += 1
		
	
	
	
	def Handle_Finger(self, finger, c):
		for b in range(4):
			self.Handle_Bone(b, c)
				
	
	
	def Handle_Frame(self):
		global finger

		self.previousNumberofHands = 0
		self.currentNumberofHands = 0

		hand = frame.hands[0]
		handList = frame.hands
		nHands = len(handList)
		if(nHands == 1):
			self.currentNumberofHands = 1
		if(nHands == 2):
			self.currentNumberofHands = 2
		fingers = hand.fingers
		length = len(fingers) 
		for i in range(length):
			finger = fingers[i]
			if(self.currentNumberofHands == 1):
				self.Handle_Finger(finger, 1)
			if(self.currentNumberofHands == 2):
				self.Handle_Finger(finger, 2)
			if self.Recording_Is_Ending():
				print(self.gestureData)
				self.Save_Gesture()

	

	def Run_Forever(self):


		while True:

			self.Run_Once()


	def Run_Once(self):

		global frame

		self.pygameWindow.Prepare(self.pygameWindow)
		frame = self.controller.frame()
		for event in pygame.event.get(): #With this for loop pygame window do not crash
			if event.type == pygame.QUIT:
				sys.exit(0)
		if not (frame.hands.is_empty > 0):
			 self.Handle_Frame()
			 self.previousNumberofHands = self.currentNumberofHands
			 
		self.pygameWindow.Reveal()


	def Recording_Is_Ending(self):
		if(self.currentNumberofHands == 1 and self.previousNumberofHands == 2):
			return True

	def Self.Gesture(self):
		
		pickle_out = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 2\\LeapSDK\\lib\\CS228\\userData\\gesture"+self.file+".p","wt")
		pickle.dump(self.gestureData, pickle_out)
		pickle_out.close()


