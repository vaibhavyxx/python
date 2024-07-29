import pygame
import sys
pygame.init()

#spritesheets for animations- don't use alpha
girl_walk_spritesheet = pygame.image.load("runner game/spritesheet/girl-walk.png")

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Scroller Game")

#for splitting spritesheet into list of pngs
def load_frame(sprite_sheet):
    frames_list= []
    sheet_width, sheet_height = sprite_sheet.get_size()

    for x in range(0, sheet_width, frame_width):
        frame = sprite_sheet.subsurface(x, 0, frame_width, frame_height)
        frames_list.append(frame)
    return frames_list

frame_width, frame_height = 521, 576
girl_walk_list = load_frame(girl_walk_spritesheet)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, frames_list):
        super().__init__()
        self.current_img =0
        self.frames_list = frames_list
        self.image = self.frames_list[self.current_img]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    
    #draws the animation
    def animate_sprite(self, last_update, animation_cooldown, current_img, frames_list, window):
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            self.current_img +=1
            last_update = current_time
            if current_img >= len(girl_walk_list):
                self.current_img =0
        window.blit(frames_list[current_img], (0 ,0))
        return last_update

p1 = Player(0,0, girl_walk_list)
last_update = pygame.time.get_ticks()
animation_cooldown = 100 #milliseconds
frame = 0   #to start at the first frame

player_group = pygame.sprite.Group()
player_group.add(p1)

#game loop
run = True
while run:

    #update background
    window.fill((255, 255, 255))

    #to load animation- for every 0.1s update the frame
    last_update= p1.animate_sprite(last_update, animation_cooldown, frame, girl_walk_list, window)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()