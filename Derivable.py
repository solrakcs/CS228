import sys
sys.path.insert(0, "..")
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW
import random
import pygame
import numpy as np

class DERIVABLE:

	global x, y, befValue, xMin, xMax, yMin, yMax, pygameWindow, controller, previousNumberofHands, currentNumberofHands

	x = 540
	y = 360
	befValue = 0
	xMin = 1000.0
	xMax = -1000.0
	yMin = 1000.0 
	yMax = -1000.0
	pygameWindow = PYGAME_WINDOW()
	controller = Leap.Controller()
	previousNumberofHands = 0
	currentNumberofHands = 0


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


	def Handle_Vector_From_Leap(self, v):
		global xMin, xMax, yMin, yMax
		global x, y
	
	
		x = v[0]
		y = v[2]

		if (x < xMin):
			xMin = x
		if (x > xMax):
			xMax = x
		if (y < yMin):
			yMin = y
		if (y > yMax):
			yMax = y

	def Scale(self, value, minValue, maxValue, newMinValue, newMaxValue):
	
		global befValue
	
		if maxValue == minValue:
			return befValue
	
		percentage_scaling = (value - minValue) / (maxValue - minValue)
		befValue = ((newMaxValue - newMinValue) * percentage_scaling) + newMinValue
		return befValue	

	def Handle_Bone(self, b, c):
		global bone
		global base, tip
	
		bone = finger.bone(b)
		base = bone.prev_joint
		tip = bone.next_joint
		self.Handle_Vector_From_Leap(base)
		pygameXBase = self.Scale(x, xMin, xMax, 0, 1080)
		pygameYBase = self.Scale(y, yMin, yMax, 0, 720)
		self.Handle_Vector_From_Leap(tip)
		pygameXTip = self.Scale(x, xMin, xMax, 0, 1080)
		pygameYTip = self.Scale(y, yMin, yMax, 0, 720)
		pygameWindow.Draw_Line(pygameXBase, pygameYBase, pygameXTip, pygameYTip, b, c)
		
	
	
	
	def Handle_Finger(self, finger, c):
		for b in range(4):
			self.Handle_Bone(b, c)
				
	
	
	def Handle_Frame(self):
		global x, y
		global finger, previousNumberofHands, currentNumberofHands

		previousNumberofHands = 0
		currentNumberofHands = 0

		hand = frame.hands[0]
		handList = frame.hands
		nHands = len(handList)
		if(nHands == 1):
			currentNumberofHands = 1
		if(nHands == 2):
			currentNumberofHands = 2
		fingers = hand.fingers
		length = len(fingers) 
		for i in range(length):
			finger = fingers[i]
			if(currentNumberofHands == 1 and previousNumberofHands == 0):
				self.Handle_Finger(finger, 1)
			if(currentNumberofHands == 2 and previousNumberofHands == 0):
				self.Handle_Finger(finger, 2)
			if(currentNumberofHands == 2 and previousNumberofHands == 1):
				self.Handle_Finger(finger, 2)
			if(currentNumberofHands == 2 and previousNumberofHands == 2):
				self.Handle_Finger(finger, 2)
			if(currentNumberofHands == 1 and previousNumberofHands == 2):
				self.Recording_Is_Ending()
				self.Handle_Finger(finger, 2)
			if(currentNumberofHands == 1 and previousNumberofHands == 1):
				self.Handle_Finger(finger, 1)

	

	def Run_Forever(self):

		while True:

			self.Run_Once()


	def Run_Once(self):

		global frame

		pygameWindow.Prepare(pygameWindow)
		frame = controller.frame()
		for event in pygame.event.get(): #With this for loop pygame window do not crash
			if event.type == pygame.QUIT:
				sys.exit(0)
		if not (frame.hands.is_empty > 0):
			 self.Handle_Frame()
			 
		pygameWindow.Reveal()


	def Recording_Is_Ending():
		print 'recording is ending'



