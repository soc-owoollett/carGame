import pygame
pygame.init()

active = True
running = True

# Screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


# Variables
FPS = 60
invulnerable = 10
collecting = 50

x, y = 100, 100
move_x, move_y = 0, 0

width = 10
height = 10

text_font = pygame.font.SysFont("Arial", 30)

score = 3
coins = 0
total_coins = 0

# Obstacles
obstaclesx = [800,800,800,800]
obstaclesy = [90,400,90,200] # in line coordinates - 90, 200, 290, 400

# Coins
coinx = [550,775]
coiny = [200,290]

obstacles_speed = 8

# Cars
all_cars = {
  "911" : {
    "brand" : "porsche",
    "model" : "911 GT3 RS",
    "year": "2022",
    "speed": 15,
    "delay": 0,
    "price": 2,
    "owned": False,
    "current": False,
    "car_img": '911_car.png',
    "dmg_1": '911_dmg_1.png',
    "dmg_2": '911_dmg_2.png',
    "dmg_3": '911_dmg_3.png'
  },
  "wrx" : {
    "brand" : "subaru",
    "model" : "wrx sti",
    "year": "2013",
    "speed": 10,
    "delay": 10,
    "price": 50,
    "owned": False,
    "current": False,
    "car_img": 'wrx_car.png',
    "dmg_1": 'wrx_dmg_1.png',
    "dmg_2": 'wrx_dmg_2.png',
    "dmg_3": 'wrx_dmg_3.png'
  },
  "corolla" : {
    "brand" : "toyota",
    "model" : "corolla gen 12",
    "year": "2013",
    "speed": 8,
    "delay": 20,
    "price": 40,
    "owned": True,
    "current": True,
    "car_img": 'corolla_car.png',
    "dmg_1": 'corolla_dmg_1.png',
    "dmg_2": 'corolla_dmg_2.png',
    "dmg_3": 'corolla_dmg_3.png'
  }
}
