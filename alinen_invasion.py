


import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf



def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    #screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 设置背景色
    #bg_color = (230,230,230)

    #开始游戏的主循环
    while True:
        
        #每次循环时都重绘屏幕
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
        #监控键盘和鼠标事件
        # 2.0版本改进了对于游戏退出的事件，转而改进了导入相应的功能函数
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        '''
        # 2.0版本的事件重构
        gf.check_events(ship)
        
run_game()
