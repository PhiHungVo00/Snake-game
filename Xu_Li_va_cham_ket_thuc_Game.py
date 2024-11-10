
   # Kiểm tra rắn ra khỏi màn hình
    if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
       game_close = True

   # Kiểm tra va chạm với thân rắn
   for block in snake_list[:-1]:
       if block == snake_head:
           game_close = True

     def message(msg, color):
         mesg = font_style.render(msg, True, color)
         screen.blit(mesg, [WIDTH / 6, HEIGHT / 3])
