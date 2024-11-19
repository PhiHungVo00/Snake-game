import pygame

def draw_snake(screen, snake_list, block_size, color):
    for block in snake_list:
        pygame.draw.rect(screen, color, [block[0], block[1], block_size, block_size])

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
