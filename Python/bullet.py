import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Class for control bullets"""
	def __init__(self, settings, screen, ship):
		"""create bullet object"""
		super(Bullet, self).__init__()
		self.screen = screen
		self.settings = settings
		#create bullet in position (0,0) and set settings
		self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
		
		#assign an initial position
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top 
		
		#bullet position is a float(real) type
		self.y = float(self.rect.y)
		self.color = self.settings.bullet_color
		self.speed = self.settings.bullet_speed
	def update(self):
		#update bullet position
		self.y -= self.speed
		self.rect.y=self.y
	def draw_bullet(self):	
		#draw bullet on new position
		pygame.draw.rect(self.screen,self.color,self.rect)
		
		
