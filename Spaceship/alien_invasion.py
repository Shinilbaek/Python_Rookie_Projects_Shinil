from typing import Set
import pygame
from pygame.sprite import Group


from game_stats import GameStats
from settings import Settings
from ship import Ship
import game_functions as gf
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化pygame,setting,并创建屏幕对象
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption('Alien Invasion')

    play_button = Button(ai_settings,screen,"Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个存储子弹的编组
    bullets = Group()
    #创建一个外星人的编组
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens,ship)

    #开始游戏
    while True:
        #监视键盘鼠标
        gf.check_events(ai_settings,screen,stats,sb,play_button,
                        ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,sb,ship,aliens,bullets)

        #重新绘制屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


run_game()
