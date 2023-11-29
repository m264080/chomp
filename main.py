import pygame
import sys
import random
from bigmeat import Bigmeat, bigmeats
from zza import Zza
from game_parameters import *
from utilities import draw_background, add_meat
from menu_screen import display_menu

#initialize pygame
pygame.init()


#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Using tiles and blit to draw on surface")

clock = pygame.time.Clock()

background = screen.copy()
draw_background(background)

#placing fish off right side of screen in random positions
add_meat(5)
zza = Zza(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

#initialize score with custom font
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)

for _ in range(5):
    bigmeats.add(Bigmeat(random.randint(0, SCREEN_WIDTH-TILE_SIZE), 0))

#main - actually runs the code
running = True
space_pressed = True  # waiting for user to press space bar
while running:

    while space_pressed:
        display_menu(screen)  #####################display menu here???
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                space_pressed = False  # once the space bar is pressed, = false so function ends --> game begins

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        # control player with arrow keys
        zza.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    zza.move_up()
            if event.key == pygame.K_LEFT:
                    zza.move_left()
            if event.key == pygame.K_RIGHT:
                    zza.move_right()
            if event.key == pygame.K_DOWN:
                    zza.move_down()

    #draws background
    screen.blit(background, (0,0))

    #update the sprites
    bigmeats.update()
    zza.update()

    result = pygame.sprite.spritecollide(zza, bigmeats, True) #checks for collisions between the sprites
    if result:
        score += len(result)
        # play chomp sound
        #pygame.mixer.Sound.play(chomp)
        # add new fish
        add_meat(len(result))
        bigmeats.add(Bigmeat(random.randint(0, SCREEN_WIDTH - TILE_SIZE), 0))

    # for bigmeat in bigmeats:
    #     if bigmeat.rect.x < -zza.rect.width:
    #         bigmeats.remove(zza)
    #         bigmeats.add(Bigmeat(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE)))

    # for bigmeat in bigmeats:
    #     if bigmeat.rect.y < -bigmeat.rect.height:
    #         bigmeats.remove(bigmeat)
    #         bigmeats.add(Bigmeat(random.randint(0, SCREEN_WIDTH - TILE_SIZE), 0))
    #         #bigmeats.add(Bigmeat(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*2), random.randint(TILE_SIZE, SCREEN_HEIGHT-TILE_SIZE)))


    bigmeats.draw(screen)
    zza.draw(screen)

    text = score_font.render(f"{score}", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH - text.get_width() - 10, 0))

    #update the display
    pygame.display.flip()

    clock.tick(60)

#quit game
pygame.quit()
sys.exit()


