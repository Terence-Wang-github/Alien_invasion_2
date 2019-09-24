
import pygame

from setting import Setting
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象

    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一个play按钮、一艘飞船、一个用于存储子弹的编组、一个外星人编组、
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen) #注意此处形参不能漏
    bullets = Group()
    aliens = Group()

    #一个存储游戏统计信息的实例、并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #创建外星人群
    gf.creat_fleet(ai_settings, screen, aliens, ship)

    #开始主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, ship, play_button, aliens,
            bullets, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, aliens, ship, bullets, stats,
                sb)
            gf.update_aliens(ai_settings, screen, ship, aliens, bullets, stats)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats,
            play_button, sb)

run_game()


