import pygame
from time import *
from pygame.locals import * 
TITLE = "Rocket in Space"
player_X = 200
player_Y = 200
pygame.init()
screen = pygame.display.set_mode((600,600))
Keys = [False,False,False,False]
player = pygame.image.load("Rocket.png")
background = pygame.image.load("space.png")
while player_Y < 600:
    screen.blit(background,(0,0))
    screen.blit(player,(player_X,player_Y))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                Keys[0] = True
            if event.key == K_LEFT:
                Keys[1] == True
            if event.key == K_RIGHT:
                Keys[2] == True
            if event.key == K_DOWN:
                Keys[3] == True
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                Keys[0] = False
            if event.key == K_LEFT:
                Keys[1] == False
            if event.key == K_RIGHT:
                Keys[2] == False
            if event.key == K_DOWN:
                Keys[3] == False
    
    if Keys [0]:
        if player_Y > 0:
            player_Y -= 7
    elif Keys[2]:
        if player_Y < 536:
            player_Y += 7
    if Keys [1]:
        if player_X > 0:
            player_X -= 2
    elif Keys[3]:
        if player_X < 536:
            player_X += 2
    player_Y += 5
    sleep(0.05)
print("GAME OVER")



           

            

