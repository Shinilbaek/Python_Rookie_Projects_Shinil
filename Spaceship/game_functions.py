import sys
import pygame
from pygame.version import SDLVersion
from time import sleep

from bullet import Bullet
from alien import Alien
from ship import Ship
from game_stats import GameStats
from button import Button


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
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """响应松开按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """响应按键与鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)        
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,
                                ship,aliens,bullets,mouse_x,mouse_y)
  
def check_play_button(ai_settings,screen,stats,sb,play_button,
                        ship,aliens,bullets,mouse_x,mouse_y):
    """start the game when click the play button"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        # initialize the game
        ai_settings.initialize_dynamic_settings()

        #隐藏光标
        pygame.mouse.set_visible(False)

        # reset game stats
        stats.reset_stats()
        stats.game_active = True

        #reset scoreboard
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #clear aliens list and bullets list
        aliens.empty()
        bullets.empty()

        #create a new fleet and center the spaceship
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """更新屏幕上的图像，切换到新的屏幕"""
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人会面后重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #显示得分
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    #最近绘制屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹位置并删除已消失的子弹"""
    #update bullet's location
    bullets.update()
    #delete disappeared bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    #check if there is a bullet that shut an alien
    #if so, delete the bullet and alien above
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
    

def fire_bullet(ai_settings, screen,ship,bullets):
    """如果子弹没有到达限制就发射一发"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width): 
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width 
    number_aliens_x = int(available_space_x / (2 * alien_width)) 
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height): 
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height)) 
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number,row_number): 
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number 
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)    

def create_fleet(ai_settings,screen,aliens,ship):
    """create a fleet"""
    #create an alien and calculate how many aliens can be in a row
    #the space between two aliens is an alien's width
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height, alien.rect.height) - 1 

    for row_number in range(1,number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)


def update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """update alien's loction in fleet"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #check if the spaceship hits an alien
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
        print('SHIP HIT!!!')

    #check if an alien reaches the bottom
    check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets)


def check_fleet_edges(ai_settings,aliens):
    """when an alien reaches the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direciton(ai_settings,aliens)
            break

def change_fleet_direciton(ai_settings,aliens):
    """move the fleet down and change their directions"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,
                                    ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0:
        #delete all the bullets then create a new fleet
        bullets.empty()
        ai_settings.increase_speed()

        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings,screen,aliens,ship)

def ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """响应被外星人撞到的飞船"""
    # subtract ships_left with 1
    if stats.ships_left>0:
        stats.ships_left -=1

        #update scoreboard
        sb.prep_ships()

        # clear aliens list and bullets list
        aliens.empty()
        bullets.empty()

        # create a new fleet and put a new spaceship at the mid-bottom
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    # pause
    sleep(0.5)


def check_aliens_bottom(ai_settings,stats,screen,sb,ship,aliens,bullets):
    """check if there is an alien reaching the bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
            print('ALIENS WIN!!!')
            break

def check_high_score(stats,sb):
    """检查是否产生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()