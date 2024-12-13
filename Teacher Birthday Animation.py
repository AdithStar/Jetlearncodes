import pygame
import time

pygame.init()

HEIGHT = 600
WIDTH = 600

display_surface = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Happy Belated Birthday to you!!!!!")

img = pygame.image.load("Card.jpg")
image = pygame.transform.scale(img,(WIDTH,HEIGHT))
while True:
    font = pygame.font.SysFont("Times New Roman", 72)
    text = font.render("Happy",True,(0,0,0))
    text1 = font.render("Belated",True,(0,0,0))
    text2 = font.render("Birthday",True,(0,0,0))
 
    

    display_surface.fill((255,255,255))
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(180,232))
    display_surface.blit(text1,(264,290))
    display_surface.blit(text2,(189,370))
  

   

    pygame.display.update()
    time.sleep(2)








