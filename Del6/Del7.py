import sys
sys.path.insert(0, "../..")
import Leap
from pygameWindow import PYGAME_WINDOW
import random
import pygame
import pickle
import numpy as np


x = 540
y = 360

befValue = 0

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0 
yMax = -1000.0 


#clf = pickle.load(open('userData/classifier.p','rb'))
#testData = np.zeros((1,30),dtype='f')



def CenterData(X):

	allXCoordinates = X[0,::3]
	meanValue = allXCoordinates.mean()
	X[0,::3] = allXCoordinates - meanValue
	allYCoordinates = X[0,1::3]	
	meanValue = allYCoordinates.mean()
	X[0,1::3] = allYCoordinates - meanValue
	allZCoordinates = X[0,2::3]	
	meanValue = allZCoordinates.mean()
	X[0,2::3] = allZCoordinates - meanValue
	return X


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

def Handle_Bone(finger, b):
	global bone
	global base, tip
	global testData
	global k

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

	if ((b==0) or (b==3)):
		testData[0,k] = tip[0]
		testData[0,k+1] = tip[1]
		testData[0,k+2] = tip[2]
		k = k + 3
	



def Handle_Finger(finger):
	for b in range(0, 4):
		Handle_Bone(finger, b)
			


def Handle_Frame(frame):
	global testData
	global k

	k = 0

	hand = frame.hands[0]
	fingers = hand.fingers
	for i in range(0, 5):
		finger = fingers[i]
		Handle_Finger(finger)

	##print(testData)
	#testData = CenterData(testData)
	#predictedClass = clf.Predict(testData)
	#print(predictedClass)


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

	pygameWindow.Prepare(pygameWindow)
	frame = controller.frame()
	for event in pygame.event.get(): #With this for loop pygame window do not crash
		if event.type == pygame.QUIT:
			sys.exit(0)
	if not (frame.hands.is_empty > 0):
		 Handle_Frame(frame)
		 
	pygameWindow.Reveal()