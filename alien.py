# -*- coding: utf-8 -*-
# @Author     : Freedomly
# @Date       : 2017/11/7 21:22
# @Email      : Freedom.JLF@gmail.com
# @File       : alien.py
# @Software   : PyCharm Community Edition
# @Description: management of alien


import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    表示单个外星人的类
    """

    def __init__(self, ai_settings, screen):
        """
        初始化外星人并设置其起始位置
        :param ai_settings: 游戏设置
        :param screen: 目标屏幕
        """
        # super(Alien, self).__init__()   # python2.7
        super().__init__()  # python3
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """
        在指定位置绘制外星人
        :return:
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        更新外星人位置
        :return:
        """
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """
        如果外星人位于屏幕边缘，就返回True
        :return: True / False
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
