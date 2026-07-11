import pygame

pygame.init()


screen_width=1000
screen_height=800

player_width=100
player_height=100




bullet_width=15
bullet_height=40
screen=pygame.display.set_mode((screen_width,screen_height))
player=pygame.image.load("assets/images/player.png")
player=pygame.transform.scale(player,(player_width,player_height))


pygame.display.set_caption("Space-Shooter")


bullet=pygame.image.load("assets/images/bullet.png")
bullet=pygame.transform.scale(bullet,(bullet_width,bullet_height))




player_x=700
player_y=650
player_speed=20
bullet_speed=15
bullet_x=player_x+ (player_width//2)-(bullet_width//2)
bullet_y=player_y+(player_height//2)-(bullet_height//2)

bullet_state="ready"
clock=pygame.time.Clock()

running=True

while running:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        
        if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                        if(bullet_state=="ready"):
                                bullet_state="fire"
                                bullet_x=player_x+ (player_width//2)-(bullet_width//2)
                                bullet_y=player_y+(player_height//2)-(bullet_height//2)

    if bullet_state=="fire":
                bullet_y-=bullet_speed

    if bullet_y<0:
            bullet_state="ready"
            bullet_y=bullet_y
            bullet_x=bullet_x
        
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
    screen.blit(bullet,(bullet_x,bullet_y))

    
    
    clock.tick(30)
    pygame.display.update()


pygame.quit()




