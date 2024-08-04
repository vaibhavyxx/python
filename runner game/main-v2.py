#changed the idea to just jumping on the sky and avoiding grey clouds
import pygame
import random
import time

pygame.init()
WIDTH, HEIGHT = 1024, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flappy birds")
pygame.mouse.set_visible(False)

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

#uses physics equation for linear motion .i.e, displacement = vel *time
    def update(self):
        self.velocity =-100
        self.tf = time.time()
        dt = self.tf - self.ti
        self.ti = self.tf
        self.pos_x += self.velocity * dt
        self.rect.x = self.pos_x

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
            print(i)

    def update(self):
        self.clouds_group.update()

    def draw(self, screen):
        self.clouds_group.draw(screen)

cloud_manager = Clouds_Manager("runner game/png/white cloud.png", "runner game/png/grey cloud.png")
cloud_manager.make_Clouds(WIDTH, HEIGHT, 5)
run = True
while run:

    #update background
    screen.fill((193,227,255))
    cloud_manager.update()
    cloud_manager.draw(screen)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()