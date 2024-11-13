   # Tọa độ ban đầu của thức ăn
    foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    # Vẽ thức ăn
    pygame.draw.rect(screen, BLUE, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
    # Kiểm tra nếu rắn ăn thức ăn
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
        foody = round(random.randrange(0, HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
        length_of_snake += 1
    #Quan ly va hien thi diem
    def your_score(score):
        value = score_font.render(f"Score: {score}", True, WHITE)
        screen.blit(value, [10, 10])
    #Goi ham score
    your_score(length_of_snake - 1)