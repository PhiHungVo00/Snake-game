WIDTH, HEIGHT = 800, 600
SNAKE_BLOCK = 20

def move_classic(x,y,dx,dy):
    global WIDTH,HEIGHT
    x = x+dx
    y = y+dy
    if x >= WIDTH:
        x = 0
    elif x < 0:
        x = WIDTH - SNAKE_BLOCK
    
    if y >= HEIGHT:
        y = 0
    elif y < 0:
        y = HEIGHT - SNAKE_BLOCK
    return x,y

def move_modern(x, y, dx, dy):
    return x + dx, y + dy

def collide_wall(x, y, width, height, border_thickness=5):
    return x < border_thickness or x >= width - border_thickness or \
           y < border_thickness or y >= height - border_thickness

def collide_self(snake_list):
    head = snake_list[-1]
    return head in snake_list[:-1]

def eat_food(x, y, foodx, foody, block_size):
    return x == foodx and y == foody





