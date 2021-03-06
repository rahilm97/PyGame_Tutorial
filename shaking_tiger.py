'''
Name: Rahil Mehta
This code is based on the following tutorial, with a different image and added sound:
https://www.pygame.org/docs/tut/PygameIntro.html
'''
import sys
import pygame
from pygame import mixer

pygame.init()
mixer.init()
mixer.music.load('tigers-roaring.mp3')

size = width, height = 580, 680
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

tiger = pygame.image.load("tiger.png")
tigerrect = tiger.get_rect()

# Set preferred volume
mixer.music.set_volume(0.2)

# Play the music
mixer.music.play()
status = 1 # 1 = active, -1 = paused
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_p: 
                status = -status
    
    if status == -1: 
        mixer.music.pause()
    if status == 1:
        mixer.music.unpause()
        tigerrect = tigerrect.move(speed)
    if tigerrect.left < 0 or tigerrect.right > width:
        speed[0] = -speed[0]
    if tigerrect.top < 0 or tigerrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(tiger, tigerrect)
    pygame.display.flip()
