class Settings:
	def __init__(self):
		#ship params
		self.width = 1000
		self.height = 600
		self.bg_color = (230,230,230)
		self.speed = 1.5
		
		#bullet params
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_allowed = 3
		
		#alien params
		self.alien_speed = 0.5
		self.drop_speed = 5
		self.direction = 1
