# Imports
import pygame
from pygame.locals import *
import random
import math

# Initialise imported pygame modules
pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Constants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

# Set up window
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('First pygame')

# Background image
bg = pygame.image.load('road_bg.png').convert()
bg_width = bg.get_width()

text_font = pygame.font.SysFont("Arial",30)

# Functions
def draw_text(text,font,colour,x,y):
    txt = font.render(text, True, colour)
    screen.blit(txt,(x,y))

# Variables
x, y = 100, 100
move_x, move_y = 0, 0

score = 0
coins = 0

tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
scroll = 0

# Set colour
color = (0,0,0)

width = 10
height = 10

vel = 5

# obstacles
obstaclesx = [300,550,725,800]
obstaclesy = [100,270,320,450]
coinx = [550,775]
coiny = [250,370]

obstacles_speed = 10
active = True

img = pygame.image.load('car.png')
img.convert()

rect = img.get_rect()
rect.center = x, y

# Run until quit
running = True
hit = False

while running:

    clock.tick(FPS)

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, ((i * bg_width + scroll), 0))

    # scroll background
    scroll -=5

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # Obstacles
    obstacle0 = pygame.draw.rect(screen, (255,0,0), [obstaclesx[0], obstaclesy[0],20,20]) # x,y,width, height
    obstacle1 = pygame.draw.rect(screen, (0, 255, 0), [obstaclesx[1], obstaclesy[1], 20, 20])
    obstacle2 = pygame.draw.rect(screen, (0, 0, 255), [obstaclesx[2], obstaclesy[2], 20, 20])
    obstacle3 = pygame.draw.rect(screen, (200, 10, 210), [obstaclesx[3], obstaclesy[3], 20, 20])

    # Coins
    coin_img = pygame.image.load('coin_img.png')
    img.convert()

    coin0 = coin_img.get_rect()
    coin0.center = (coinx[0], coiny[0])

    #coin0 = pygame.draw.rect(screen, (252, 186, 3), [coinx[0], coiny[0], 20, 20])  # x,y,width, height
    coin1 = pygame.draw.rect(screen, (252, 186, 3), [coinx[1], coiny[1], 20, 20])

    pygame.time.delay(10)
    # screen.fill(color)

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
    elif keys[pygame.K_UP] and y>35:
        y -= vel
    elif keys[pygame.K_DOWN] and y<SCREEN_HEIGHT-height:
        y += vel

    # Obstacles loop
    for i in range(len(obstaclesx)):
        if active:
            obstaclesx[i] -= obstacles_speed
            if obstaclesx[i] < -10:
                obstaclesx[i] = random.randint(600,800)
                obstaclesy[i] = random.randint(0,500)
                pygame.time.delay(10)
                score += 1
            if (rect.colliderect(obstacle0) or rect.colliderect(obstacle1) or rect.colliderect(obstacle2) or rect.colliderect(obstacle3)) and not hit :
                hit = True
                screen.fill((255,0,0))
                pygame.display.flip()
                score -=1
            else:
                hit = False
                if score < -300:
                    active = False

    # Coins loop
    for i in range(len(coinx)):
        if active:
            coinx[i] -= obstacles_speed
            if coinx[i] < -20:
                coinx[i] = random.randint(300,800)
                coiny[i] = random.randint(0,500)
            if rect.colliderect(coin0) or rect.colliderect(coin1):
                coins +=1
                if score < -300:
                    active = False

    # Car
    img = pygame.image.load('car.png')
    img.convert()

    rect = img.get_rect()
    rect.center = x, y

    screen.blit(img, rect)
    draw_text("Score: {}".format(score), text_font, (0, 0, 0), SCREEN_WIDTH-(100 + 10 * len(str(score))), SCREEN_HEIGHT-40)
    draw_text("Coins: {}".format(coins), text_font, (0, 0, 0), 20,460)

    pygame.display.flip()


pygame.quit()
