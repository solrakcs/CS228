import sys
sys.path.insert(0, "..")
import Leap
from pygameWindow import PYGAME_WINDOW
import random
import pygame
from Derivable import DERIVABLE


new_derivable = DERIVABLE()
exit()

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
		 Handle_Frame()
		 
	pygameWindow.Reveal()
