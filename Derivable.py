import sys
sys.path.insert(0, "..")
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW
import random
import pygame

class DERIVABLE:

	def __init__(self):

		self.pygameWindow = PYGAME_WINDOW()
		self.controller = Leap.Controller()
		
		self.x = 540
		self.y = 360

		self.befValue = 0

		self.xMin = 1000.0
		self.xMax = -1000.0
		self.yMin = 1000.0 
		self.yMax = -1000.0


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

	def Handle_Bone(self, b):
		global bone
		global base, tip
	
		bone = finger.bone(b)
		base = bone.prev_joint
		tip = bone.next_joint
		Handle_Vector_From_Leap(base)
		pygameXBase = Scale(x, xMin, xMax, 0, 1080)
		pygameYBase = Scale(y, yMin, yMax, 0, 720)
		Handle_Vector_From_Leap(tip)
		pygameXTip = Scale(x, xMin, xMax, 0, 1080)
		pygameYTip = Scale(y, yMin, yMax, 0, 720)
		pygameWindow.Draw_Black_Line(pygameXBase, pygameYBase, pygameXTip, pygameYTip, b)
		
	
	
	
	def Handle_Finger(self, finger):
		for b in range(4):
			Handle_Bone(b)
				
	
	
	def Handle_Frame(self):
		global x, y
		global finger
	
		hand = frame.hands[0]
		fingers = hand.fingers
		length = len(fingers) 
		for i in range(length):
			finger = fingers[i]
			Handle_Finger(finger)
	
	
	def Scale(self, value, minValue, maxValue, newMinValue, newMaxValue):
	
		global befValue
	
		if maxValue == minValue:
			return befValue
	
		percentage_scaling = (value - minValue) / (maxValue - minValue)
		befValue = ((newMaxValue - newMinValue) * percentage_scaling) + newMinValue
		return befValue

	def Run_Forever(self):

		while True:

			Run_Once()
	

	def Run_Once(self):
		pygameWindow.Prepare(pygameWindow)
		frame = controller.frame()
		for event in pygame.event.get(): #With this for loop pygame window do not crash
			if event.type == pygame.QUIT:
				sys.exit(0)
		if not (frame.hands.is_empty > 0):
			 Handle_Frame()
		 
		pygameWindow.Reveal()