class GameStats():
	"""stores current level and score of the game"""
	def __init__(self, settings):
		self.settings = settings
		self.game_active = False
		self.reset_stats()
		
	def reset_stats(self):
		self.ship_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
		self.high_score = self.load_high_record()
		
	def load_high_record(self):
		"""load high level from txt file"""
		record = 0
		try:
			filepath ='data\high_record.txt'
			with open(filepath,'r') as f:
				str_record = f.read()
				try:
					record = int(str_record)
				except ValueError:
					print('in record file must stores only digits')
		except FileNotFoundError:
			print('record file not found!')
		return record
	
	def save_high_record(self):
		"""save high level from txt file"""
		record = 0
		print('here')
		try:
			filepath ='data\high_record.txt'
			with open(filepath,'w') as f:
				f.write(str(int(round(self.high_score,-1))))
		except FileNotFoundError:
			print('record file not found!')
		return record
		
