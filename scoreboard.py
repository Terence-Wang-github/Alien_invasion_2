import pygame.font

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

        #准备渲染图像
        self.prep_score()

    def prep_score(self):
        """ 准备渲染图像,并将得分显示在右上角 """
        # score_str = str(self.stats.score)
        #将得分圆整为最近的10的倍数
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()

        #显示得分放到右上角
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ 在屏幕上显示得分 """
        self.screen.blit(self.score_image, self.score_rect)