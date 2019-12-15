import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
	pygame.init()
	stn = Settings()
	screen=pygame.display.set_mode((stn.width,stn.height))
	pygame.display.set_caption('Alien Invasion')
	bg_color = stn.bg_color
	ship = Ship(screen, stn)
	#create group for keeping bullets
	bullets = Group()
	#create group for keeping aliens
	aliens = Group()
	gf.create_fleet(stn, screen, aliens, ship)
	#create stats
	stats = GameStats(stn)
	#create button
	button = Button(screen, stn, 'Play')
	while True:
		gf.check_events(ship, stn, screen, bullets, stats, button, aliens)
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, stn, screen, ship)
			gf.update_aliens(stn, aliens, ship, stats, screen, bullets)	
		gf.update_screen(stn, screen, ship, bullets, aliens, stats, button)
					
run_game()
