import pygame

class Cell(pygame.sprite.Sprite):
    """sprite to hold rect and text objects"""

    #constructor
    def __init__(self, x, y, rows, cols, surface ):
        
        #calls the parent constructor
        pygame.sprite.Sprite.__init__(self)
        
        #set the coords of the cell
        self.x = x
        self.y = y

        #set the text of the cell
        self.text = " "        
        
        #set the rect to the proper coords and dimensions
        w = surface.get_width()
        h = surface.get_height()
        self.cols = cols
        self.rows = rows
        
        #print(x)
        #print(y)
        #print(rows)
        #print(cols)
        #print(surface)
        
        left = int((w / cols) * x)
        top = int((h / rows) * y)
        width = int( w / cols)
        height = int( h / rows)
        
        #print("left: ",left)
        #print("top: ",top)
        #print("width: ", width)
        #print("height: ", height)
        
        self.rectangle = pygame.Rect( left, top, width,height)
        #self.rectangle.fill(0,0,0)
        
    def draw(self, surface):
        pygame.draw.rect(surface, (0,0,0), self.rectangle)
        #surface
    
    def print(self):
        print("x: ", self.x, "y: ", self.y)

class Board:
    """a class that handles the grid"""
    def __init__(self, r, c, surface):
        self.draw_group = []
        self.cols = c
        self.rows = r
        self.grid = [[None] * self.cols] * self.rows

        for i in range(len(self.grid)):
            #print("i: ",i)
            for j in range(len(self.grid[i])):
                #print("j: ",j)
                temp = Cell( i, j, r, c, surface)
                self.grid[i][j] = c
                self.draw_group.append(c)
    def getCell(self,r,c):
        r = int(r)
        c = int(c)
        if(r > 0 and r < self.rows and c > 0 and c < self.cols):
            return self.grid[r][c]
        return False
    def setCell(self,r,c,v):
        r = int(r)
        c = int(c)
        v = str(v)
        if(r > 0 and r < self.rows and c > 0 and c < self.cols):
            self.grid[r][c] = v
            return True
        return False


