from Globals import *
from Tile import Tile

class Player:

    def __init__(self, num):

        self.number = num
        self.tiles = [Tile(4,16," "), Tile(5,16," "), Tile(6,16," "), Tile(7,16," "), Tile(8,16," "), Tile(9,16," "), Tile(10,16," ")]

    def draw(self):

        for tile in self.tiles:

            # Draw borders
            pygame.draw.rect(screen, [255,255,255], (tile.x * TILESIZE - 1, tile.y * TILESIZE - 1, TILESIZE+1, TILESIZE+1), 2)

            color = [200, 200, 200]

            # Draw blank tiles
            if tile.letter == " ":

                pygame.draw.rect(screen, color, (tile.x * TILESIZE, tile.y * TILESIZE, TILESIZE, TILESIZE), 0)
                pygame.draw.rect(screen, [color[0]+50,color[1]+50,color[2]+50], (tile.x * TILESIZE + 1, tile.y * TILESIZE + 1, TILESIZE-2, TILESIZE-2), 2)

            # Draw placed tiles
            elif tile.letter != " " and tile.placed == True:

                pygame.draw.rect(screen, [150,100,70], (tile.x * TILESIZE, tile.y * TILESIZE, TILESIZE, TILESIZE), 0)
                pygame.draw.rect(screen, [0,0,0], (tile.x * TILESIZE, tile.y * TILESIZE, TILESIZE, TILESIZE), 1)

                if tile.set == True: color = (200, 160, 130)
                else: color = (200, 200, 200)

                #screen.blit(shadow_font.render(self.letter, 1, [100,100,100]), (self.x * TILESIZE + 3, self.y * TILESIZE + 0))
                screen.blit(font.render(tile.letter, 1, color), (tile.x * TILESIZE + 4, tile.y * TILESIZE + 1))
                screen.blit(small_font.render(str(letter_scores[tile.letter]), 1, color), (tile.x * TILESIZE + 22, tile.y * TILESIZE + 18))

            if tile.placed == False:
                pygame.draw.rect(screen, color, (tile.x * TILESIZE, tile.y * TILESIZE, TILESIZE, TILESIZE), 0)
                pygame.draw.rect(screen, [color[0]+50,color[1]+50,color[2]+50], (tile.x * TILESIZE + 1, tile.y * TILESIZE + 1, TILESIZE-2, TILESIZE-2), 2)






#
