import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """ 显示得分信息的类 """

    def __init__(self, ai_settings, screen, stats):
        """ 初始化显示得分涉及的属性 """
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        #显示得分时的字体设置
        self.text_color =(30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #准备渲染包含最高得分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """ 准备渲染图像,并将得分显示在右上角 """
        # score_str = str(self.stats.score)
        #将得分圆整为最近的10的倍数
        rounded_score = round(self.stats.score, -1)
        score_str = "Score: "+"{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()

        #显示得分放到右上角
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """ 准备渲染最高得分，并将其显示在屏幕中间 """
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: "+"{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.ai_settings.bg_color)
        
        #显示得分放到上面中间
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """ 准备渲染游戏等级的的图像，并将其放在的得分下方 """
        level_str = "Level: "+ str(self.stats.level)
        self.level_image =self.font.render(level_str, True,
            self.text_color, self.ai_settings.bg_color)

        #将等级放在的得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom

    def prep_ships(self):
        """ 显示还余下多少飞船 """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """ 在屏幕上显示得分和当前的最高得分 """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        #绘制飞船
        self.ships.draw(self.screen)
