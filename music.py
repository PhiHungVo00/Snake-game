import pygame

def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load("back_ground.mp3")  
    pygame.mixer.music.set_volume(0.4) 
    pygame.mixer.music.play(-1) 

def play_eat_sound():
    eat_sound = pygame.mixer.Sound("eat.mp3") 
    eat_sound.set_volume(0.8)  
    eat_sound.play()