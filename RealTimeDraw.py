from pygameWindow import PYGAME_WINDOW


pygameWindow = PYGAME_WINDOW()

print(pygameWindow)

while True:
	pygameWindow.Prepare(pygameWindow)
	pygameWindow.Draw_Black_Circle(540,360)
	pygameWindow.Reveal()
