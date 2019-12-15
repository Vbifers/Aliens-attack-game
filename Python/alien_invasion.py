import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard

def run_game():
	"""main feature"""
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
	#create scoreboard
	sb = ScoreBoard(screen, stn, stats)
	while True:
		gf.check_events(ship, stn, screen, bullets, stats, button, aliens, sb)
		if stats.game_active:
			ship.update()
			gf.update_bullets(bullets, aliens, stn, screen, ship, stats, sb)
			gf.update_aliens(stn, aliens, ship, stats, screen, bullets, sb)	
		gf.update_screen(stn, screen, ship, bullets, aliens, stats, button, sb)
					
run_game()
