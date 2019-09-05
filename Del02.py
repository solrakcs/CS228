import sys
sys.path.insert(0, "..")
import Leap

from pygameWindow import PYGAME_WINDOW
import random

x = 540
y = 360

xMin = 1000.0
xMax = -1000.0
yMin = -1000.0 #I switch the values of yMin and yMax and later on, I change the conditionals of y in the function Handle_Frame(), in order to move the black dot properly.
yMax = 1000.0

befValue = 0

#def Perturb_Circle_Position(): #I am not gonna include a velocity. 1 works well for me
#	global x, y
#
#	fourSidedDieRoll = random.randint(1, 4)
#	
#	if fourSidedDieRoll == 1:
#		x -= 1
#	elif fourSidedDieRoll == 2:
#		x += 1
#	elif fourSidedDieRoll == 3:
#		y -= 1
#	else:
#		y += 1


def Handle_Frame():
	#global x, y
	#global xMin, xMax
	#global yMin, yMax

	#hand = frame.hands[0]
	#print (hand)
	#fingers = hand.fingers
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

	#print xMax
	#print xMin
	#print yMax
	#print yMin
	pass


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
	pygameX = Scale(x, xMin, xMax, 0, 1080)
	pygameY = Scale(y, yMin, yMax, 0, 720)
	print pygameX
	print pygameY
	pygameWindow.Prepare(pygameWindow)
	##Perturb_Circle_Position()
	#pygameWindow.Draw_Black_Circle(int(pygameX),int(pygameY))
	frame = controller.frame()
	if not (frame.hands.is_empty > 0):
		 Handle_Frame()
	pygameWindow.Reveal()


