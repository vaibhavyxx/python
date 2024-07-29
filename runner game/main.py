import pygame
from pygame.sprite import _Group

pygame.init()

#spritesheets for animations- don't use alpha
girl_walk_spritesheet = pygame.image.load("runner game/spritesheet/girl-walk.png")

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Endless Scroller Game")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, frame_width, frame_height, scale):
        self.x =x
        self.y = y
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.scale = scale

    #for splitting spritesheet into list of pngs
    def load_frame(self, sprite_sheet):
        frames_list= []
        sheet_width, sheet_height = sprite_sheet.get_size()

        for x in range(0, sheet_width, frame_width):
            frame = sprite_sheet.subsurface(x, 0, frame_width, frame_height)
            frames_list.append(frame)

        return frames_list
    
    #draws the animation
    def animate_sprite(self, last_update, animation_cooldown, frame, frames_list, window):
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame +=1
            last_update = current_time
            if frame >= len(frames):
                frame =0
        window.blit(frames_list[frame], (self.x,self.y))

    

#for animation
def load_frame(sprite_sheet, frame_width, frame_height):
    frames= []
    sheet_width, sheet_height = sprite_sheet.get_size()

    for x in range(0, sheet_width, frame_width):
        frame = sprite_sheet.subsurface(x, 0, frame_width, frame_height)
        frames.append(frame)

    return frames
    
frame_width, frame_height = 521, 576
frames = load_frame(girl_walk_spritesheet, frame_width, frame_height)
last_update = pygame.time.get_ticks()
animation_cooldown = 100 #milliseconds
frame = 0   #to start at the first frame

#game loop
run = True
while run:

    #update background
    window.fill((255, 255, 255))

    #to load animation- for every 0.1s update the frame
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame +=1
        last_update = current_time
        if frame >= len(frames):
            frame =0
    window.blit(frames[frame], (0,0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()