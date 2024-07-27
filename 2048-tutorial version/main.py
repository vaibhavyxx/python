import pygame
import random
import math

pygame.init()

total_score = 0
f = open("2048-tutorial version/scores.txt", "w")

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
GRID_WIDTH, GRID_HEIGHT = 800,800
ROWS = 4
COLS = 4

RECT_HEIGHT = GRID_HEIGHT // ROWS
RECT_WIDTH = GRID_WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)
FONT = pygame.font.SysFont("Comic Sans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2048")

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
        (236, 202, 80),      #512
        (245, 161, 113),     #1024
        (245, 105, 98),      #2048
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

    def set_pos(self, ceil=False):
        #rounds up number to a higher integer value-moves right
        if ceil:
            self.row = math.ceil(self.y / RECT_HEIGHT)
            self.col = math.ceil(self.x / RECT_WIDTH)
        
        #rounds up number to a lower integer value- moves left
        else:
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x / RECT_WIDTH)

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]

#draws game title, button and a music?
def draw_menu(window):
    text = FONT.render("2048", True, (255, 255, 255))
    window.blit(
        text, 
        ((GRID_WIDTH/2 - text.get_width()/2), 
        (GRID_HEIGHT/3 - text.get_height()/2),),
        )

    play_text = FONT.render("Press ENTER to play", True, FONT_COLOR)
    window.blit(
            play_text,
            (100,
             (GRID_HEIGHT -250))
        )
    
def draw_end(window):
    global phrase
    if state == "lost":
        phrase = "You Lost!"
    elif state == "win":
        phrase = "You Won!"

    text = FONT.render(phrase, True, (255, 255, 255))
    window.blit(
        text, 
        ((GRID_WIDTH/2 - text.get_width()/2), 
        (GRID_HEIGHT/3 - text.get_height()/2),),
        )
    score_text = FONT.render(f"Score: {total_score}", True, FONT_COLOR)
    window.blit(
        score_text,
        (GRID_WIDTH/2 - text.get_width()/2,
         GRID_HEIGHT-350)
    )
    play_text = FONT.render("Press ENTER to replay", True, FONT_COLOR)
    window.blit(
            play_text,
            ((100),
             (GRID_HEIGHT * 0.67))
        )
    
def draw_grid(window):
    for row in range(ROWS):
        pygame.draw.line(window, OUTLINE_COLOR, (0, row * RECT_HEIGHT), (GRID_WIDTH, row * RECT_HEIGHT), OUTLINE_THICKNESS)
    for col in range(COLS):
        pygame.draw.line(window, OUTLINE_COLOR, (col * RECT_WIDTH, 0), (col * RECT_WIDTH, GRID_HEIGHT), OUTLINE_THICKNESS)

    pygame.draw.rect(window, OUTLINE_COLOR, (0, 0, GRID_WIDTH, GRID_HEIGHT), OUTLINE_THICKNESS)

#main draw function
def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)

    if game_scene == "menu":
       draw_menu(window)

    elif game_scene == "game":
        #draws all the tile objects
        for tile in tiles.values():
            tile.draw(window)
        draw_grid(window)

    elif game_scene == "end":
        draw_end(window)

    pygame.display.update()

#uses dictionary to find if the random coordinate is empty or not
def get_random_position(tiles):
    row = None
    col = None

    while True:
        row = random.randrange(0, ROWS)
        col = random.randrange(0, COLS)

        if f"{row}{col}" not in tiles:
            break
    return row, col

#for tile movement
def move_tiles(window, tiles, clock, direction):
    global total_score
    updated = True
    blocks = set()

    if direction == 'left':
        sort_func = lambda x : x.col
        reverse = False
        delta = (-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col -1}")
        #moves the tile it is over the other tile to merge
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
        move_check = lambda tile, next_tile: tile.x > next_tile.x + RECT_WIDTH + MOVE_VEL
        ceil = True

    elif direction == "right":
        sort_func = lambda x: x.col
        reverse = True
        delta = (MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == COLS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row}{tile.col + 1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.x + RECT_WIDTH + MOVE_VEL < next_tile.x
        )
        ceil = False
        
    elif direction == "up":
        sort_func = lambda x: x.row
        reverse = False
        delta = (0, -MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row - 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y > next_tile.y + RECT_HEIGHT + MOVE_VEL
        )
        ceil = True
        
    elif direction == "down":
        sort_func = lambda x: x.row
        reverse = True
        delta = (0, MOVE_VEL)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1}{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
        move_check = (
            lambda tile, next_tile: tile.y + RECT_HEIGHT + MOVE_VEL < next_tile.y
        )
        ceil = False

    #continue will force the loop to start the next iteration
    #pass will make it just skip it and run the rest of the loop
    #update this to true if this operation has happened
    #enumerate acts similar to for loops, i index where you access values
    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key=sort_func, reverse=reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue

            #you will move the tile till it is overlapping on its next tile
            #which has the same value. then, you would update the value
            next_tile = get_next_tile(tile)
            if not next_tile:
                tile.move(delta)

            #to format it like this, use ()
            elif (tile.value== next_tile.value 
                  and tile not in blocks 
                  and next_tile not in blocks):
                
                if merge_check(tile, next_tile):
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    total_score+= next_tile.value #saves value of the newly merged tile
                    sorted_tiles.pop(i)
                    #to avoid this tile to be merged again
                    blocks.add(next_tile)

            elif move_check(tile, next_tile):
                tile.move(delta)

            else:
                continue

            #this triggers the update loop, the only way to exit this
            #loop is when else condition is satisfied 
            tile.set_pos(ceil)
            updated = True

        update_tiles(window, tiles, sorted_tiles)
    return end_move(tiles)

def saveScore():
    try:
        with open("2048-tutorial version/scores.txt", "a") as f:
            f.write(f"{total_score}\n")
    except IOError as e:
        print(f"Error printing this to file: {e}")

#finds last move and saves score
def end_move(tiles):

    if any(tile.value == 2048 for tile in tiles.values()):
        return "win"
    
    if len(tiles) ==16:
        return "lost"
    
    row,col = get_random_position(tiles)
    tiles[f"{row}{col}"] = Tile(random.choice([2,4]), row, col)
    return "continue"

#updates tile position and draws them
def update_tiles(window, tiles, sorted_tiles):
    tiles.clear()
    for tile in sorted_tiles:
        tiles[f"{tile.row}{tile.col}"] = tile

    draw(window, tiles)

#chooses two random position and makes a tile there if it is empty
def generate_tiles():
    tiles = {}
    for t in range(2):
        row, col = get_random_position(tiles)
        tiles[f"{row}{col}"] = Tile(2, row, col)
    return tiles

#game loop
def main(window):
    clock = pygame.time.Clock()
    run = True
    global state
    state = ""
    global game_scene
    game_scene = "menu"

    tiles = generate_tiles()

    #to ensure that the game's speed is regardless of processor's speed
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    state = move_tiles(window, tiles, clock, "left")

                elif event.key == pygame.K_RIGHT:
                    state = move_tiles(window, tiles, clock, "right")

                elif event.key == pygame.K_UP:
                    state = move_tiles(window, tiles, clock, "up")

                elif event.key == pygame.K_DOWN:
                    state = move_tiles(window, tiles, clock, "down")

                #bug: issue w saving scores and tile movement
                #fms for scene transitions
                if game_scene == "menu" and event.key == pygame.K_RETURN:
                    game_scene = "game"

                if state == "lost" or state == "win":
                    game_scene = "end"
                
                if game_scene == "game" and len(tiles) == 0:
                    tiles = generate_tiles()
                    
                if game_scene == "end" and event.key == pygame.K_RETURN:
                    saveScore()
                    game_scene = "menu"
                    tiles.clear()
                    state = ""

        draw(window, tiles)
    pygame.quit()

if __name__ == "__main__":
    main(WINDOW)
