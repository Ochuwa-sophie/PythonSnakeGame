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