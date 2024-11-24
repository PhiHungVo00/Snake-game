import pygame
import sys

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255,0,0)

SNAKE_SPEED = 5
SNAKE_COLOR = GREEN
GAME_MODE = 'classic'

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game Menu")
# Font chữ
font = pygame.font.Font(None, 50)

#UI- Nguyen Quoc Cuong
def draw_snake(screen, snake_list, block_size, color):
    if snake_list:
        # Vẽ đầu (màu vàng)
        head = snake_list[-1]
        pygame.draw.rect(screen, WHITE, [head[0], head[1], block_size, block_size])  # Đầu màu vàng

        # Vẽ thân (màu xanh)
        for block in snake_list[:-1]:
            pygame.draw.rect(screen, color, [block[0], block[1], block_size, block_size])  # Thân màu xanh lá cây

def draw_food(screen, foodx, foody, block_size):
    pygame.draw.rect(screen, (255, 0, 0), [foodx, foody, block_size, block_size])

def draw_menu(screen, message, color):
    font = pygame.font.Font(None, 35)
    mesg = font.render(message, True, color)
    screen.blit(mesg, [100, 100])

def draw_scoreboard(screen, score, color):
    font = pygame.font.Font(None, 25)
    value = font.render(f"Score: {score}", True, color)
    screen.blit(value, [10, 10])


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def main_menu():
    global SNAKE_SPEED
    while True:
        screen.fill(BLACK)
        draw_text("Main Menu", font, WHITE, screen, WIDTH // 2, 80)

        options = ["1. Play New Game", "2. HighScore", "3. Setting", "4. Quit"]
        for idx, option in enumerate(options):
            draw_text(option, font, WHITE, screen, WIDTH // 2, 200 + idx * 80)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Chạy game mới
                    return True
                elif event.key == pygame.K_2:
                    high_score()
                elif event.key == pygame.K_3:
                    settings()
                elif event.key == pygame.K_4:
                    pygame.quit()
                    sys.exit()



def high_score():
    screen.fill(BLACK)
    draw_text("High Scores", font, WHITE, screen, WIDTH // 2, 80)

    scores = load_high_scores()
    for idx, score in enumerate(scores):
        draw_text(f"{idx + 1}. {score}", font, WHITE, screen, WIDTH // 2, 200 + idx * 60)
    
    draw_text("Press B to go back", font, WHITE, screen, WIDTH // 2, 500)
    pygame.display.update()
    
    wait_for_key(pygame.K_b)


def save_high_scores(new_score, filename="highscore.txt"):
    scores = load_high_scores(filename)
    scores.append(new_score)
    scores = sorted(scores, reverse=True)[:5]  # Lưu top 5
    with open(filename, "w") as file:
        for score in scores:
            file.write(f"{score}\n")


def load_high_scores(filename="highscore.txt"):
    try:
        with open(filename, "r") as file:
            scores = [int(line.strip()) for line in file.readlines()]
        return sorted(scores, reverse=True)
    except FileNotFoundError:
        return [0] * 5  # Mặc định 5 điểm 0 nếu file chưa tồn tại

def settings():
    while True:
        screen.fill(BLACK)
        draw_text("Settings", font, WHITE, screen, WIDTH // 2, 80)
        options = ["1. Choose Level", "2. Choose Mode", "3. Choose Color", "4. Back"]
        for idx, option in enumerate(options):
            draw_text(option, font, WHITE, screen, WIDTH // 2, 200 + idx * 80)
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choose_level()
                elif event.key == pygame.K_2:
                    choose_mode()
                elif event.key == pygame.K_3:
                    choose_color()
                elif event.key == pygame.K_4:
                    return

def choose_level():
    global SNAKE_SPEED
    screen.fill(BLACK)
    draw_text("Choose Level", font, WHITE, screen, WIDTH // 2, 80)
    levels = ["1. Easy", "2. Normal", "3. Difficult"]
    for idx, level in enumerate(levels):
        draw_text(level, font, WHITE, screen, WIDTH // 2, 200 + idx * 80)
    draw_text("Press B to go back", font, WHITE, screen, WIDTH // 2, 500)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    SNAKE_SPEED = 5
                elif event.key == pygame.K_2:
                    SNAKE_SPEED = 10
                elif event.key == pygame.K_3:
                    SNAKE_SPEED = 15
                elif event.key == pygame.K_b:
                    return

def get_SNAKE_SPEED():
    return SNAKE_SPEED

def choose_mode():
    global GAME_MODE
    screen.fill(BLACK)
    draw_text("Choose Mode", font, WHITE, screen, WIDTH // 2, 80)
    modes = ["1. Classic", "2. Modern"]
    for idx, mode in enumerate(modes):
        draw_text(mode, font, WHITE, screen, WIDTH // 2, 200 + idx * 80)
    
    draw_text("Press B to go back", font, WHITE, screen, WIDTH // 2, 400)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    GAME_MODE = 'classic'
                elif event.key == pygame.K_2:
                    GAME_MODE = 'modern'
                elif event.key == pygame.K_b:
                    return
                
def get_GAME_MODE():
    return GAME_MODE

def choose_color():
    global SNAKE_COLOR
    screen.fill(BLACK)
    draw_text("Choose Color", font, WHITE, screen, WIDTH // 2, 80)
    colors = ["1. Green", "2. Purple", "3. Yellow"]
    for idx, color in enumerate(colors):
        draw_text(color, font, WHITE, screen, WIDTH // 2, 200 + idx * 80)

    draw_text("Press B to go back", font, WHITE, screen, WIDTH // 2, 500)
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    SNAKE_COLOR = GREEN
                elif event.key == pygame.K_2:
                    SNAKE_COLOR = PURPLE
                elif event.key == pygame.K_3:
                    SNAKE_COLOR = YELLOW
                elif event.key == pygame.K_b:
                    return

def get_SNAKE_COLOR():
    return SNAKE_COLOR

def wait_for_key(key):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == key:
                return

if __name__ == "__main__":
    main_menu()
