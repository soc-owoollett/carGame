#Imports
import pygame
from pygame.locals import *

# Initialise imported pygame modules
pygame.init()

# Screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

# Set up window
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('Car game')

# Background
bg = pygame.image.load('road_bg.png').convert()
bg_width = bg.get_width()

# Variables
x, y = 100, 100
move_x, move_y = 0, 0

width = 10
height = 10

vel = 5

#car
img = pygame.image.load('car.png')
img.convert()

rect = img.get_rect()
rect.center = x, y


running = True

while running:
    pygame.time.delay(10)
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>0:
        x -= vel
    elif keys[pygame.K_RIGHT] and x<SCREEN_WIDTH-width:
        x += vel
    elif keys[pygame.K_UP] and y>0:
        y -= vel
    elif keys[pygame.K_DOWN] and y<SCREEN_HEIGHT-height:
        y += vel

    # Car
    img = pygame.image.load('car.png')
    img.convert()

    rect = img.get_rect()
    rect.center = x, y

    screen.blit(img, rect)


    pygame.display.flip()

pygame.quit()