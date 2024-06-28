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
image = pygame.image.load('background.jpg')
screen.blit(image,(0,0))
pygame.display.flip()

# Variables
x, y = 100, 100
move_x, move_y = 0, 0

# Set colour
color = (0,0,0)

width = 10
height = 10

vel = 10

# Obstacle
rect_1 = pygame.Rect(0,0,25,25)
obst_rect = pygame.Rect(random.randint(0,500), random.randint(0,500),30,30)
obst_rect1 = pygame.Rect(random.randint(0,500), random.randint(0,500),15,60)
pygame.mouse.set_visible(False)

# Run until quit
running = True

while running:
    pygame.time.delay(10)
    # screen.fill(color)
    screen.blit(image, (0, 0))

    if rect_1.colliderect(obst_rect) or rect_1.colliderect(obst_rect1):
        screen.fill((255,0,0))
        pygame.display.update()
        pygame.time.delay(100)

    pos = pygame.mouse.get_pos()
    rect_1.center = pos
    pygame.draw.rect(screen,(255,255,255), rect_1)
    pygame.draw.rect(screen, (190,0,0), obst_rect)
    pygame.draw.rect(screen, (190,0,0), obst_rect1)

    if y == SCREEN_HEIGHT-height:
        running = False
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


    pygame.draw.rect(screen, (0,0,225),
                     (x, y, width, height))
    pygame.display.flip()

pygame.quit()
