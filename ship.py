import pygame

class Ship():
    """ 管理《外星人入侵》飞船所有设置的类 """

    def __init__(self, ai_settings, screen):
        """ 初始化飞船并设置其初始位置 """
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外界矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """ 让飞船在屏幕上居中 """
        self.center = self.screen_rect.centerx

    def update(self):
        """ 根据移动标志调整飞船的位置 """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0: #self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):     #注意方法的缩进
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)

