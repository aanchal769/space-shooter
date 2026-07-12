import pygame
import random
import math

pygame.init()


screen_width=1000
screen_height=800

player_width=100
player_height=100




bullet_width=15
bullet_height=40

enemy_width=80
enemy_height=80


screen=pygame.display.set_mode((screen_width,screen_height))
player=pygame.image.load("assets/images/player.png")
player=pygame.transform.scale(player,(player_width,player_height))
font=pygame.font.Font(None,72)

pygame.display.set_caption("Space-Shooter")


bullet=pygame.image.load("assets/images/bullet.png")
bullet=pygame.transform.scale(bullet,(bullet_width,bullet_height))


enemy=pygame.image.load("assets/images/enemy.png")
enemy=pygame.transform.scale(enemy,(enemy_width,enemy_height))

enemy_x=450
enemy_y=50

player_x=700
player_y=650
player_speed=20
bullet_speed=15
bullet_x=player_x+ (player_width//2)-(bullet_width//2)
bullet_y=player_y+(player_height//2)-(bullet_height//2)

enemy_speed=5
bullet_state="ready"


def reset_bullet():
        global bullet_x,bullet_y,bullet_state

        bullet_state="ready"

        bullet_x=player_x+(player_width//2) -(bullet_width//2)

        bullet_y=player_y +(player_height//2)- (bullet_height//2)

def fire_bullet():

        global bullet_state,bullet_x,bullet_y

        if bullet_state=="ready":
                print("bullet fired!")
                bullet_state="fire"

                bullet_x=player_x+(player_width//2)-(bullet_width//2)

                bullet_y=player_y+(player_height//2)-(bullet_height//2)

def is_collision(enemy_x,enemy_y,bullet_x,bullet_y):
        
        distance=math.sqrt((enemy_x-bullet_x)**2+(enemy_y-bullet_y)**2)
       
       
        if distance<55:
                
                return True
        
        return False

def move_bullet():
        global bullet_y

        if bullet_state=="fire":
                bullet_y-=bullet_speed

        if bullet_y<0:
                reset_bullet()


def move_enemy():
        global enemy_y,enemy_x

        enemy_y+=enemy_speed

        if enemy_y>screen_height:
                enemy_y=0

                enemy_x=random.randint(0,screen_width-enemy_width)
    


def show_score(score):
        
        score_text=font.render(f"Score: {score}",True,(255,0,0))
        screen.blit(score_text,(10,10))



def draw_game():
        screen.blit(player,(player_x,player_y))
    
        screen.blit(enemy,(enemy_x,enemy_y))

        if bullet_state=="fire":
            screen.blit(bullet,(bullet_x,bullet_y))

score=0
clock=pygame.time.Clock()

running=True

while running:
    screen.fill((10,25,60))

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False

        
        if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                       fire_bullet()



    move_bullet()
        
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
    

    
    move_enemy()
    
   

    if is_collision(enemy_x,enemy_y,bullet_x,bullet_y) :
            print("Collision!")

            score+=1
            print(score)
            bullet_state="ready"
            
            bullet_y=player_y+(player_height//2)-(bullet_height//2)
            bullet_x=player_x+ (player_width//2)-(bullet_width//2)
            enemy_y=0
            enemy_x=random.randint(0,screen_width-enemy_width)
            
    show_score(score)
    
    draw_game()
    
   

    
    clock.tick(30)
    pygame.display.update()


pygame.quit()




