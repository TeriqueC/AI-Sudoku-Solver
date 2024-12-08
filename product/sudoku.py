import pygame

class Sudoku():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        self.screen.fill((255, 255, 255))
        self.board = []
        self.font = pygame.font.Font(None, 50)
        # setting up the window  in which the puzzle will be displayed on
        
    def draw_grid(self, grid):
        square_size = 340/grid.__len__()
        # keeps the size of the sudoku grid 340 by ensuring the squares all fit within that size
        self.font = pygame.font.Font(None, round(square_size))
        col_offset = 130
        #row_offset = 0 will be needed later when tidying up the interface!
        # offsets needed to keep the squares inside the grid borders
        divisor = grid.__len__() ** 0.5
        if(divisor%1!=0):
            row_divisor = round(divisor)
            column_divisor = round(divisor)+1
        else: row_divisor, column_divisor = divisor, divisor
        # logic needed to divide the grid into sub-grids based on the size of the sudoku puzzle
        for row in range(grid.__len__()):
            self.board.append([])
            # adds a array inside another array, representing rows on the board
            if(row%row_divisor==0 and row != 0):
                pygame.draw.line(self.screen, (0, 0, 0), (col_offset, row*square_size), 
                (col_offset+(grid.__len__()*square_size), row*square_size), 8)
                # where the board is divided based on divisor, thicker lines are used to show the divisions that 
                # make up the sub-grids
            for col in range(grid.__len__()):
                square = pygame.Rect(col_offset+(col*square_size), row*square_size, square_size, square_size)
                value = self.font.render("" if grid[row][col] == 0 else str(grid[row][col]), True, (0, 0, 0))
                val_rect = value.get_rect()
                val_rect.center = square.center
                self.screen.blit(value, val_rect)
                self.board[row].append(square)
                pygame.draw.rect(self.screen, (0, 0, 0), square, 1)
                # the squares are created within the boundaries of the grid, and smaller rectangles with the preset
                # puzzle values are displayed within the squares where their coordinates are found from the input array
                if(col%column_divisor==0 and col != 0):
                    pygame.draw.line(self.screen, (0, 0, 0), (col_offset+(col*square_size), row*square_size), 
                    (col_offset+(col*square_size), grid.__len__()*square_size), 8)
                # where the board is divided based on divisor, thicker lines are used to show the divisions that 
                # make up the sub-grids
        pygame.display.flip()
        # updates window

    def update(self, int, x, y):
        self.screen.subsurface(self.board[x][y]).subsurface(5, 5,
        self.board[x][y].width-10,self.board[x][y].height-10).fill((255, 255, 255))
        # resets the value in the square on the board by replacing it with a blank square
        if(int != 0):
            value = self.font.render(str(int), True, (0, 0, 0))
            val_rect = value.get_rect(center=self.board[x][y].center)
            self.screen.blit(value, val_rect)
            # if the value to be put on the square is not a 0, then a new rectangle (square) with the parameter value
            # is used replace the blank square     
        pygame.display.flip()
        # updates window

    def print_grid(self, grid):
        if(grid == None):
            print("No found solution!")
            return
        divisor = grid.__len__() ** 0.5
        if(divisor%1!=0):
            row_divisor = round(divisor)
            column_divisor = round(divisor)+1
        else: row_divisor, column_divisor = divisor, divisor
        # logic for dividing sudoku grid into regions depending on sudoku length
        for i in range(grid.__len__()):
            if i % row_divisor == 0:
                print(" - "*grid.__len__())
                # uses dividing value to place row borders
            row=""
            for j in range(grid[i].__len__()):
                if(j % column_divisor ==0):
                    row+= " |"
                    # uses dividing value to place column borders
                row+=" "+str(grid[i][j]) if grid[i][j]!=0 else " *"
                # adds number or * to be printed for final sudoku output
            print(row+" |")
        print(" - "*grid.__len__())
        # printing the numbers of grid list or an * where there is a 0
        # and the borders to display the sudoku in the console to the user