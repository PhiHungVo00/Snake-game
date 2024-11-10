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

   # Khởi tạo màn hình
   screen = pygame.display.set_mode((WIDTH, HEIGHT))
   pygame.display.set_caption("Rắn săn mồi")
   # Thiết lập font chữ
   font_style = pygame.font.SysFont("comicsansms", 35)
   score_font = pygame.font.SysFont("comicsansms", 25)
def game_loop():
       game_over = False
       game_close = False

       # Các biến khởi tạo vị trí của rắn
       x1 = WIDTH / 2
       y1 = HEIGHT / 2

       x1_change = 0
       y1_change = 0

       # Danh sách lưu thân rắn
       snake_list = []
       length_of_snake = 1

       # Khởi tạo clock để điều khiển tốc độ game
       clock = pygame.time.Clock()

       while not game_over:
           # Xử lý khi game kết thúc
           while game_close:
               # Hiển thị màn hình game over (phối hợp với Thành viên 4)
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
  # Thành viên 4 sẽ hoàn thiện phần này

           # Xử lý sự kiện (phối hợp với Thành viên 2)
           pass  # Thành viên 2 sẽ hoàn thiện phần này

           # Cập nhật vị trí của rắn (phối hợp với Thành viên 2)
           pass  # Thành viên 2 sẽ hoàn thiện phần này

           # Vẽ màn hình và các thành phần (phối hợp với Thành viên 3)
           pass  # Thành viên 3 sẽ hoàn thiện phần này

           # Kiểm tra va chạm và cập nhật game (phối hợp với Thành viên 4)
            x1 += x1_change
            y1 += y1_change

            # Kiểm tra rắn ra khỏi màn hình
            if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
            # Cập nhật thân rắn
            nake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
            del snake_list[0]

            # Kiểm tra va chạm với thân rắn
            for block in snake_list[:-1]:
            if block == snake_head:
            game_close = True
            def message(msg, color):
            mesg = font_style.render(msg, True, color)
            screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])
            
            def your_score(score):
            value = score_font.render(f"Score: {score}", True, WHITE)
            screen.blit(value, [10, 10])

              # Thành viên 4 sẽ hoàn thiện phần này

           clock.tick(SNAKE_SPEED)

       pygame.quit()
       quit()
   # Bắt đầu game
   game_loop()
