import sys
sys.path.insert(0, "..")
import Leap

#from pygameWindow import PYGAME_WINDOW
#import random

#x = 540
#y = 360

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
#

def Handle_Frame():
	hand = frame.hands[0]
	print (hand)
	fingers = hand.fingers
	indexFingerList = fingers.finger_type(0)
	indexFinger = indexFingerList[0]
	print(indexFinger)
#
#
#pygameWindow = PYGAME_WINDOW()

#print(pygameWindow)

controller = Leap.Controller()

while True:
#	pygameWindow.Prepare(pygameWindow)
#	Perturb_Circle_Position()
#	pygameWindow.Draw_Black_Circle(x,y)
	frame = controller.frame()
	if not (frame.hands.is_empty > 0):
		 Handle_Frame()

#	pygameWindow.Reveal()

