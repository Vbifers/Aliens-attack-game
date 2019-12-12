import sys, pygame
from bullet import Bullet

def check_events(ship, settings, screen, bullets):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			keydown_events(ship,event, settings, screen, bullets)
		elif event.type==pygame.KEYUP:
			keyup_events(ship,event)
def update_screen(stn, screen,ship,bullets):
	screen.fill(stn.bg_color)
	#draw bullets behind ship and enemies
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
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
