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
        
food_pos = generate_food()

#draw object on the screen

def draw_objects():
    win.fill((0, 0, 0))
    for pos in snake_pos:
        pygame.draw.rect(win, WHITE, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(win, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    #Render the score

    score_text = score_font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10,10)) # draws the score on the top left corner

#update snake position

def update_snake():
    global food_pos, score
    new_head = [snake_pos[0][0] + snake_speed[0], snake_pos[0],[1] + snake_speed[1]]

    if teleport_walls:

        # if the new head position is outside of the screen, wrap it to the other side
        if new_head[0] >= WIDTH:
            new_head[0] = 0
        elif new_head[0] < 0 :
            new_head[0] = WIDTH - BLOCK_SIZE
        if new_head[1] >= HEIGHT:
            new_head[1] = 0
        elif new_head[1] < 0:
            new_head[1] = HEIGHT - BLOCK_SIZE
    
    if new_head == food_pos:
        food_pos = generate_food() #generate new food
        score += 1 #increment score when food is eaten
    else:
        snake_pos.pop() #remove the last element from the snake


    snake_pos.insert(0, new_head) #add the new head to the snake

    #game over condition

    def game_over():
        # game over when snake hits the boundaries or runs into itself

        if teleport_walls:
            return snake_pos[0] in snake_pos[1:]
        else:
            return snake_pos[0] in snake_pos[1:] or \
                snake_pos[0][0] > WIDTH - BLOCK_SIZE or \
                snake_pos[0][0] < 0 or \
                snake_pos[0][1] > HEIGHT - BLOCK_SIZE or \
                snake_pos[0][1] < 0
        