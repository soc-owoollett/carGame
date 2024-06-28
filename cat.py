# Import pygame
import pygame
from pygame.locals import *
import random

# Initialise imported pygame modules
pygame.init()

# Constants for screen width and height
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Set up window
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('First pygame')

# Background image
image = pygame.image.load('bg.jpg')

# Set colour
color = (0,0,0)

# Obstacle
pygame.mouse.set_visible(False)

# Cat
img = pygame.image.load('cat.png')
img.convert()

rect = img.get_rect()
rect.center = 200,200

isjump = False
v = 5
m = 1

x=100
y=100
# Run until quit
running = True
moving = False

while running:
    pygame.time.delay(10)
    # screen.fill(color)
    screen.blit(image, (0, 0))
    #pygame.display.flip()

    pos = pygame.mouse.get_pos()
    rect.center = pos

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
    keys = pygame.key.get_pressed()

    if isjump == False:
        if keys[pygame.K_SPACE]:
            isjump = True
    if isjump:
        F =(1/2)*m*(v**2)
        y-=F
        v=v-1

        if v<0:
            m =-1
        if v ==-6:
            isjump = False
            v= 5
            m= 1

    #screen.fill((50,100,100))
    screen.blit(image, (0, 0))
    screen.blit(img, rect)

    #pygame.draw.rect(screen, (0,0,255), rect, 2)


    pygame.display.flip()

pygame.quit()
