import pygame  # Thư viện pygame để xử lý giao diện
import random
from ui import draw_snake, draw_food, draw_menu, draw_scoreboard
from logic import move, collide_wall, collide_self, eat_food

pygame.init()  # Khởi tạo pygame

# Thiết lập kích thước màn hình và các biến game
WIDTH, HEIGHT = 800, 600
SNAKE_BLOCK = 20
SNAKE_SPEED = 15
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Thành viên Võ Phi Hùng - Khởi tạo màn hình và các biến ban đầu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def game_loop():
    game_over = False
    game_close = False
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake_list = []
    length_of_snake = 1
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            draw_menu(screen, "Game Over! Press C-Continue or Q-Quit", RED)
            draw_scoreboard(screen, length_of_snake - 1, WHITE)
            pygame.display.update()
