import pygame  # Thư viện pygame để xử lý giao diện
import random
from ui import draw_snake, draw_food, draw_menu, draw_scoreboard
from logic import move, collide_wall, collide_self, eat_food
from music import play_background_music, play_eat_sound
pygame.init()  # Khởi tạo pygame
play_background_music()
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
# Thành viên Nguyễn Tuấn Kiệt - Xử lý kết thúc game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -SNAKE_BLOCK, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = SNAKE_BLOCK, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -SNAKE_BLOCK
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, SNAKE_BLOCK

        x, y = move(x, y, dx, dy)
        if collide_wall(x, y, WIDTH, HEIGHT) or (len(snake_list) > 1 and collide_self(snake_list)):
            game_close = True

        screen.fill(BLACK)
        draw_food(screen, foodx, foody, SNAKE_BLOCK)
        draw_snake(screen, snake_list, SNAKE_BLOCK, GREEN)
        draw_scoreboard(screen, length_of_snake - 1, WHITE)
        pygame.display.update()

        if eat_food(x, y, foodx, foody, SNAKE_BLOCK):
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            length_of_snake += 1
            play_eat_sound()

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

game_loop()
