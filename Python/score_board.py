import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
	def __init__(self, screen, settings, stats):
		"""initialize score settings"""
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.settings = settings
		self.stats = stats
	
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None, 48)
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
		
	def prep_score(self):
		"""rendering score"""
		rounded_score = int(round(self.stats.score, -1))
		score_text = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_text, True, self.text_color,
		self.settings.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	def blit_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.ships.draw(self.screen)
		
	def prep_high_score(self):
		"""rendering hight score"""
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
		self.text_color, self.settings.bg_color)
		#record aligns at the center of the top side
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
	def prep_level(self):
		"""rendering level"""
		self.level_image = self.font.render(str(self.stats.level),True,
		self.text_color, self.settings.bg_color)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
	def prep_ships(self):
		"""inform about the current number of ships"""
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.screen, self.settings)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
