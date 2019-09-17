import sys
sys.path.insert(0, "..")
import Leap
from pygameWindow_Del03 import PYGAME_WINDOW
from Derivable import DERIVABLE
import random
import pygame
import os

new_derivable = DERIVABLE(PYGAME_WINDOW(), Leap.Controller(), 540, 360, 1000, 1000.0, -1000.0, 1000.0, -1000.0)
new_derivable.Run_Forever()
