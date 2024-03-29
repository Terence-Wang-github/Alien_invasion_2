import pygame

class GameStats():
    """ 跟踪游戏统计信息的类 """

    def __init__(self, ai_settings):
        """ 初始化游戏统计信息 """
        self.ai_settings = ai_settings
        self.reset_stats()

        #游戏刚启动时处于非活动状态
        self.game_active = False

        #在任何情况下都不应该重置最高得分
        filename = 'high_score_digits.txt'
        with open(filename) as file_object:
            contents = file_object.read()
            self.high_score = int(contents.strip())

    def reset_stats(self):
        """ 初始化在游戏运行期间可能变化的统计信息 """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
