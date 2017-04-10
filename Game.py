import pygame
import math
import random

from Globals import *
from Grid import Grid
from Player import Player
from Dictionary import is_word

class Game:

    def __init__(self):

        self.Running = True
        self.gamegrid = Grid(15)
        self.p1 = Player(1)
        self.p2 = Player(2)

        for i in range(0,7):
            choice = random.randrange(0,len(bag))
            self.p1.tiles[i].letter = bag[choice]
            del bag[choice]
        for i in range(0,7):
            choice = random.randrange(0,len(bag))
            self.p2.tiles[i].letter = bag[choice]
            del bag[choice]

        self.holding_tile = False
        self.holding_player_tile = False
        self.selectX = 0
        self.selectY = 0
        self.mousePressed = False
        self.turn = 1

    def Render(self):

        global button_font

        pygame.display.flip()
        screen.fill([0,0,0])

        # Draw the recall button
        pygame.draw.rect(screen, [80,20,170], (1 * TILESIZE, 16 * TILESIZE, TILESIZE*2 - 2, TILESIZE), 0)
        pygame.draw.rect(screen, [130,70,220], (1 * TILESIZE + 1, 16 * TILESIZE + 1, TILESIZE*2 - 2, TILESIZE-2), 2)
        screen.blit(button_font.render("Recall", 1, [180,120,255]), (1 * TILESIZE + 4, 16 * TILESIZE + 7))

        # Draw the place button
        pygame.draw.rect(screen, [200,200,30], (12 * TILESIZE, 16 * TILESIZE, TILESIZE*2 - 2, TILESIZE), 0)
        pygame.draw.rect(screen, [255,255,80], (12 * TILESIZE + 1, 16 * TILESIZE + 1, TILESIZE*2 - 2, TILESIZE-2), 2)
        screen.blit(button_font.render("Place", 1, [255,255,130]), (12 * TILESIZE + 6, 16 * TILESIZE + 7))

        # Draw the currently placed tiles
        self.gamegrid.draw()
        if self.turn == 1:
            self.p1.draw()
        elif self.turn == 2:
            self.p2.draw()

        # Draw the currently held tile
        if self.holding_tile:
            mX = pygame.mouse.get_pos()[0]
            mY = pygame.mouse.get_pos()[1]

            pygame.draw.rect(screen, [150,100,70], (mX-15, mY-15, TILESIZE, TILESIZE), 0)
            pygame.draw.rect(screen, [0,0,0], (mX-15, mY-15, TILESIZE, TILESIZE), 1)

            if self.selectX < 15 and self.selectY < 15:
                screen.blit(font.render(self.gamegrid.grid[self.selectY][self.selectX].letter, 1, (200, 200, 200)), (mX - 15 + 4, mY -15 + 1))
                screen.blit(small_font.render(str(letter_scores[self.gamegrid.grid[self.selectY][self.selectX].letter]), 1, (200, 200, 200)), (mX - 15 + 22,  mY - 15 + 18))

        if self.holding_player_tile:
            mX = pygame.mouse.get_pos()[0]
            mY = pygame.mouse.get_pos()[1]

            pygame.draw.rect(screen, [150,100,70], (mX - 15, mY - 15, TILESIZE, TILESIZE), 0)
            pygame.draw.rect(screen, [0,0,0], (mX - 15, mY - 15, TILESIZE, TILESIZE), 1)

            screen.blit(font.render(self.p1.tiles[self.selectX-4].letter, 1, (200, 200, 200)), (mX - 15 + 4, mY -15 + 1))
            screen.blit(small_font.render(str(letter_scores[self.p1.tiles[self.selectX-4].letter]), 1, (200, 200, 200)), (mX - 15 + 22,  mY - 15 + 18))

    def Update(self):

        ev = pygame.event.get()
        mouseVal = pygame.mouse.get_pressed()
        mouseCoords = pygame.mouse.get_pos()

        mouseX = mouseCoords[0]
        mouseY = mouseCoords[1]

        if not self.holding_tile:
            self.selectX = math.ceil(mouseX/TILESIZE) - 1
            self.selectY = math.ceil(mouseY/TILESIZE) - 1

        keysPressed = pygame.key.get_pressed()

        # If first time left clicking
        if mouseVal[0] and self.mousePressed == False:

            self.mousePressed = True

            # If within the game grid
            if self.selectX >= 0 and self.selectY >= 0 and self.selectX < 15 and self.selectY < 15:

                # If an actual tile is selected, hold that tile
                if self.gamegrid.grid[self.selectY][self.selectX].letter != " " and self.gamegrid.grid[self.selectY][self.selectX].set == False:
                    self.holding_tile = True
                    self.gamegrid.grid[self.selectY][self.selectX].placed = False

            # If within the player grid
            elif self.selectX > 3 and self.selectX < 11 and self.selectY == 16:
                if self.p1.tiles[self.selectX-4].letter != " ":
                    self.holding_tile = True
                    self.holding_player_tile = True
                    self.p1.tiles[self.selectX-4].placed = False

            # If on the recall button
            elif self.selectX > 0 and self.selectX < 3 and self.selectY == 16:
                letters = self.gamegrid.recall()
                for tile in self.p1.tiles:
                    if tile.letter == " ":
                        tile.letter = letters[-1]
                        del letters[-1]

            # If on the place button
            elif self.selectX > 11 and self.selectX < 14 and self.selectY == 16:

                can_continue = True

                # Get the list of unplaced tiles
                tiles = self.gamegrid.get_unplaced_tiles()

                # Check if horizontal or vertical (or both)
                if len(tiles) > 0:
                    x = tiles[0].x
                    y = tiles[0].y

                    # Determine if valid tile placement
                    horizontal = True
                    vertical = True
                    for tile in tiles:
                        if tile.x != x:
                            vertical = False
                        if tile.y != y:
                            horizontal = False
                    if not horizontal and not vertical: can_continue = False
                else: can_continue = False

                # Verify placed word is real, then verify all words connected to it
                if can_continue:
                    # First, find the upperleft-most tile of all unplaced tiles
                    lowX = 14
                    lowY = 14
                    for tile in tiles:
                        if horizontal:
                            if tile.x < lowX: lowX = tile.x
                        if vertical:
                            if tile.y < lowY: lowY = tile.y
                    if horizontal: lowY = tiles[0].y
                    if vertical: lowX = tiles[0].x

                    # Then, move left or up to check for placed tiles being first
                    if horizontal:
                        x = lowX - 1
                        letter = "*"
                        in_once = False
                        while x > 0 and letter != " ":
                            letter = self.gamegrid.grid[lowY][x].letter
                            x -= 1
                            in_once = True
                        if in_once:
                            lowX = x + 2
                    if vertical:
                        y = lowY - 1
                        letter = "*"
                        in_once = False
                        while y > 0 and letter != " ":
                            letter = self.gamegrid.grid[y][lowY].letter
                            y -= 1
                            in_once = True
                        if in_once:
                            lowY = y + 2

                    # Upperleft-most point at first letter is at lowX, lowY

                # Calculate points, solidify the tiles and give back more
                if can_continue:
                    pass

        # If let go of left click
        if mouseVal[0] == 0:

            self.mousePressed = False
            if self.holding_tile:

                currentX = math.ceil(mouseX/TILESIZE) - 1
                currentY = math.ceil(mouseY/TILESIZE) - 1

                # If within the game grid
                if currentX >= 0 and currentY >= 0 and currentX < 15 and currentY < 15:

                    # Get the letter, depending on gamegrid or from player tiles
                    if self.selectY < 15:

                        letter = self.gamegrid.grid[self.selectY][self.selectX].letter

                        # If the space is free, place the tile and update the empty one
                        if self.gamegrid.grid[currentY][currentX].letter == " ":
                            self.gamegrid.grid[currentY][currentX].letter = letter
                            self.gamegrid.grid[currentY][currentX].placed = True
                            self.gamegrid.grid[self.selectY][self.selectX].letter = " "
                    else:

                        letter = self.p1.tiles[self.selectX-4].letter

                        # If the space is free, place the tile and update the empty one
                        if self.gamegrid.grid[currentY][currentX].letter == " ":
                            self.gamegrid.grid[currentY][currentX].letter = letter
                            self.gamegrid.grid[currentY][currentX].placed = True
                            self.p1.tiles[self.selectX-4].letter = " "


                # Else if in the player tile area
                elif currentX > 3 and currentX < 11 and currentY == 16:

                    # Get the letter, depending on gamegrid or from player tiles
                    if self.selectY < 15:
                        letter = self.gamegrid.grid[self.selectY][self.selectX].letter
                    else:
                        letter = self.p1.tiles[self.selectX-4].letter

                    # If the space is free, place the tile and update the empty one
                    if self.p1.tiles[currentX-4].letter == " ":
                        self.p1.tiles[currentX-4].letter = letter
                        self.p1.tiles[currentX-4].placed = True

                        if self.selectY < 15:
                            self.gamegrid.grid[self.selectY][self.selectX].letter = " "
                        else:
                            self.p1.tiles[self.selectX-4].letter = " "

                self.holding_tile = False

                # If within the game grid, Update the selected space
                if self.selectX < 15 and self.selectY < 15:
                    self.gamegrid.grid[self.selectY][self.selectX].placed = True
                else:
                    self.p1.tiles[self.selectX-4].placed = True
                    self.holding_player_tile = False

        if keysPressed[pygame.K_LEFT]:
            pass


        for event in ev:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.gamegrid.insert_word("H","WORDS",7,5)
            if event.type == pygame.QUIT:
                self.Running = False
