import pygame
from pygame.locals import *
import random
import math
from settings import *

def iterate_nested_dict(all_cars):
    for key, value in all_cars.items():
        if isinstance(value, dict):
            iterate_nested_dict(value)
        else:
            print(f"Key: {key}, Value: {value}")

def current_car_stats():
    for key, nested_dict in all_cars.items():
        if 'current' in nested_dict and nested_dict['current'] == True:
            vel = nested_dict['speed']
            delay = nested_dict['lag']
            print(f"{vel}")
            print(f"{delay}")
            return vel, delay

vel, delay = current_car_stats()

print(f"Delay:{vel}")
print(f"Speed:{delay}")

class Button:
    def __init__(self, x, y, image, scale, screen):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.clicked = False
        self.screen = screen

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.x, self.y))
        return action

def menu(coins):

    pygame.display.set_caption("Main Menu screen")

    # Buttons
    play_img = pygame.image.load('play_btn.png').convert()
    play_btn = Button((SCREEN_WIDTH/2)-95, (SCREEN_HEIGHT/2)-80, play_img, 1, screen)

    cars_img = pygame.image.load('cars_btn.png').convert()
    cars_btn = Button((SCREEN_WIDTH/2)-95, (SCREEN_HEIGHT / 2), cars_img, 1, screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_c:
                    cars()

        # Draw the button and check for clicks
        if play_btn.draw() == True:
            print("play")
            play()

        elif cars_btn.draw() == True:
            print("cars")
            cars()

        # Update display
        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Button Example')

play_btn = pygame.image.load('play_btn.png').convert_alpha()
btn = Button(400,400, play_btn,1, screen)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw the button and check for clicks
    if btn.draw():
        print("Button clicked!")  # Example action upon button click

    # Update display
    pygame.display.flip()

pygame.quit()