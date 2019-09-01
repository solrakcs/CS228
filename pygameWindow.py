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




