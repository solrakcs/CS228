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



def Handle_Frame():
	global x, y
	global xMin, xMax
	global yMin, yMax

	hand = frame.hands[0]
	fingers = hand.fingers
	print(fingers)
	


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
	frame = controller.frame()
	if not (frame.hands.is_empty > 0):
		 Handle_Frame()
	pygameWindow.Reveal()