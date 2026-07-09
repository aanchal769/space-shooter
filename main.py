import pygame

pygame.init()

screen=pygame.display.set_mode((900,800))

pygame.display.set_caption("Space-Shooter")

running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False
    

    
    screen.fill((10,25,60))
    pygame.display.update()


pygame.quit()




