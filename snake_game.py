import pygame
import random
import time

# Khởi tạo pygame
pygame.init()

# Thiết lập màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Kích thước màn hình
WIDTH = 800
HEIGHT = 600

# Kích thước của mỗi ô rắn
SNAKE_BLOCK = 20

# Tốc độ rắn
SNAKE_SPEED = 15

# Khởi tạo màn hình
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rắn săn mồi")

# Thiết lập font chữ
font_style = pygame.font.SysFont("comicsansms", 35)
score_font = pygame.font.SysFont("comicsansms", 25)

# Hàm hiển thị điểm số
def your_score(score):
    value = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])

# Hàm vẽ con rắn
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

# Hàm hiển thị thông báo
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])

# Vòng lặp chính
def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Tọa độ ban đầu của thức ăn
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(BLACK)
            message("Game Over! Press C-Continue or Q-Quit", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # Kiểm tra rắn ra khỏi màn hình
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
# Vẽ thức ăn
        pygame.draw.rect(screen, BLUE, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        # Cập nhật thân rắn
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Kiểm tra va chạm với thân rắn
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Kiểm tra nếu rắn ăn thức ăn
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()

# Bắt đầu game
game_loop()