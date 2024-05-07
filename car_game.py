# Imports
import pygame
from pygame.locals import *
import math
import random
from settings import *

# Initialise imported pygame modules
pygame.init()

# Set up window
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('Car game')

# Background
bg = pygame.image.load('road_bg.png').convert()
bg_width = bg.get_width()

clock = pygame.time.Clock()

tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
scroll = 0

#car
img = pygame.image.load('car.png')
img.convert()

rect = img.get_rect()
rect.center = x, y

while running:
    pygame.time.delay(10)

    clock.tick(FPS)

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, ((i * bg_width + scroll), 0))

    # scroll background
    scroll -= 5

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0

    # Draw obstacles
    obstacle0 = pygame.draw.rect(screen, (255, 0, 0), [obstaclesx[0], obstaclesy[0], 20, 20])  # x,y,width, height
    obstacle1 = pygame.draw.rect(screen, (0, 255, 0), [obstaclesx[1], obstaclesy[1], 20, 20])
    obstacle2 = pygame.draw.rect(screen, (0, 0, 255), [obstaclesx[2], obstaclesy[2], 20, 20])
    obstacle3 = pygame.draw.rect(screen, (255, 255, 255), [obstaclesx[3], obstaclesy[3], 20, 20])

    # Coins
    coin0 = pygame.draw.rect(screen, (252, 186, 3), [coinx[0], coiny[0], 20, 20])  # x,y,width, height
    coin1 = pygame.draw.rect(screen, (252, 186, 3), [coinx[1], coiny[1], 20, 20])


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


    # Obstacles loop
    for i in range(len(obstaclesx)):
        if active:
            obstaclesx[i] -= obstacles_speed
            if obstaclesx[i] < -10:
                obstaclesx[i] = random.randint(600, 800)
                obstaclesy[i] = random.randint(0, 500)
                pygame.time.delay(10)
                score += 1
            if (rect.colliderect(obstacle0) or rect.colliderect(obstacle1) or rect.colliderect(
                    obstacle2) or rect.colliderect(obstacle3)):
                screen.fill((255, 0, 0))
                pygame.display.flip()
                score -= 1
            if score < -300:
                active = False

    # Coins loop
    for i in range(len(coinx)):
        if active:
            coinx[i] -= obstacles_speed
            if coinx[i] < -20:
                coinx[i] = random.randint(300, 800)
                coiny[i] = random.randint(0, 500)
            if rect.colliderect(coin0) or rect.colliderect(coin1):
                coins += 1
                print(coins)


    # Car
    img = pygame.image.load('car.png')
    img.convert()

    rect = img.get_rect()
    rect.center = x, y

    screen.blit(img, rect)


    pygame.display.flip()

pygame.quit()