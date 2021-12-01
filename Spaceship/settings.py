class Settings():
    """储存游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""

        #屏幕
        self.screen_width =1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3