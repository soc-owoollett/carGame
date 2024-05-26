# Imports
import pygame
from pygame.locals import *
import random
import math
from settings import *

pygame.init()

# Constants for screen(width,heiht,frames/s)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def draw_text(text,font,colour,x,y):
    txt = font.render(text, True, colour)
    screen.blit(txt,(x,y))

def menu():
    screen.fill((255, 0, 0))
    pygame.display.set_caption("Main Menu screen")
    text_font = pygame.font.SysFont("Arial", 30)

    draw_text("This is the main menu", text_font, (0, 0, 0), 100, 100)
    run()

def play():

    pygame.display.set_caption("Play screen")

    active = True
    running = True

    # Screen width and height
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500

    # Variables
    FPS = 60
    invulnerable = 50
    collecting = 50

    x, y = 100, 100
    move_x, move_y = 0, 0

    width = 10
    height = 10

    # Car speed
    delay = 10
    vel = 5

    score = 3
    coins = 0

    # Obstacles
    obstaclesx = [800, 800, 800, 800]
    # obstaclesx = [300,550,725,760]
    obstaclesy = [90, 400, 90, 200]  # in line coordinates - 90, 200, 290, 400

    # Coins
    coinx = [550, 775]
    coiny = [200, 290]

    obstacles_speed = 10

    # Set up window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption('Car game')

    # Background
    bg = pygame.image.load('road_bg.png').convert()
    bg_width = bg.get_width()

    clock = pygame.time.Clock()

    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    scroll = 0

    # car
    img = pygame.image.load('car.png')
    img.convert()

    damaged = 0

    rect = img.get_rect()
    rect.center = x, y

    text_font = pygame.font.SysFont("Arial", 30)
    bigger_font = pygame.font.SysFont("Arial", 80)

    while running:
        pygame.time.delay(delay)

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
        # car0
        green_car_img = pygame.image.load('green_car.png')
        green_car_img.convert()

        car0 = green_car_img.get_rect()
        car0.center = (obstaclesx[0], obstaclesy[0])
        screen.blit(green_car_img, car0)

        # car1
        blue_car_img = pygame.image.load('blue_car.png')
        blue_car_img.convert()

        car1 = blue_car_img.get_rect()
        car1.center = (obstaclesx[1], obstaclesy[1])
        screen.blit(blue_car_img, car1)

        # car2
        truck_img = pygame.image.load('truck.png')
        truck_img.convert()

        car2 = truck_img.get_rect()
        car2.center = (obstaclesx[2], obstaclesy[2])
        screen.blit(truck_img, car2)

        # car3
        cop_car_img = pygame.image.load('cop_car.png')
        cop_car_img.convert()

        car3 = cop_car_img.get_rect()
        car3.center = (obstaclesx[3], obstaclesy[3])
        screen.blit(cop_car_img, car3)

        # Coins
        coin_img = pygame.image.load('coin_img.png')
        coin_img.convert()

        # coin0
        coin0 = coin_img.get_rect()
        coin0.center = (coinx[0], coiny[0])
        screen.blit(coin_img, coin0)

        # coin1
        coin1 = coin_img.get_rect()
        coin1.center = (coinx[1], coiny[1])
        screen.blit(coin_img, coin1)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
        elif keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - width:
            x += vel
        elif keys[pygame.K_UP] and y > 0:
            y -= vel
        elif keys[pygame.K_DOWN] and y < SCREEN_HEIGHT - height:
            y += vel

        invulnerable -= 1
        collecting -= 1

        # Obstacles loop
        for i in range(len(obstaclesx)):
            if active:
                obstaclesx[i] -= obstacles_speed
                if obstaclesx[i] < -10:
                    obstaclesx[i] = 800
                    if (car0.colliderect(car1) or car0.colliderect(car2) or car0.colliderect(car3)
                            or car1.colliderect(car2) or car1.colliderect(car3) or car2.colliderect(car3)):
                        obstaclesx[i] = random.randint(600, 800)
                    obstaclesy[i] = random.choice((90, 200, 290, 400))
                    pygame.time.delay(10)
                    # score += 1
                    if (rect.colliderect(car0) or rect.colliderect(car1) or rect.colliderect(
                            car2) or rect.colliderect(car3)) and invulnerable <= 0:
                        screen.fill((255, 0, 0))
                        pygame.display.flip()
                        score -= 1
                        invulnerable = 5
                    if score < 0:
                        active = False

        # Coins loop
        for i in range(len(coinx)):
            if active:
                coinx[i] -= obstacles_speed
                if coinx[i] < -20:
                    coinx[i] = random.randint(300, 800)
                    coiny[i] = random.choice((90, 200, 290, 400))  # in line coordinates - 90, 200, 290, 400
                if rect.colliderect(coin0) and collecting <= 0 or rect.colliderect(coin1) and collecting <= 0:
                    coins += 1
                    collecting = 20

        if score < 0:
            draw_text("Game Over", bigger_font, (0, 0, 0), 200, 150)
            pygame.display.flip()
            run()


        # Car
        img = pygame.image.load('car.png')
        img.convert()

        rect = img.get_rect()
        rect.center = x, y

        screen.blit(img, rect)

        draw_text("Lives: {}".format(score), text_font, (0, 0, 0), SCREEN_WIDTH - (100 + 10 * len(str(score))),
                  SCREEN_HEIGHT - 40)
        draw_text("Coins: {}".format(coins), text_font, (0, 0, 0), 20, SCREEN_HEIGHT - 40)

        pygame.display.flip()
    pygame.quit()

def cars():
    screen.fill((0, 255, 0))
    pygame.display.set_caption("Cars screen")
    text_font = pygame.font.SysFont("Arial", 30)
    draw_text("This is the cars screen", text_font, (0, 0, 0), 100, 100)
    run()

def run():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                elif event.key == K_c:
                    cars()
                elif event.key == K_m:
                    menu()
                elif event.key == K_p:
                    play()

        pygame.display.flip()

menu()


pygame.quit()

