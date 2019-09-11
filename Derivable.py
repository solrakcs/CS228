class DERIVABLE:

	def __init__(self, xMin, xMax, yMin, yMax, x, y, befValue):
		
		self.xMin = 1000.0
		self.xMax = -1000.0
		self.yMin = 1000.0 
		self.yMax = -1000.0
		self.x = 540
		self.y = 360
		self.befValue = 0



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
		pygameWindow.Draw_Black_Line(pygameXBase, pygameYBase, pygameXTip, pygameYTip, b)
		



	def Handle_Finger(finger):
		for b in range(4):
			Handle_Bone(b)
				
	
	
	def Handle_Frame():
		global x, y
		global finger
	
		hand = frame.hands[0]
		fingers = hand.fingers
		length = len(fingers) 
		for i in range(length):
			finger = fingers[i]
			Handle_Finger(finger)
	
	
	def Scale(value, minValue, maxValue, newMinValue, newMaxValue):
	
		global befValue
	
		if maxValue == minValue:
			return befValue
	
		percentage_scaling = (value - minValue) / (maxValue - minValue)
		befValue = ((newMaxValue - newMinValue) * percentage_scaling) + newMinValue
		return befValue	