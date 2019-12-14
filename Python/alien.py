import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
	"""alien object"""
	def __init__(self, ai_settings, screen):
		"""initialize alien"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings
		# load alien image
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		# each new alien appears at left top corner of screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		# create alien position
		self.x = float(self.rect.x)
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
	
	def update(self):
		"""update alien position"""
		self.x+=(self.ai_settings.alien_speed*self.ai_settings.direction)
		self.rect.x=self.x
		
	def check_edges(self):
		"""check that the alien is at the edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right>=screen_rect.right or self.rect.left<=screen_rect.left:
			return True
