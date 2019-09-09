import sys
sys.path.insert(0, "..")
import Leap
from pygameWindow import PYGAME_WINDOW
import random
import pygame

x = 540
y = 360

befValue = 0

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0 
yMax = -1000.0


def Handle_Vector_From_Leap(v):
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

def Handle_Bone(b):
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
	pygameWindow.Draw_Black_Line(pygameXBase, pygameYBase, pygameXTip, pygameYTip)
	



def Handle_Finger(finger):
	for b in range(4):
		Handle_Bone(b)
			


def Handle_Frame():
	global x, y
	global finger

	hand = frame.hands[0]
	#print (hand)
	fingers = hand.fingers
	length = len(fingers) 
	for i in range(length):
		finger = fingers[i]
		Handle_Finger(finger)
	#indexFingerList = fingers.finger_type(0)
	#indexFinger = indexFingerList[0]
	#distalPhalanx = indexFinger.bone(3)
	#print(distalPhalanx)
	#distalPhalanx = indexFinger.bone(3)
	#tip = distalPhalanx.next_joint
	#print(tip)
	#x = tip[0]
	#y = tip[1]
	#if (x < xMin):
	#	xMin = x
	#if (x > xMax):
	#	xMax = x
	#if (y > yMin):
	#	yMin = y
	#if (y < yMax):
	#	yMax = y


def Scale(value, minValue, maxValue, newMinValue, newMaxValue):

	global befValue

	if maxValue == minValue:
		return befValue

	percentage_scaling = (value - minValue) / (maxValue - minValue)
	befValue = ((newMaxValue - newMinValue) * percentage_scaling) + newMinValue
	return befValue



		

pygameWindow = PYGAME_WINDOW()

print(pygameWindow)

controller = Leap.Controller()

while True:

	#print pygameX
	#print pygameY
	pygameWindow.Prepare(pygameWindow)
	##Perturb_Circle_Position()
	#pygameWindow.Draw_Black_Circle(int(pygameX),int(pygameY))
	frame = controller.frame()
	for event in pygame.event.get(): #With this for loop pygame window do not crash
		if event.type == pygame.QUIT:
			sys.exit(0)
	if not (frame.hands.is_empty > 0):
		 Handle_Frame()
		 
	pygameWindow.Reveal()




    