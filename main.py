import pygame
import random
pygame.init()
WIDTH=800
HEIGHT=600
FPS=120
num_of_obstacles=2
Obstacle_x=[]
Obstacle_y=[]
obstacle_vel=5
gravity=0.25
bird_movement=0
obstacle_rect_list=[]
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")
background=pygame.image.load("download.jpg")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
player=pygame.image.load("player.png")
player=pygame.transform.scale(player,(120,120))
print(player.get_width())
bird_rect=player.get_rect(center=(350,250))
obstacle=pygame.image.load("obstacle.png")
obstacle=pygame.transform.scale(obstacle,(100,200))
for i in range(num_of_obstacles):
    Obstacle_x.append(random.randint(800 * (i + 1) +60, 800 * (i + 2)- 60))
for y in range(num_of_obstacles):
    Obstacle_y.append(random.choice((400,1)))
running=True
def Lose():
    screen.fill((255,255,255))
    background = pygame.image.load("download.jpg")
    Lost = pygame.font.Font("freesansbold.ttf",64)
    background=pygame.transform.scale(background,(WIDTH,HEIGHT))
    Lost_text=Lost.render("You Lost",True,(255,255,255))
    screen.blit(background,(0,0))
    screen.blit(Lost_text,(250,250))
    pygame.display.update()
def obstacles(x, y,obstacle):
    clock=pygame.time.Clock()
    clock.tick(FPS)
    if Obstacle_y[i] == 1:
        obstacle=pygame.transform.rotate(pygame.transform.scale(obstacle,(100,200)),180)
        screen.blit(obstacle,(x,y))
    else:
        obstacle=pygame.transform.scale(obstacle,(100,200))
        screen.blit(obstacle, (x, y))
def collision(obstacle_rect):
    if bird_rect.x+player.get_width()-10>obstacle_rect.x and bird_rect.x+player.get_width()-10<obstacle_rect.x+100-20 or bird_rect.x<obstacle_rect.x+100 and bird_rect.x+5>obstacle_rect.x:
        if obstacle_rect.y==1:
            if bird_rect.y <obstacle_rect.y+200:
                return True
        else:
            if bird_rect.y+player.get_height()-3>obstacle_rect.y:
                return True
    if bird_rect.y+200-100>600:
        return True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bird_movement=0
                bird_movement-=5
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    bird_movement+=gravity
    bird_rect.centery+=bird_movement
    screen.blit(player,bird_rect)
    for i in range(num_of_obstacles):
        obstacles(Obstacle_x[i], Obstacle_y[i], obstacle)
        Obstacle_x[i] -= obstacle_vel
        obstacle_rect=pygame.Rect(Obstacle_x[i],Obstacle_y[i],100,200)
        collision(obstacle_rect)
        if Obstacle_x[i] < -100:
            Obstacle_x[i]
            Obstacle_x[i] = random.randint(800 * (i + 1) -60, 800 * (i + 2) +60)
            Obstacle_y[i] = random.choice((400, 1))
        if collision(obstacle_rect):
            Lose()
            running=False
    pygame.display.update()
pygame.time.delay(3000)
