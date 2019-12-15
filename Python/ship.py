import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, screen, settings):
		super(Ship, self).__init__()
		self.settings = settings 
		self.screen = screen
		self.image = pygame.image.load("images\ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.rect.centerx = self.screen_rect.centerx
		#self.rect.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False
		self.center=float(self.rect.centerx)
		
	def update(self):
		"""update ship position"""
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.settings.speed
			self.rect.centerx=self.center
		if self.moving_left and self.rect.left>0:
			 
			self.center-=self.settings.speed
			self.rect.centerx=self.center
			
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		self.rect.centerx = self.screen_rect.centerx
			
		
