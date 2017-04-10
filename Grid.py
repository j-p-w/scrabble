from Globals import *
from Tile import Tile

class Grid:

    def __init__(self, size):

        self.grid = [[Tile(i,j,"none") for i in range(0,size) ] for j in range(0,size)]
        self.size = size
        self.config()

    def config(self, style="default"):

        if style == "default":

            grid = [
                ["3w"," "," ","2l"," "," "," ","3w"," "," "," ","2l"," "," ","3w"],
                [" ","2w"," "," "," ","3l"," "," "," ","3l"," "," "," ","2w"," "],
                [" "," ","2w"," "," "," ","2l"," ","2l"," "," "," ","2w"," "," "],
                ["2l"," "," ","2w"," "," "," ","2l"," "," "," ","2w"," "," ","2l"],
                [" "," "," "," ","2w"," "," "," "," "," ","2w"," "," "," "," "],
                [" ","3l"," "," "," ","3l"," "," "," ","3l"," "," "," ","3l"," "],
                [" "," ","2l"," "," "," ","2l"," ","2l"," "," "," ","2l"," "," "],
                ["3w"," "," ","2l"," "," "," ","2w"," "," "," ","2l"," "," ","3w"],
                [" "," ","2l"," "," "," ","2l"," ","2l"," "," "," ","2l"," "," "],
                [" ","3l"," "," "," ","3l"," "," "," ","3l"," "," "," ","3l"," "],
                [" "," "," "," ","2w"," "," "," "," "," ","2w"," "," "," "," "],
                ["2l"," "," ","2w"," "," "," ","2l"," "," "," ","2w"," "," ","2l"],
                [" "," ","2w"," "," "," ","2l"," ","2l"," "," "," ","2w"," "," "],
                [" ","2w"," "," "," ","3l"," "," "," ","3l"," "," "," ","2w"," "],
                ["3w"," "," ","2l"," "," "," ","3w"," "," "," ","2l"," "," ","3w"]
            ]

            for x in range(0,15):
                for y in range(0,15):
                    self.grid[x][y].tileType = grid[x][y]


    def draw(self):

        global screen, font, small_font

        for row in self.grid:
            for tile in row:
                tile.draw()

    def recall(self):

        letters = []
        for row in self.grid:
            for tile in row:
                if tile.set == False and tile.letter != " ":
                    letters.append(tile.letter)
                    tile.letter = " "

        return letters

    def get_unplaced_tiles(self):

        letters = []
        for row in self.grid:
            for tile in row:
                if tile.set == False and tile.letter != " ":
                    letters.append(tile)

        return letters


    def insert_word(self, dir, word, row, col):

        if dir == "H":

            if col + len(word) > self.size:
                return False

            i = 0
            for c in word:
                self.grid[row][col+i].letter = word[i]
                self.grid[row][col+i].set = True
                i += 1

        elif dir == "V":

            if row + len(word) > self.size:
                return False

            i = 0
            for c in word:
                self.grid[row+i][col].letter = word[i]
                self.grid[row+i][col].set = True
                i += 1

    def get_word_indices(self):

        word_indices = []
        letter_indices = []

        for x in range(0,self.size):
            for y in range(0,self.size):
                if self.grid[x][y].isalpha() and [x,y] not in word_indices:
                    letter_indices.append([x,y])

        for tile in letter_indices:
            x = tile[0]
            y = tile[1]

            i = 0
            while self.grid[x-i][y].isalpha():
                i += 1
                if (x-i) < 0: break
            startX = x-i+1

            j = 0
            while self.grid[x][y-j].isalpha():
                j += 1
                if (y-j) < 0: break
            startY = y-j+1
            if [startX, y] not in word_indices: word_indices.append([startX, y])
            if [x, startY] not in word_indices: word_indices.append([x, startY])

        return word_indices

    def get_starting_points(self, word_indices):

        starting_points = []

        for tile in word_indices:
            x = tile[0]
            y = tile[1]
            lowX = x - 7
            lowY = y - 7
            if lowX < 0: lowX = 0
            if lowY < 0: lowY = 0

            for i in range(lowX, x):
                if i != 0:
                    if self.grid[i][y] == " " and not self.grid[i-1][y].isalpha() and [i,y] not in starting_points:
                        starting_points.append([i,y])
                else:
                    if self.grid[i][y] == " " and [i,y] not in starting_points:
                        starting_points.append([i,y])

            for j in range(lowY, y):
                if j != 0:
                    if self.grid[x][j] == " " and not self.grid[x][j-1].isalpha() and [x,j] not in starting_points:
                        starting_points.append([x,j])
                else:
                    if self.grid[x][j] == " " and [x,j] not in starting_points:
                        starting_points.append([x,j])

            if [x,y] not in starting_points:
                starting_points.append([x,y])

        return starting_points

    def verify(self, grid):

        for i in range(0,self.size):

            in_word = False
            word_list = []
            word = ""
            for j in range(0,self.size):
                if grid[i][j] == " ":
                    if in_word == True:
                        word_list.append(word)
                        print(word)
                        in_word = False
                        word = ""
                    else: pass
                else:
                    in_word = True
                    word += grid[i][j]
        return word_list
