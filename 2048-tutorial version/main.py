import pygame
import random
import math

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800,800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)
FONT = pygame.font.SysFont("Arial", 60, bold=True)
MOVE_VEL = 20

#window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

#tiles class
class Tile:
    #colors of the tiles for different numbers- advanced make this a dictionary
    # or use logs wil make it sm easier
    COLORS = [
        (237, 229, 218),    #2
        (238, 225, 201),    #4
        (243, 178, 122),    #8
        (246, 150, 101),    #16
        (247, 124, 95),     #32
        (247, 95,  59),     #64
        (237, 208, 115),    #128
        (237, 204, 99),     #256
        (236, 202, 80)      #512
    ]

#instead of this keyword, py uses self keyword, to access everything
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col
        #calculates x,y on your own
        self.x = col * RECT_WIDTH
        self.y = row* RECT_HEIGHT

    def get_color(self):
        color_index = int(math.log2(self.value)) -1
        color= self.COLORS[color_index]
        return color

    #draw the tile and then the text- blit draws a source surface to 
    #another surface
    def draw(self, window):
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, RECT_WIDTH, RECT_HEIGHT))
        text = FONT.render(f"{self.value}", True, FONT_COLOR)
        window.blit(
            text, 
            (self.x + (RECT_WIDTH/2 - text.get_width()/2), 
             self.y + (RECT_HEIGHT/2 - text.get_height()/2),),
            )


    def set_pos(self):
        pass

    def move(self, delta):
        pass

#draws grids
def draw_grid(window):
    for row in range(ROWS):
        pygame.draw.line(window, OUTLINE_COLOR, (0, row * RECT_HEIGHT), (WIDTH, row * RECT_HEIGHT), OUTLINE_THICKNESS)
    for col in range(COLS):
        pygame.draw.line(window, OUTLINE_COLOR, (col * RECT_WIDTH, 0), (col * RECT_WIDTH, HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

#main draw function
def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)

    #draws all the tile objects
    for tile in tiles.values():
        tile.draw(window)

    draw_grid(window)
    pygame.display.update()

#start at 36:26
#chooses two random position and makes a tile there if it is empty
def generate_tiles():
    pass

#game loop
def main(window):
    clock = pygame.time.Clock()
    run = True

    #use a dictionary for tiles to access value
    tiles = {
        "00" : Tile(4,0,0),
        "20" : Tile(128, 2, 0)
    }

    #to ensure that the game's speed is regardless of processor's speed
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window, tiles)

    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)


