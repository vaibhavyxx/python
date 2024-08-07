#changed the idea to just jumping on the sky and avoiding grey clouds
#to do- add event management, scoring, ui buttons, sound
import pygame
import random
import time

pygame.init()
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flappy birds")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

#loads all the assets
bird_fly = []
bird_fly.append(pygame.image.load("runner game/png/PNG/SMALL/BirdS_0000_Capa-1.png"))
bird_fly.append(pygame.image.load("runner game/png/PNG/SMALL/BirdS_0001_Capa-2.png"))
bird_fly.append(pygame.image.load("runner game/png/PNG/SMALL/BirdS_0002_Capa-3.png"))
bird_fly.append(pygame.image.load("runner game/png/PNG/SMALL/BirdS_0003_Capa-0.png"))
plane_fly = []
plane_fly.append(pygame.image.load("runner game/png/PNG/Plane/Fly (1).png"))
plane_fly.append(pygame.image.load("runner game/png/PNG/Plane/Fly (2).png"))
plane_dead = pygame.image.load("runner game/png/PNG/Plane/Dead (1).png")

class Plane(pygame.sprite.Sprite):
    def __init__(self, plane_fly_list, scale, gravity):
        super().__init__()
        self.current_frame =0
        self.image = plane_fly_list[self.current_frame]
        self.new_width = scale * self.image.get_width()
        self.new_height = scale * self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.new_width, self.new_height))
        self.rect = self.image.get_rect()
        self.pos_x = WIDTH/2 - self.image.get_width()/2
        self.pos_y = HEIGHT/2 - self.image.get_height()/2
        self.rect.topleft = [self.pos_x, self.pos_y]
        self.gravity = gravity
        self.ti = time.time()                           #for movement
        self.start_time = time.time()                   #for animation

#uses physics equation: h = ut for gravity and falls down when there is no input
    def update(self):
        self.plane_animation()

        vert_speed = 0
        keys = pygame.key.get_pressed()
        self.tf = time.time()
        dt = self.tf - self.ti

        if keys[pygame.K_w]:
            vert_speed = 1000
        self.pos_y -= vert_speed * dt
        self.pos_y -= self.gravity * dt 
        self.ti = self.tf
        self.rect.y = self.pos_y

    #shows bird animation
    def plane_animation(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
 
        if elapsed_time > 0.5:  
            self.current_frame += 1
            self.start_time = current_time
            if self.current_frame >= len(plane_fly):
                self.current_frame = 0
        self.image = plane_fly[self.current_frame]

#cloud class
class Cloud(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y, scale):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.new_width = scale * self.image.get_width()
        self.new_height = scale * self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.new_width, self.new_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ti = time.time()

#uses physics equation for linear motion .i.e, displacement = vel *time and kills itself if you go offscreen
    def update(self):
        self.velocity =-100
        self.tf = time.time()
        dt = self.tf - self.ti
        self.ti = self.tf
        self.pos_x += self.velocity * dt
        self.rect.x = self.pos_x

        if self.rect.x < -500:
            self.kill()

#instantiating cloud- making a manager class to decide its size, position, color, etc.
class Clouds_Manager(pygame.sprite.Sprite):
    def __init__(self, picture_path_A, picture_path_B):
        super().__init__()
        self.picture_path_A = picture_path_A        #image directory for white clouds
        self.picture_path_B = picture_path_B        #image directory for grey cloudss
        self.clouds_group = pygame.sprite.Group()

    #randomly gives coordinates, scale, cloud color and adds it to the list
    def make_Clouds(self, screen_width, screen_height, num_of_clouds):
        for i in range(num_of_clouds):
            x = random.randrange(screen_width, screen_width + 200)      #1024, 1224
            y = random.randrange(0, screen_height -100)                 # 0, 629
            scale = random.uniform(0.1, 0.4)
            picture_path = self.picture_path_A                          #default color of the clouds is white
            choose_color = random.randrange(0,5)
            if choose_color > 3: picture_path = self.picture_path_B
            cloud = Cloud(picture_path, x, y, scale)
            self.clouds_group.add(cloud)

    def update(self):
        self.clouds_group.update()

    def draw(self, screen):
        self.clouds_group.draw(screen)

#for birds
class Bird(pygame.sprite.Sprite):
    def __init__(self, bird_fly_list, pos_x, pos_y, scale, vel):
        super().__init__()
        self.current_frame = 0
        self.image = bird_fly_list[self.current_frame]
        self.new_width = scale * self.image.get_width()
        self.new_height = scale * self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.new_width, self.new_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocity = vel
        self.ti = time.time()                #for movement
        self.start_time = time.time()        #for animation

#uses physics equation for linear motion .i.e, displacement = vel *time and kills itself if you go offscreen
    def update(self):
        self.bird_animation()

        tf = time.time()
        dt = tf - self.ti
        self.ti = tf
        self.pos_x += self.velocity * dt
        self.rect.x = self.pos_x

        if self.rect.x < -200:
            self.kill()

    #shows bird animation
    def bird_animation(self):
        current_time = time.time()
        elapsed_time = current_time - self.start_time
 
        if elapsed_time > 0.1:  
            self.current_frame += 1
            self.start_time = current_time
            if self.current_frame >= len(bird_fly):
                self.current_frame = 0
        self.image = bird_fly[self.current_frame]

#instantiating cloud- making a manager class to decide its size, position, color, etc.
class Bird_Manager(pygame.sprite.Sprite):
    def __init__(self, bird_fly_list):
        super().__init__()
        self.bird_fly_list = bird_fly_list
        self.bird_group = pygame.sprite.Group()

    #randomly gives coordinates, speed and number of birds
    def make_Birds(self, screen_width, screen_height):
        num_of_birds = random.randrange(0, 6)
        for i in range(num_of_birds):
            x = random.randrange(screen_width, screen_width + 200)      
            y = random.randrange(0, screen_height -50)                 
            speed = random.randrange(-700, -400)
            bird = Bird(self.bird_fly_list, x, y, 1, speed)
            self.bird_group.add(bird)

    def update(self):
        self.bird_group.update()

    def draw(self, screen):
        self.bird_group.draw(screen)

#objects
cloud_manager = Clouds_Manager("runner game/png/white cloud.png", "runner game/png/grey cloud.png")
cloud_manager.make_Clouds(WIDTH, HEIGHT, 5)
player = Plane(plane_fly,0.01, -200)
player_group = pygame.sprite.Group()
player_group.add(player)
bird_manager = Bird_Manager(bird_fly)
cloud_manager.make_Clouds(WIDTH, HEIGHT, 5)

run = True
#fills the screen with new clouds after every 2 seconds
while run:
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time    #gives time in mills

    if(elapsed_time > 2000):
        num = random.randrange(0, 5)
        cloud_manager.make_Clouds(WIDTH, HEIGHT, num)
        bird_manager.make_Birds(WIDTH, HEIGHT)
        start_time = current_time

    #update background
    screen.fill((193,227,255))

    cloud_manager.update()
    cloud_manager.draw(screen)
    player_group.update()
    player_group.draw(screen)
    bird_manager.update()
    bird_manager.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if pygame.sprite.spritecollide(player, bird_manager.bird_group, False):
            #run = False
            pass
            
    pygame.display.update()
pygame.quit()