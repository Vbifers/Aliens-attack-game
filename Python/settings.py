class Settings:
	def __init__(self):
		#ship params
		self.width = 1000
		self.height = 600
		self.bg_color = (230,230,230)
		self.speed = 1.5
		self.ship_limit = 3
		
		#bullet params
		self.bullet_speed = 2
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_allowed = 3
		
		#alien params
		self.drop_speed = 30
		self.direction = 0.7
		
		self.speedup_scale = 1.1
		self.scoreup_scale = 1.5
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.alien_speed = 0.5
		self.alien_points = 50
	
	def increase_dynamic_settings(self):
		self.alien_speed *= self.speedup_scale	
		self.alien_points*=self.scoreup_scale
