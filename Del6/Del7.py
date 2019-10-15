import sys
sys.path.insert(0, "../..")
import Leap
from pygameWindow import PYGAME_WINDOW
import random
import pygame
import pickle
import numpy as np
import threading 



x = 540
y = 360

befValue = 0

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0 
yMax = -1000.0 

programState = 0

counter = 0


clf = pickle.load(open('userData/classifier.p','rb'))
testData = np.zeros((1,30),dtype='f')



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


def UserSignCorrectly():
	global testData, counter

	testData = CenterData(testData)
	predictedClass = clf.Predict(testData)
	print(predictedClass)
	if predictedClass == 1:
		counter = counter + 1
		print(predictedClass)


def HandleState3():
	global counter
	background = pygame.image.load('background.png')
	pygameWindow.Draw_Image(background, 550, 15)
	task_completed = pygame.image.load('task_completed.png')
	pygameWindow.Draw_Image(task_completed, (1080/1.7), 90)
	counter = 0
	CheckIfCentered()


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
	global pygameXBase, pygameYBase, pygameXTip, pygameYTip
	global programState

	bone = finger.bone(b)
	base = bone.prev_joint
	tip = bone.next_joint
	Handle_Vector_From_Leap(base)
	pygameXBase = Scale(x, xMin, xMax, 0, 1080/2)
	pygameYBase = Scale(y, yMin, yMax, 0, 720/2)
	Handle_Vector_From_Leap(tip)
	pygameXTip = Scale(x, xMin, xMax, 0, 1080/2)
	pygameYTip = Scale(y, yMin, yMax, 0, 720/2)
	if(programState == 1):
		pygameWindow.Draw_Black_Line(pygameXBase, pygameYBase, pygameXTip, pygameYTip, b, 0)
	elif(programState == 2):
		pygameWindow.Draw_Black_Line(pygameXBase, pygameYBase, pygameXTip, pygameYTip, b, 1)


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
	global counter 
	global programState

	k = 0

	hand = frame.hands[0]
	fingers = hand.fingers
	for i in range(0, 5):
		finger = fingers[i]
		Handle_Finger(finger)

	if(programState == 2):

		background = pygame.image.load('background.png')
		pygameWindow.Draw_Image(background, 550, 0)
		number1 = pygame.image.load('Number1.png')
		pygameWindow.Draw_Image(number1, 540, 50)
		Capture1 = pygame.image.load('Captura1.png')
		pygameWindow.Draw_Image(Capture1, 550, 370)

		UserSignCorrectly()
		if counter == 10:
			programState = 3



def Scale(value, minValue, maxValue, newMinValue, newMaxValue):

	global befValue

	if maxValue == minValue:
		return befValue

	percentage_scaling = (value - minValue) / (maxValue - minValue)
	befValue = ((newMaxValue - newMinValue) * percentage_scaling) + newMinValue
	return befValue


def DrawImageToHelpUserPutTheirHandOverTheDevice():
	userInit = pygame.image.load('userInit.png')
	pygameWindow.Draw_Image(userInit, (1080/2)+5, 0)


def HandOverDevice():
	if not (frame.hands.is_empty > 0):
		return True


def CheckIfCentered():
	global pygameXBase, pygameYBase
	global programState

	if pygameXBase >= 150 and pygameXBase <= 400 and pygameYBase >= 120 and pygameYBase <= 200:
		programState = 2
	else:
		programState = 1


def HandleState0():
	global programState

	DrawImageToHelpUserPutTheirHandOverTheDevice()
	if HandOverDevice():
		programState = 1


def HandleState1():
	global programState

	if not (frame.hands.is_empty > 0):
		 userCenter = pygame.image.load('userCenter.png')
		 pygameWindow.Draw_Image(userCenter, (1080/1.7), 90)
		 Handle_Frame(frame)

	else:
		programState = 0


def HandleState2():
	global programState, frame
	
	if not (frame.hands.is_empty > 0):
		Handle_Frame(frame)
	else:
		programState = 0


pygameWindow = PYGAME_WINDOW()

print(pygameWindow)

controller = Leap.Controller()

while True:

	pygameWindow.Prepare(pygameWindow)
	frame = controller.frame()
	pygameWindow.Draw_Black_Circle(0, 0)
	pygameWindow.Split_Black_Line(0, 720/2, 1080, 720/2)
	pygameWindow.Split_Black_Line(1080/2, 0, 1080/2, 720)

	for event in pygame.event.get(): #With this for loop pygame window do not crash
		if event.type == pygame.QUIT:
			sys.exit(0)

	if programState == 0:
		HandleState0()
	elif programState == 1:		
		HandleState1()
		CheckIfCentered()
	elif programState == 2:
		HandleState2()
	elif programState == 3:
		HandleState3()
		 
	pygameWindow.Reveal()