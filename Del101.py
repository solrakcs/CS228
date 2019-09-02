import sys
sys.path.insert(0, "..")
import Leap

from pygameWindow import PYGAME_WINDOW
import random

x = 540
y = 360

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
	global x, y

	hand = frame.hands[0]
	print (hand)
	fingers = hand.fingers
	indexFingerList = fingers.finger_type(0)
	indexFinger = indexFingerList[0]
	distalPhalanx = indexFinger.bone(3)
	print(distalPhalanx)
	distalPhalanx = indexFinger.bone(3)
	tip = distalPhalanx.next_joint
	print(tip)

	x = tip[0]
	y = tip[1]

pygameWindow = PYGAME_WINDOW()

print(pygameWindow)

controller = Leap.Controller()

while True:
	pygameWindow.Prepare(pygameWindow)
	#Perturb_Circle_Position()
	pygameWindow.Draw_Black_Circle(int(x),int(y))
	frame = controller.frame()
	if not (frame.hands.is_empty > 0):
		 Handle_Frame()

	pygameWindow.Reveal()


