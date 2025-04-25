import pygame
pygame.init()
screen = pygame.display.set_mode((600,700))
TITLE = "Match the Aplications"
run = True
pygame.display.set_caption(TITLE)
sf = pygame.image.load("Subway Surf.png")
tr = pygame.image.load("Temple Run.png")
cc = pygame.image.load("Candy Crush.jpg")
l = pygame.image.load("Ludo.png")


while run == True:
    screen.blit(sf,(100,100))
    screen.blit(tr,(100,250))
    screen.blit(cc,(100,400))
    screen.blit(l,(100,550))
    font_style = pygame.font.SysFont("nunito",25)
    text = font_style.render("Subway Surfers",True,"white")
    screen.blit(text,(350,450))
    text1 = font_style.render("Candy Crush",True,"white")
    screen.blit(text1,(350,600))
    text2 = font_style.render("Ludo",True,"white")
    screen.blit(text2,(350,150))
    text3 = font_style.render("Temple Run",True,"white")
    screen.blit(text3,(350,300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,"white",pos,4)
        if event.type == pygame.MOUSEBUTTONUP:
            pos1 = pygame.mouse.get_pos()
            pygame.draw.circle(screen,"white",pos1,4)
            pygame.draw.line(screen,"white",pos,pos1)

    pygame.display.update()