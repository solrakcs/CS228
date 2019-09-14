import sys
sys.path.insert(0, "..")
import Leap
from pygameWindow import PYGAME_WINDOW
from Derivable import DERIVABLE
import random
import pygame

new_derivable = DERIVABLE(PYGAME_WINDOW(), Leap.Controller(), 540, 360, 0, 1000.0, -1000.0, 1000.0, -1000.0)
new_derivable.Run_Forever()
