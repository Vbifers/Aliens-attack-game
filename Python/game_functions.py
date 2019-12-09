import sys, pygame

def check_events():
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
def update_screen(screen,bg_color, ship):
	screen.fill(bg_color)
	ship.blitme()
	pygame.display.flip()
