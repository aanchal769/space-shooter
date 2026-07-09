import pygame

pygame.init()

screen=pygame.display.set_mode((1000,800))
player=pygame.image.load("assets/images/player.png")
player=pygame.transform.scale(player,(100,100))
pygame.display.set_caption("Space-Shooter")

player_x=700
player_y=650
player_speed=20
running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                player_x+=10

            if event.key==pygame.K_LEFT:
                player_x-=10

            if event.key==pygame.K_UP:
                player_y-=10

            if event.key==pygame.K_DOWN:
                player_y+=10
    
    
    screen.fill((10,25,60))
    screen.blit(player,(player_x,player_y))
    
    pygame.display.update()


pygame.quit()




