def move(x, y, dx, dy):
    return x + dx, y + dy

def collide_wall(x, y, width, height, border_thickness=5):
    return x < border_thickness or x >= width - border_thickness or \
           y < border_thickness or y >= height - border_thickness

def collide_self(snake_list):
    head = snake_list[-1]
    return head in snake_list[:-1]

def eat_food(x, y, foodx, foody, block_size):
    return x == foodx and y == foody
