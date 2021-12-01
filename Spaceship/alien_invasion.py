from typing import Set
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化pygame,setting,并创建屏幕对象
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption('Alien Invasion')

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个存储子弹的编组
    bullets = Group()

    #背景色
    bg_color =(230,230,230)


    #开始游戏
    while True:
        #监视键盘鼠标
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(bullets)

        #重新绘制屏幕
        gf.update_screen(ai_settings,screen,ship,bullets)


run_game()
