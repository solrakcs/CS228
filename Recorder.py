import sys
sys.path.insert(0, "..")
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW
import random
import pygame
import numpy as np
import pickle
import os
import shutil

class RECORDER:


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
		self.previousNumberofHands = 0
		self.currentNumberofHands = 0
		self.numberOfGestures = 100
		self.gestureIndex = 0
		self.gestureData = np.zeros((5,4,6,self.numberOfGestures),dtype='f')
		self.file = 0
		self.Delete_Create_Directory()
		


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

	def Handle_Bone(self, i, j, c):
		global bone
		global base, tip
	
		bone = finger.bone(j)
		base = bone.prev_joint
		tip = bone.next_joint
		self.Handle_Vector_From_Leap(base)
		pygameXBase = self.Scale(self.x, self.xMin, self.xMax, 0, 1080)
		pygameYBase = self.Scale(self.y, self.yMin, self.yMax, 0, 720)
		self.Handle_Vector_From_Leap(tip)
		pygameXTip = self.Scale(self.x, self.xMin, self.xMax, 0, 1080)
		pygameYTip = self.Scale(self.y, self.yMin, self.yMax, 0, 720)
		self.pygameWindow.Draw_Line(pygameXBase, pygameYBase, pygameXTip, pygameYTip, j, c)

		if self.currentNumberofHands == 2:
			self.gestureData[i,j,0,self.gestureIndex] = base[0]
 			self.gestureData[i,j,1,self.gestureIndex] = base[1]
 			self.gestureData[i,j,2,self.gestureIndex] = base[2]
 			self.gestureData[i,j,3,self.gestureIndex] = tip[0]
 			self.gestureData[i,j,4,self.gestureIndex] = tip[1]
 			self.gestureData[i,j,5,self.gestureIndex] = tip[2]	

		if self.currentNumberofHands == 2:

			print('gesture ' + str(self.gestureIndex) + ' stored.')
			self.gestureIndex = self.gestureIndex + 1
			if self.gestureIndex == self.numberOfGestures:
				print self.gestureData[:,:,:,0]
				print self.gestureData[:,:,:,99]
				exit()

	
	def Handle_Finger(self, i, c):
			for j in range(4):
				self.Handle_Bone(i, j, c)

				
	
	
	def Handle_Frame(self):
		global finger

		printed = 0

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
				self.Handle_Finger(i, 1)
			if(self.currentNumberofHands == 2):
				self.Handle_Finger(i, 2)
			if (self.Recording_Is_Ending() == True):
				print(self.gestureData)
				self.Save_Gesture()	
				self.file += 1

	

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

	def Save_Gesture(self):
		
		pickle_out = open("C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData\\gesture"+str(self.file)+".p","wb")
		pickle.dump(self.gestureData, pickle_out)
		pickle_out.close()

	def Delete_Create_Directory(self):

		shutil.rmtree('C:\\Users\\ruths\\Desktop\\2019_UVM_CS228_Castrejon_Carlos_Deliverable 4\\LeapSDK\\lib\\CS228\\userData')

		dirName = 'userData'
 		os.mkdir(dirName)
		