class Settings():
    """储存游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""

        #屏幕
        self.screen_width =1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 10

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction, 1=right, -1=left
        self.fleet_direction = 1

        

