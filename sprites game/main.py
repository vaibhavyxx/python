#to learn how sprites work have to be drawn in a group only
#shoot 60 logos in 60 seconds to win
import pygame, sys
import random
pygame.display.set_caption("Shump")

pygame.init()

#crosshair
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path, sound_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound(sound_path)

    def shoot(self):
        self.gunshot.play()
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

#targets
#init overrides parents class init function
class Target(Crosshair):
    def __init__(self, picture_path, sound_path, x, y):
        super().__init__(picture_path, sound_path)
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        
    def shoot(self):
        self.gunshot.play()

    #to avoid it following mouse position
    def update(self):
        self.rect.center = [50, 50]

SCREEN_WIDTH, SCREEN_HEIGHT= 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT_COLOR = (119, 110, 101)
FONT = pygame.font.SysFont("Arial", 36)

#assets and scaling them accordingly
background = pygame.image.load("sprites game/img/background.jpg")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

#disable mouse
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

#crosshair
crosshair = Crosshair("sprites game/img/circle-01.png", "sprites game/sound/gunshot.wav")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

#target
targets_group = pygame.sprite.Group()
start_time = pygame.time.get_ticks()
total_time = 60*1000

#creates targets 
def createTargets(num):
    for i in range(num):
        x = random.randrange(0, SCREEN_WIDTH-50)
        y =  random.randrange(0, SCREEN_HEIGHT-50)
        target = Target("sprites game/img/ct logo.png", "sprites game/sound/pop.ogg", x, y)
        targets_group.add(target)

for i in range(5):
    x = random.randrange(0, SCREEN_WIDTH-50)
    y =  random.randrange(0, SCREEN_HEIGHT-50)
    target = Target("sprites game/img/ct logo.png", "sprites game/sound/pop.ogg", x, y)
    targets_group.add(target)

timer =0
total_time =60*1000
#you can't remove from a group directly, you would have to add it to a list and then access that value
while True:
    current_time = pygame.time.get_ticks()
    time_left = current_time - start_time
    total_time -= time_left

    if total_time ==0:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #for every target you shoot, two more are created
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()
            to_remove = []
            for target in targets_group:
                if crosshair.rect.colliderect(target.rect):
                    target.shoot()
                    to_remove.append(target)
                
            for target in to_remove:
                targets_group.remove(target)
                createTargets(1)

    screen.blit(background,(0,0))
    time_text = FONT.render(f"{total_time // 1000} seconds left", True, FONT_COLOR)
    screen.blit(time_text, (SCREEN_WIDTH/2, 50))
    target.update()
    targets_group.draw(screen)

    crosshair.update()
    crosshair_group.draw(screen)

    pygame.display.flip()           #v important updates the screen
    #v imp to fix the timer issue
    start_time = current_time