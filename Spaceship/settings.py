class Settings():
    """储存游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""

        #屏幕
        self.screen_width =1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10

        #alien settings
        self.fleet_drop_speed = 20
        #fleet_direction, 1=right, -1=left
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

       


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction, 1=right, -1=left
        self.fleet_direction = 1

        #score
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points =int(self.alien_points * self.score_scale)
        

        

