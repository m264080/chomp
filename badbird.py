# import pygame
# import random
# from game_parameters import *
# from math import cos, sin
#
#
# class Badbird(pygame.sprite.Sprite):
#
#     def __init__(self, x,y):
#         super().__init__()
#
#         self.image = pygame.image.load("../final game/assets-finalgame/sprites/bird.png").convert()
#         self.image = pygame.transform.flip(self.image, True, False)
#
#         self.image.set_colorkey((255,255,255))
#         self.rect = self.image.get_rect()
#
#         self.x = x
#         self.y = y
#         self.rect.center = (x,y)
#
#         self.speed = random.uniform(BADBIRD_MIN_SPEED, BADBIRD_MAX_SPEED)
#
#     def update(self, direction):
#         self.x += self.speed * cos(direction)
#         self.rect.x = self.x
#         self.y += self.speed * sin(direction)
#         self.rect.y = self.y
#
#     def draw(self, screen):
#         screen.blit(self.image, self.rect)
#
#
# badbirds = pygame.sprite.Group()
