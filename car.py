# Import pygame
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
bg = pygame.image.load('road.png').convert()
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

tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
scroll = 0

# Set colour
color = (0,0,0)

width = 10
height = 10

vel = 5

# obstacles
obstacles = [300,450,600]
obstacles_speed = 10
active = True

img = pygame.image.load('car.png')
img.convert()

rect = img.get_rect()
rect.center = x, y

# Run until quit
running = True

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
    obstacle0 = pygame.draw.rect(screen, (255,0,0), [obstacles[0], 200,20,20])
    obstacle1 = pygame.draw.rect(screen, (0, 255, 0), [obstacles[1], 200, 20, 20])
    obstacle2 = pygame.draw.rect(screen, (0, 0, 255), [obstacles[2], 200, 20, 20])

    pygame.time.delay(10)
    # screen.fill(color)

    if x == 0:
        running = False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>0:
        #pygame.transform.rotate(rect,90)
        x -= vel
    elif keys[pygame.K_RIGHT] and x<SCREEN_WIDTH-width:
        x += vel
    elif keys[pygame.K_UP] and y>0:
        y -= vel
    elif keys[pygame.K_DOWN] and y<SCREEN_HEIGHT-height:
        y += vel

    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacles_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(470,570)
                score += 1
            if rect.colliderect(obstacle0) or rect.colliderect(obstacle1) or rect.colliderect(obstacle2):
                screen.fill((255,0,0))
                pygame.display.flip()
                score -=1
                if score < -300:
                    active = False


    # Car
    img = pygame.image.load('car.png')
    img.convert()

    rect = img.get_rect()
    rect.center = x, y

    screen.blit(img, rect)
    draw_text("Score: {}".format(score), text_font, (0, 0, 0), SCREEN_WIDTH-130, SCREEN_HEIGHT-40)
    pygame.display.flip()

pygame.quit()
