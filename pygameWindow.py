import pygame
import constants

class PYGAME_WINDOW:

	def __init__(self):		
		pygame.init()
		self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth))


	@classmethod
	def Prepare(cls, self):
		self.screen.fill((255, 255, 255))

	@classmethod
	def Reveal(cls):
		pygame.display.update()

	def Draw_Black_Circle(self, x, y):
		pygame.draw.circle(self.screen, (0,0,0), (x, y), 7) #The first value is the surface, the second value is that the circle will be in black, the third value is the position where the circle will be drawn and the last value is the radius of the circle





