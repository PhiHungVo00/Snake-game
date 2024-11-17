def move(x, y, dx, dy):
    return x + dx, y + dy

def collide_wall(x, y, width, height):
    return x >= width or x < 0 or y >= height or y < 0

def collide_self(snake_list):
    head = snake_list[-1]
    return head in snake_list[:-1]

def eat_food(x, y, foodx, foody, block_size):
    return x == foodx and y == foody
