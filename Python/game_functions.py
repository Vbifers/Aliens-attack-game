import sys, pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ship, settings, screen, bullets, stats, button, aliens, sb):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			keydown_events(ship,event, settings, screen, bullets, stats, aliens, sb)
		elif event.type==pygame.KEYUP:
			keyup_events(ship,event)
		elif event.type==pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_mouse_button_collide(stats, button, mouse_x, mouse_y, bullets, aliens, settings, screen, ship, sb)
			
def update_screen(stn, screen,ship,bullets, aliens, stats, button, sb):
	screen.fill(stn.bg_color)
	#draw bullets behind ship and enemies
	for bullet in bullets.sprites():
		bullet.draw_bullet()	
	ship.blitme()
	aliens.draw(screen)
	if not stats.game_active:
		button.draw_button()
	sb.blit_score()
	pygame.display.flip()

def keydown_events(ship,event,settings, screen, bullets, stats, aliens, sb):
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
	elif event.key==pygame.K_p:
		start_game(stats, bullets, aliens,settings, screen, ship, sb)
def keyup_events(ship,event):
	"""pool keys"""
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
def update_bullets(bullets, aliens, settings, screen, ship, stats, sb):
	bullets.update()
	#delete bullets escaped from the screen
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	check_bullet_alien_collision(bullets, settings, screen, aliens, ship, stats, sb)
	
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
	
def update_aliens(settings, aliens, ship, stats, screen, bullets, sb):
	check_fleet_edges(settings, aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(stats, settings, bullets, aliens, sb)
	check_alien_screen_bottom(screen, aliens, stats, settings, bullets, sb)
		 
		
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
			
def check_bullet_alien_collision(bullets, settings, screen, aliens, ship, stats, sb):
	#check collisions of bullet and allien
	collisions=pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for alien in collisions.values():
			stats.score+=(settings.alien_points*len(alien))
		sb.prep_score()
		check_high_score(stats, sb)
	if len(aliens) == 0:
		bullets.empty()
		settings.increase_dynamic_settings()
		stats.level += 1
		sb.prep_level()
		create_fleet(settings, screen, aliens, ship) 
		ship.center_ship()		
		sleep(0.2)
		
def ship_hit(stats, settings, bullets, aliens, sb):
	if stats.ship_left>0:
		stats.ship_left-=1
		sb.prep_ships()
		bullets.empty()
		aliens.empty()
	else:
		if stats.score >= stats.high_score:			
			stats.save_high_record()
			#print('hit')
		bullets.empty()
		aliens.empty()
		stats.game_active = False
		pygame.mouse.set_visible(True)
		
	 
def	check_alien_screen_bottom(screen, aliens,stats, settings, bullets, sb):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom>=screen_rect.bottom:
			ship_hit(stats, settings, bullets, aliens, sb)
			break
	
def check_mouse_button_collide(stats, button, mouse_x, mouse_y, bullets, aliens,settings, screen, ship, sb):
	if button.rect.collidepoint(mouse_x, mouse_y) and stats.game_active == False:
		start_game(stats, bullets, aliens,settings, screen, ship, sb)
		
def start_game(stats, bullets, aliens,settings, screen, ship, sb):
	stats.game_active = True
	settings.initialize_dynamic_settings()
	stats.reset_stats()
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()
	sb.prep_ships()
	bullets.empty()
	aliens.empty()
	create_fleet(settings, screen, aliens, ship)
	ship.center_ship()
	pygame.mouse.set_visible(False)

def check_high_score(stats, sb):
	"""check new hight scores"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
