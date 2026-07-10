import pygame

pygame.init()


screen_width=1000
screen_height=800

player_width=100
player_height=100


screen=pygame.display.set_mode((screen_width,screen_height))
player=pygame.image.load("assets/images/player.png")
player=pygame.transform.scale(player,(player_width,player_height))
pygame.display.set_caption("Space-Shooter")

player_x=700
player_y=650
player_speed=20
clock=pygame.time.Clock()

running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
               player_x += player_speed

    if keys[pygame.K_LEFT]:
               player_x -= player_speed

    if keys[pygame.K_UP]:
               player_y -= player_speed

    if keys[pygame.K_DOWN]:
                player_y += player_speed
    if player_x<0:
                player_x=0

    if player_y<0:
                player_y=0

    if player_x > screen_width-player_width:
                player_x=screen_width-player_width

    if player_y > screen_height-player_height:
                player_y=screen_height-player_height
    
    
    screen.fill((10,25,60))
    screen.blit(player,(player_x,player_y))
    clock.tick(30)
    pygame.display.update()


pygame.quit()




