import pygame
import sys
import random

class Snake:
    def __init__(self, x, y):
        self.snake = [(x, y)]
        self.direction = 'RIGHT'
        self.length = 1

    def move_snake(self):
        if self.direction == 'RIGHT':
            new_head = (self.snake[-1][0] + 20, self.snake[-1][1])
        elif self.direction == 'LEFT':
            new_head = (self.snake[-1][0] - 20, self.snake[-1][1])
        elif self.direction == 'UP':
            new_head = (self.snake[-1][0], self.snake[-1][1] - 20)
        else:
            new_head = (self.snake[-1][0], self.snake[-1][1] + 20)

        self.snake.append(new_head)
        if len(self.snake) > self.length:
            self.snake.pop(0)

    def check_collision(self, width, height):
        head = self.snake[-1]
        if head in self.snake[:-1] or head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
            return True
        return False

    def eat_food(self, food_position):
        if self.snake[-1] == food_position:
            self.length += 1
            return True
        return False

class Food:
    def __init__(self, width, height):
        self.position = [random.randrange(1, (width // 20)) * 20, random.randrange(1, (height // 20)) * 20]

    def reset_position(self, width, height):
        self.position = [random.randrange(1, (width // 20)) * 20, random.randrange(1, (height // 20)) * 20]

def draw_snake(snake_positions):
    for pos in snake_positions:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

def game_over():
    my_font = pygame.font.SysFont("monospace", 75)
    game_over_surface = my_font.render("游戏结束", True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
snake_size = 20
snake_speed = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()

snake = Snake(100, 100)
food = Food(WIDTH, HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

       keys = pygame.key.get_pressed()
for key in keys:
if keys[pygame.K_UP] or keys[pygame.K_w]:
if snake.direction != 'DOWN':
snake.direction = 'UP'
if keys[pygame.K_DOWN] or keys[pygame.K_s]:
if snake.direction != 'UP':
snake.direction = 'DOWN'
if keys[pygame.K_LEFT] or keys[pygame.K_a]:
if snake.direction != 'RIGHT':
snake.direction = 'LEFT'
if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
if snake.direction != 'LEFT':
snake.direction = 'RIGHT'

snake.move_snake()

if snake.check_collision(WIDTH, HEIGHT):
game_over()

if snake.eat_food(food.position):
food.reset_position(WIDTH, HEIGHT)

screen.fill(WHITE)
draw_snake(snake.snake)
pygame.draw.rect(screen, RED, pygame.Rect(food.position[0], food.position[1], snake_size, snake_size))
pygame.display.flip()
clock.tick(snake_speed)
