import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
screen.fill(White)
pygame.display.update()
class Rect:
   def __init__(self,color,dimensions): 
      self.rect_surf = screen
      self.rect_color = color
      self.rect_dimesions = dimensions
   def draw(self):
      self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimesions)

greenRect = Rect(Green,(50,20,100,100))
redRect = Rect(Red,(150,200,150,150))
blueRect = Rect(Blue,(300,400,200,200))
greenRect.draw()
redRect.draw()
blueRect.draw()



pygame.display.update()
running = True
while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
pygame.quit()
