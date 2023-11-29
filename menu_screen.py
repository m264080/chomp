import pygame
import sys
import random
import time
from game_parameters import *
from utilities import draw_background, add_meat
#from main import screen


def display_menu(screen):
    background = screen.copy()
    draw_background(background)#draws the background with dimentions from the screen


    # load game font
    big_font = pygame.font.Font("../final game/assets-finalgame/fonts/From_Cartoon_Blocks.ttf", 128)
    small_font = pygame.font.Font("../final game/assets-finalgame/fonts/Brainfish_Rush.ttf", 48)


    #create text object with the message "chomp" to display, and tuple (253, 69, 0) as font color
    text = big_font.render("PIZZA", True, (255, 0, 0))
    smaller_text = small_font.render("Press SPACE to play!", True, (255, 0, 0))


    # draws background
    screen.blit(background, (0, 0))

    # draw text at center of display
    screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))
    screen.blit(smaller_text, (SCREEN_WIDTH / 2 - text.get_width() / 2 - 20, SCREEN_HEIGHT / 2 - text.get_height() / 2 + 120))


    pygame.display.flip()

    # space_pressed = True # waiting for user to press space bar
    # while space_pressed:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
    #             space_pressed = False # once the space bar is pressed, = false so function ends --> game begins


#
# pygame.display.set_caption("Using tiles and blit to draw on surface")

