import pygame
import math
from Globals import *

class Tile:

    def __init__(self, x, y, tileType):

        self.x = x
        self.y = y
        self.tileType = tileType
        self.letter = " "
        self.set = False
        self.placed = True

    def draw(self):

        global TILESIZE
        global screen, font, small_font, multiplier_font, shadow_font

        mX = pygame.mouse.get_pos()[0]
        mY = pygame.mouse.get_pos()[1]


        if self.tileType == " ":
            color = [255, 255, 255]
        if self.tileType == "2w":
            color = [255, 0, 0]
        if self.tileType == "3w":
            color = [255, 165, 0]
        if self.tileType == "2l":
            color = [0, 0, 255]
        if self.tileType == "3l":
            color = [0, 255, 0]

        color[0] -= 50
        color[1] -= 50
        color[2] -= 50
        if color[0] < 0: color[0] = 0
        if color[1] < 0: color[1] = 0
        if color[2] < 0: color[2] = 0

        # Draw borders
        pygame.draw.rect(screen, [255,255,255], (self.x * TILESIZE, self.y * TILESIZE, TILESIZE+1, TILESIZE+1), 1)

        # Draw blank tiles
        if self.letter == " ":

            pygame.draw.rect(screen, color, (self.x * TILESIZE, self.y * TILESIZE, TILESIZE, TILESIZE), 0)
            pygame.draw.rect(screen, [color[0]+50,color[1]+50,color[2]+50], (self.x * TILESIZE + 1, self.y * TILESIZE + 1, TILESIZE-2, TILESIZE-2), 2)

            if self.tileType == "2w": screen.blit(multiplier_font.render("DW", 1, [255,100,100]), (self.x * TILESIZE + 4, self.y * TILESIZE + 8))
            if self.tileType == "3w": screen.blit(multiplier_font.render("TW", 1, [255,165,100]), (self.x * TILESIZE + 3, self.y * TILESIZE + 8))
            if self.tileType == "2l": screen.blit(multiplier_font.render("DL", 1, [100,100,255]), (self.x * TILESIZE + 6, self.y * TILESIZE + 8))
            if self.tileType == "3l": screen.blit(multiplier_font.render("TL", 1, [100,255,100]), (self.x * TILESIZE + 4, self.y * TILESIZE + 8))

        # Draw placed tiles
        elif self.letter != " " and self.placed == True:

            pygame.draw.rect(screen, [150,100,70], (self.x * TILESIZE, self.y * TILESIZE, TILESIZE, TILESIZE), 0)
            pygame.draw.rect(screen, [0,0,0], (self.x * TILESIZE, self.y * TILESIZE, TILESIZE, TILESIZE), 1)

            if self.set == True: color = (200, 160, 130)
            else: color = (200, 200, 200)

            #screen.blit(shadow_font.render(self.letter, 1, [100,100,100]), (self.x * TILESIZE + 3, self.y * TILESIZE + 0))
            screen.blit(font.render(self.letter, 1, color), (self.x * TILESIZE + 4, self.y * TILESIZE + 1))
            screen.blit(small_font.render(str(letter_scores[self.letter]), 1, color), (self.x * TILESIZE + 22, self.y * TILESIZE + 18))

        elif self.placed == False:
            pygame.draw.rect(screen, color, (self.x * TILESIZE, self.y * TILESIZE, TILESIZE, TILESIZE), 0)
            pygame.draw.rect(screen, [color[0]+50,color[1]+50,color[2]+50], (self.x * TILESIZE + 1, self.y * TILESIZE + 1, TILESIZE-2, TILESIZE-2), 2)

            if self.tileType == "2w": screen.blit(multiplier_font.render("DW", 1, [255,100,100]), (self.x * TILESIZE + 4, self.y * TILESIZE + 8))
            if self.tileType == "3w": screen.blit(multiplier_font.render("TW", 1, [255,165,100]), (self.x * TILESIZE + 3, self.y * TILESIZE + 8))
            if self.tileType == "2l": screen.blit(multiplier_font.render("DL", 1, [100,100,255]), (self.x * TILESIZE + 6, self.y * TILESIZE + 8))
            if self.tileType == "3l": screen.blit(multiplier_font.render("TL", 1, [100,255,100]), (self.x * TILESIZE + 4, self.y * TILESIZE + 8))











#
