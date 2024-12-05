import pygame

class Sudoku():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        self.screen.fill((255, 255, 255))
        self.board = []
        self.font = pygame.font.Font(None, 50)
        
    def draw_grid(self, grid):
        square_size = 340/grid.__len__()
        self.font = pygame.font.Font(None, round(square_size))
        col_offset = 130
        #row_offset = 0 will be needed later when tidying up the interface!
        divisor = grid.__len__() ** 0.5
        if(divisor%1!=0):
            row_divisor = round(divisor)
            column_divisor = round(divisor)+1
        else: row_divisor, column_divisor = divisor, divisor
        for row in range(grid.__len__()):
            self.board.append([])
            if(row%row_divisor==0 and row != 0):
                pygame.draw.line(self.screen, (0, 0, 0), (col_offset, row*square_size), 
                (col_offset+(grid.__len__()*square_size), row*square_size), 8)
            for col in range(grid.__len__()):
                square = pygame.Rect(col_offset+(col*square_size), row*square_size, square_size, square_size)
                value = self.font.render("" if grid[row][col] == 0 else str(grid[row][col]), True, (0, 0, 0))
                val_rect = value.get_rect()
                val_rect.center = square.center
                self.screen.blit(value, val_rect)
                self.board[row].append(square)
                pygame.draw.rect(self.screen, (0, 0, 0), square, 1)
                if(col%column_divisor==0 and col != 0):
                    pygame.draw.line(self.screen, (0, 0, 0), (col_offset+(col*square_size), row*square_size), 
                    (col_offset+(col*square_size), grid.__len__()*square_size), 8)
        pygame.display.flip()

    def update(self, int, x, y):
        self.screen.subsurface(self.board[x][y]).subsurface(5, 5,
        self.board[x][y].width-10,self.board[x][y].height-10).fill((255, 255, 255))
        if(int != 0):
            value = self.font.render(str(int), True, (0, 0, 0))
            val_rect = value.get_rect(center=self.board[x][y].center)
            self.screen.blit(value, val_rect)
        pygame.display.flip()

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