# import necessary libraries
import pygame
import random

# setting up some initial parameters

WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20

#colour definition
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.font.init()
score_font = pygame.font.SysFont("consolas", 20)
score = 0

pygame.init()

#setting up display
win = pygame.display.set_mode((WIDTH, HEIGHT))

#setting up the clock
clock = pygame.time.Clock()

# snake and food initialization
snake_pos = [[WIDTH//2, HEIGHT//2]]
snake_speed = [0, BLOCK_SIZE]

teleport_walls = True #set to true to enable Wall teleporting

# generate food position
def generate_food():
    while True:
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE ) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_pos = [x, y]
        if food_pos not in snake_pos:
            return food_pos