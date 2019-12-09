import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	pygame.init()
	stn = Settings()
	screen=pygame.display.set_mode((stn.width,stn.height))
	pygame.display.set_caption('Alien Invasion')
	bg_color = stn.bg_color
	ship = Ship(screen)
	while True:
		gf.check_events()
		gf.update_screen(screen,bg_color, ship)
					
run_game()
