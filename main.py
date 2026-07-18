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

enemybullet_width=15
enemybullet_height=40


screen=pygame.display.set_mode((screen_width,screen_height))
player=pygame.image.load("assets/images/player.png")
player=pygame.transform.scale(player,(player_width,player_height))
font=pygame.font.Font(None,72)

pygame.display.set_caption("Space-Shooter")


bullet=pygame.image.load("assets/images/bullet.png")
bullet=pygame.transform.scale(bullet,(bullet_width,bullet_height))


enemy=pygame.image.load("assets/images/enemy.png")
enemy=pygame.transform.scale(enemy,(enemy_width,enemy_height))


enemybullet=pygame.image.load("assets/images/enemybullet.png")
enemybullet=pygame.transform.scale(enemybullet,(enemybullet_width,enemybullet_height))
enemy_x=450
enemy_y=50

player_x=700
player_y=650
player_speed=20
bullet_speed=10
bullet_x=player_x+ (player_width//2)-(bullet_width//2)
bullet_y=player_y+(player_height//2)-(bullet_height//2)




enemybullet_x=[]
enemybullet_y=[]
enemybullet_speed=8
enemybullet_state=[]

game_over=False

num_of_enemies=3
enemy_alive=[]
e_x=[]
e_y=[]


for i in range(num_of_enemies):
        enemy_x=random.randint(0,screen_width-enemy_width)
        enemy_y=0

        e_x.append(enemy_x)
        e_y.append(enemy_y)

        enemy_alive.append(True)
        enemybullet_x.append(0)
        enemybullet_y.append(0)
        enemybullet_state.append("ready")


enemy_speed=2
bullet_state="ready"
def ispebcollison(enemybullet_x,enemybullet_y,player_x,player_y):
       distance=math.sqrt((player_x-enemybullet_x)**2+(player_y-enemybullet_y)**2)
       if distance<40:
              return True
       
       return False

def is_ebcollision(enemybullet_x,enemybullet_y,bullet_x,bullet_y):
       distance=math.sqrt((bullet_x-enemybullet_x)**2+(bullet_y-enemybullet_y)**2)
       if distance<20:
              return True
       
       return False

def is_pecollision(enemy_x,enemy_y,player_x,player_y,x):

        distance=math.sqrt((enemy_x-player_x)**2 + (enemy_y-player_y)**2)

        if distance < x:
                return True
        
        return False


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

        for i in range(num_of_enemies):

                if enemy_alive[i]:
                   e_y[i]+=enemy_speed

                   if e_y[i]>screen_height:
                        e_y[i]=0

                        e_x[i]=random.randint(0,screen_width-enemy_width)

def fire_enemy_bullet():
      
             for i in range(num_of_enemies):
                if enemybullet_state[i]=="ready"  and  enemy_alive[i]:
                   
                      enemybullet_x[i]=e_x[i]+(enemy_width//2)-(enemybullet_width//2)
                      enemybullet_y[i]=e_y[i]+(enemy_height)

                      enemybullet_state[i]="fire"


def move_enemy_bullet():
       
             for i in range (num_of_enemies):
                if enemybullet_state[i]=="fire"   and enemy_alive[i]:
                    enemybullet_y[i]+=enemybullet_speed
                     

                    if enemybullet_y[i]>screen_height:
                       enemybullet_state[i]="ready"
                       
                        
def draw_enemy_bullet():
       for i in range(num_of_enemies):
              if(enemy_alive[i] and enemybullet_state[i]=="fire"):
                     screen.blit(enemybullet,(enemybullet_x[i],enemybullet_y[i]))


def isenemycollisiion():
       global score,game_over
       for i in range(num_of_enemies):
              if enemy_alive[i] and bullet_state=="fire" and enemybullet_state[i]=="fire" :
                     if is_ebcollision(enemybullet_x[i],enemybullet_y[i],bullet_x,bullet_y):
                            score+=1
                            reset_bullet()
                            enemybullet_state[i]="ready"
                            enemybullet_x[i]=0
                            enemybullet_y[i]=0
                            enemy_alive[i]=False
                            break
                            


              if enemy_alive[i]  and ispebcollison(enemybullet_x[i],enemybullet_y[i],player_x,player_y):
                     game_over=True
                     break
                     
                     
def show_score(score):
        
        score_text=font.render(f"Score: {score}",True,(255,0,0))
        screen.blit(score_text,(10,10))



def draw_game():
        screen.blit(player,(player_x,player_y))
        for i in range(num_of_enemies):
           if enemy_alive[i]:
              screen.blit(enemy,(e_x[i],e_y[i]))

        if bullet_state=="fire":
            screen.blit(bullet,(bullet_x,bullet_y))
        

        

def check_game_over():
        global game_over

        for i in range(num_of_enemies):
                if is_pecollision(e_x[i],e_y[i],player_x,player_y,70):
                        game_over=True
                        break

        
def show_game_over():
        game_over_text=font.render("GAME OVER",True,(255,0,0))

        screen.blit(game_over_text,(250,350))     

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


    if not game_over:
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
    
   
        for i in range(num_of_enemies):
            
           if enemy_alive[i]  and is_collision(e_x[i],e_y[i],bullet_x,bullet_y) :
            
               score+=1
               print(score)
               reset_bullet()
               enemy_alive[i]=False
               e_y[i]=0
               e_x[i]=random.randint(0,screen_width-enemy_width)
               
               break
           

        check_game_over()
        fire_enemy_bullet()
        move_enemy_bullet()
        isenemycollisiion()
        draw_enemy_bullet()
    show_score(score)
    
    draw_game()

    


    if game_over:
            show_game_over() 
    
    clock.tick(30)
    pygame.display.update()


pygame.quit()




