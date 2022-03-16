#创建一个背景色为蓝色的窗口


import sys
import pygame


def run_bg():
    #初始化一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption('Test!')
    #设置背景色
    bg_color = (0, 102, 255)

    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()   
run_bg()