''''Docstring
Name: Olivia Woollett

Car game, instructions for playing and game messages will show in the console.
'''

# Imports
import pygame
from pygame.locals import *
import random
import math
from settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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


def draw_text(text,font,colour,x,y):
    txt = font.render(text, True, colour)
    screen.blit(txt,(x,y))


def current_car_stats():
    for key, nested_dict in all_cars.items():
        if 'current' in nested_dict and nested_dict['current'] == True:
            vel = nested_dict['speed']
            delay = nested_dict['delay']
            car_img = nested_dict['car_img']
            dmg_1 = nested_dict['dmg_1']
            dmg_2 = nested_dict['dmg_2']
            dmg_3 = nested_dict['dmg_3']
            return vel, delay, car_img, dmg_1, dmg_2, dmg_3

def buy_car(car):
    for key, nested_dict in all_cars.items():
        if 'model' in nested_dict and nested_dict['model'] == car:
            price = nested_dict['price']
            owned = nested_dict['owned']
            current = nested_dict['current']
            return price, owned, current


def menu(coins):
    global total_coins, text_font

    pygame.display.set_caption("Main Menu screen")

    # Buttons
    play_img = pygame.image.load('play_btn.png').convert_alpha()
    play_btn = Button((SCREEN_WIDTH/2)-95, (SCREEN_HEIGHT/2)-80, play_img, 1, screen)

    cars_img = pygame.image.load('cars_btn.png').convert_alpha()
    cars_btn = Button((SCREEN_WIDTH/2)-95, (SCREEN_HEIGHT / 2), cars_img, 1, screen)

    # Coins
    total_coins += coins
    coins = 0   #reset coins value

    background = pygame.image.load('main_menu_bg.jpg').convert_alpha()
    screen.blit(background, (0, 0))

    main_menu_img = pygame.image.load("main_menu_img.png").convert_alpha()
    screen.blit(main_menu_img, (260, 40))

    dollar_sign = pygame.image.load('dollar.png')
    screen.blit(dollar_sign, (0, 455))
    draw_text((str(total_coins)), text_font, (255, 255, 255), 50, 458)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_c:
                    cars(coins)
                elif event.key == K_p:
                    play()


        # Draw the button and check for clicks
        if play_btn.draw():
            play()
            running = False

        elif cars_btn.draw():
            cars(coins)
            running = False


        # Update display
        pygame.display.flip()
    return total_coins


def play():
    # Reset variables required for playing
    score = 3
    active = True
    global SCREEN_WIDTH, SCREEN_HEIGHT, FPS, invulnerable, collecting, obstaclesx, obstaclesy, obstacles_speed, \
        running, coins, x, y, move_x, move_y, width, height, coinx, coiny, text_font

    pygame.display.set_caption("Play screen")

    vel, delay, car_img, dmg_1, dmg_2, dmg_3 = current_car_stats()

    # Set up window
    pygame.display.set_caption('Car game')

    # Background
    bg = pygame.image.load('road_bg.png').convert()
    bg_width = bg.get_width()

    clock = pygame.time.Clock()

    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    scroll = 0

    # car
    img = pygame.image.load(car_img)
    img.convert()

    damaged = 0

    rect = img.get_rect()
    rect.center = x, y

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
                elif event.key == K_c:
                    cars(coins)
                elif event.key == K_m:
                    menu(coins)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= vel
        elif keys[pygame.K_RIGHT] and x < SCREEN_WIDTH - width:
            x += vel
        elif keys[pygame.K_UP] and y > 50:
            y -= vel
        elif keys[pygame.K_DOWN] and y < 450:
            y += vel

        invulnerable -= 1
        collecting -= 1

        # Obstacle speed
        if coins >= 10:
            obstacles_speed = 10
        elif coins >= 20:
            obstacles_speed = 20
        elif coins >= 30:
            obstacles_speed = 30
        elif coins >= 40:
            obstacles_speed = 40

        obstacle_sfx = pygame.mixer.Sound("obstacle_sfx.mp3")
        coin_sfx = pygame.mixer.Sound("coins_sfx.mp3")
        pygame.mixer.music.stop()

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
                        obstacle_sfx.play()
                        score -= 1
                        invulnerable = 5
                        damaged += 1
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
                    coin_sfx.play()
                    collecting = 20


        if score < 0:
            screen.fill((0,0,0))
            game_over_img = pygame.image.load("game_over_img.png").convert_alpha()
            screen.blit(game_over_img, (100, 100))
            pygame.display.flip()
            pygame.time.wait(2000)
            menu(coins)

        # Car image
        img = pygame.image.load(car_img).convert_alpha()

        # Car
        if damaged == 1:
            img = pygame.image.load(dmg_1).convert_alpha()
        elif damaged == 2:
            img = pygame.image.load(dmg_2).convert_alpha()
        elif damaged == 3:
            img = pygame.image.load(dmg_3).convert_alpha()


        rect = img.get_rect()
        rect.center = x, y

        screen.blit(img, rect)

        draw_text("Lives: {}".format(score), text_font, (0, 0, 0), SCREEN_WIDTH - (100 + 10 * len(str(score))),
                  SCREEN_HEIGHT - 40)
        draw_text("Coins: {}".format(coins), text_font, (0, 0, 0), 20, SCREEN_HEIGHT - 40)

        pygame.display.flip()

    pygame.quit()


def cars(coins):
    global total_coins, text_font
    pygame.display.set_caption("Cars screen")

    menu_img = pygame.image.load('menu_btn.png').convert_alpha()
    menu_btn = Button(10,10, menu_img, 0.75, screen)

    play_img = pygame.image.load('play_btn.png').convert_alpha()
    play_btn = Button(15, 80, play_img, 0.75, screen)

    #Car buy and select buttons
    corolla_select_img = pygame.image.load('select_btn.png').convert_alpha()
    corolla_select_btn = Button(80, 400, corolla_select_img, 0.5, screen)

    wrx_buy_img = pygame.image.load('buy_btn.png').convert_alpha()
    wrx_buy_btn = Button(300, 400, wrx_buy_img, 0.5, screen)

    wrx_select_img = pygame.image.load('select_btn.png').convert_alpha()
    wrx_select_btn = Button(400, 400, wrx_select_img, 0.5, screen)

    _911_buy_img = pygame.image.load('buy_btn.png').convert_alpha()
    _911_buy_btn = Button(550, 400, _911_buy_img, 0.5, screen)

    _911_select_img = pygame.image.load('select_btn.png').convert_alpha()
    _911_select_btn = Button(650, 400, _911_select_img, 0.5, screen)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                elif event.key == K_m:
                    menu(coins)
                elif event.key == K_p:
                    play()

        cars_bg = pygame.image.load("cars_garage_bg.jpg").convert_alpha()
        screen.blit(cars_bg, (0,0))

        cars_heading = pygame.image.load("cars_page_img.png").convert_alpha()
        screen.blit(cars_heading, (260, 40))

        corolla_img = pygame.image.load('corolla_img.png').convert_alpha()
        screen.blit(corolla_img, (50, 260))

        wrx_img = pygame.image.load('wrx_main.png').convert_alpha()
        screen.blit(wrx_img, (280, 250))

        _911_img = pygame.image.load('911_img.png').convert_alpha()
        screen.blit(_911_img, (510, 240))

        draw_text(f"Price:{all_cars['wrx']['price']}", text_font, (0, 0, 0), 320, 435)
        draw_text(f"Price:{all_cars['911']['price']}", text_font, (0, 0, 0), 580, 435)

        draw_text(f"{all_cars['corolla']['brand']} {all_cars['corolla']['model']}", text_font, (0, 0, 0), 20, 180)
        draw_text(f"{all_cars['wrx']['brand']} {all_cars['wrx']['model']}", text_font, (0, 0, 0), 340, 180)
        draw_text(f"{all_cars['911']['brand']} {all_cars['911']['model']}", text_font, (0, 0, 0), 580, 180)


        # Draw the button and check for clicks
        if play_btn.draw():
            play()
            running = False
        elif menu_btn.draw():
            menu(coins)
            running = False
        # Corolla button
        elif corolla_select_btn.draw():
            price, owned, current = buy_car("corolla gen 12")
            if owned == True:
                current = True
                print("Car selected")
            all_cars["corolla"]["current"] = current
            all_cars["wrx"]["current"] = False
            all_cars["911"]["current"] = False
        # Wrx buttons
        elif wrx_buy_btn.draw():
            price, owned, current = buy_car("wrx sti")
            if owned == True:
                print("You already own this car")
            if total_coins < price:
                print("Not enough coins")
            if owned == False and total_coins >= price:
                owned = True
                total_coins -= price
                print("car bought")
            all_cars["wrx"]["owned"] = owned
        elif wrx_select_btn.draw():
            price, owned, current = buy_car("wrx sti")
            if owned == True:
                current = True
                print("Car selected")
            else:
                print("You don't own this car")
            all_cars["corolla"]["current"] = False
            all_cars["wrx"]["current"] = current
            all_cars["911"]["current"] = False
        # 911 buttons
        elif _911_buy_btn.draw():
            price, owned, current = buy_car("911 GT3 RS")
            if owned == True:
                print("You already own this car")
            if total_coins < price:
                print("Not enough coins")
            if owned == False and total_coins >= price:
                owned = True
                total_coins -= price
                print("car bought")
            all_cars["911"]["owned"] = owned
        elif _911_select_btn.draw():
            price, owned, current = buy_car("911 GT3 RS")
            if owned == True:
                current = True
                print("Car Selected")
            else:
                print("You don't own this car")
            all_cars["corolla"]["current"] = False
            all_cars["wrx"]["current"] = False
            all_cars["911"]["current"] = current

        dollar_sign = pygame.image.load('dollar.png')
        screen.blit(dollar_sign, (0, 455))
        draw_text((str(total_coins)), text_font, (255, 255, 255), 50, 458)

        # Update display
        pygame.display.flip()

    return total_coins, owned, current

print("Welcome to my car game \nKeyboard shortcuts are c for cars, m for menu, p for play \nUse arrows to move car")
menu(coins)

pygame.quit()
