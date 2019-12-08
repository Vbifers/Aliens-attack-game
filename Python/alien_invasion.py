import sys
import pygame
from settings import Settings


def run_game():
	pygame.init()
	stn = Settings()
	screen=pygame.display.set_mode((stn.width,stn.height))
	pygame.display.set_caption('Alien Invasion')
	bg_color = stn.bg_color
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
		screen.fill(bg_color)
		pygame.display.flip()
		
run_game()
