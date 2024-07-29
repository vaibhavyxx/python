#to learn how sprites work have to be drawn in a group only
import pygame, sys
pygame.display.set_caption("Sprites")
class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width, height, x_pos, y_pos, color):
        super().__init__()
        self.image = pygame.Surface([width, height]) #empty surface
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT= 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

crosshair = Crosshair(100,100, 200,200, (255,255,255))
c2 = Crosshair(50, 100, 300, 400, (200, 150,0))
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)
crosshair_group.add(c2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    crosshair_group.draw(screen)
    pygame.display.flip()           #v important updates the screen
    clock.tick(60)
