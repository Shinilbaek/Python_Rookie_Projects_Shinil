import sys
import pygame
from pygame.version import SDLVersion
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key ==pygame.K_RIGHT:
        #move the ship to the right
        ship.moving_right = True
    elif event.key ==pygame.K_LEFT:
        #move the ship to the left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create a bullet then add it to group bullets
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
    """响应松开按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def check_events(ai_settings,screen,ship,bullets):
    """响应按键与鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
  

def update_screen(ai_settings,screen,ship,bullets):
    """更新屏幕上的图像，切换到新的屏幕"""
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人会面后重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    

    #最近绘制屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹位置并删除已消失的子弹"""
    #update bullet's location
    bullets.update()
    #delete disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen,ship,bullets):
    """如果子弹没有到达限制就发射一发"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
