import sys, pygame
from bullet import Bullet
from alien import Alien

def check_events(ship, settings, screen, bullets):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			keydown_events(ship,event, settings, screen, bullets)
		elif event.type==pygame.KEYUP:
			keyup_events(ship,event)
def update_screen(stn, screen,ship,bullets, aliens):
	screen.fill(stn.bg_color)
	#draw bullets behind ship and enemies
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
	aliens.draw(screen)
	pygame.display.flip()

def keydown_events(ship,event,settings, screen, bullets):
	"""push keys"""
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	#include new bullet in group
	elif event.key==pygame.K_SPACE and len(bullets)<settings.bullet_allowed:
		fire_bullet(settings,screen,ship,bullets)
	elif event.key==pygame.K_q:
		sys.exit()
def keyup_events(ship,event):
	"""pool keys"""
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
def update_bullets(bullets):
	bullets.update()
	#delete bullets escaped from the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
def fire_bullet(settings,screen,ship,bullets):
	new_bullet = Bullet(settings, screen, ship)
	bullets.add(new_bullet)
	
def create_fleet(settings, screen, aliens, ship):
	number_aliens_x = get_number_aliens(settings, screen)
	number_aliens_y = get_number_rows(settings, screen, ship)
	for row_number in range(number_aliens_y):
		for number in range(number_aliens_x):
			create_alien(settings,screen,number,aliens, row_number)
		
def create_alien(settings,screen,number,aliens, row_number):
	alien = Alien(settings, screen)
	alien.x = alien.rect.width+number*alien.rect.width*2
	alien.rect.x = alien.x
	alien.rect.y = row_number*2*alien.rect.height
	aliens.add(alien)
	
def get_number_aliens(settings, screen):
	alien = Alien(settings, screen)
	available_space_x = settings.width - (alien.rect.width*2)
	number_aliens_x = int(available_space_x/(alien.rect.width*2))
	return number_aliens_x
	
def get_number_rows(settings, screen, ship):
	alien = Alien(settings, screen)
	avaliable_space_y = settings.height - 3*alien.rect.height-ship.rect.height
	number = int(avaliable_space_y/(2*alien.rect.height))
	return number
	
def update_aliens(settings, aliens):
	check_fleet_edges(settings, aliens)
	aliens.update() 
		
def check_fleet_edges(settings, aliens):
	"""control the fleet reaching the edge of the screen"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break

def change_fleet_direction(settings, aliens):
	"""change fleet direction"""
	for alien in aliens.sprites():
		alien.rect.y+=settings.drop_speed
	settings.direction*=-1
			
		
