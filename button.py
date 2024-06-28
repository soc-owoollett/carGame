# Import pygame
import pygame
from pygame.locals import *
import random
import math

# Initialise imported pygame modules
pygame.init()

# Constants for screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

# Set up window
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('First pygame')

playing = False
menus = False
cat_state = True
car = True

def play():
    msg = "helloworld"
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == QUIT:
                play = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    play = False

        pygame.display.flip()
        return msg

def cat():
    car = True
    while car:
        print("cat cat cat")
        for event in pygame.event.get():
            if event.type == QUIT:
                car = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    car = False
def menu():
    while menu:
        print(msg)


play()
print(msg)
menu()

pygame.quit()