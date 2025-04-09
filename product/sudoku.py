import pygame

class Sudoku():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700,650))
        pygame.display.set_caption("AI Sudoku Solver")
        self.screen.fill((255, 255, 255))
        self.board = []
        self.font = pygame.font.Font(None, 50)
        text_font = pygame.font.Font(None, 30)
        title = self.font.render("AI Sudoku Solver", True, (0,0,0))
        self.screen.blit(title, (200, 60))
        self.print_instructions(text_font)
        self.performance_display(text_font)
        # setting up the window  in which the puzzle will be displayed on
        
    def print_instructions(self, text_font):
        instruction_rect = pygame.Rect(400, 120, 286, 180)
        pygame.draw.rect(self.screen, (0,0,0), instruction_rect, 2)
        instruction_title = text_font.render("instructions:", True, (0,0,0))
        self.screen.blit(instruction_title, (instruction_rect.left+5, instruction_rect.top+5))
        instructions = ["Num keys 1-4: switch sudoku puzzles", 
        "Enter key: Backtracking solution", "Space key: CNN solution", 
        "Backspace: clear current solution", "higher num 1-3 renders harder sudoku", 
        "4th sudoku has no solution!!", "CNN (Convolutional Neural Network)"]
        top_offset = instruction_rect.top + 35
        for i in instructions:
            self.screen.blit(pygame.font.Font(None, 23).render(i, True, (0,0,0)), (instruction_rect.left+5, top_offset))
            top_offset += 20
        # set up the text prompts to guide the user on how to use the application to switch between puzzles, solvers and clearing solutions.
    
    def performance_display(self, text_font):
        performance_title = text_font.render("Performance scores:", True, (0,0,0))
        self.performance_rect = pygame.Rect(45, 480, 340, 100)
        pygame.draw.rect(self.screen, (0,0,0), self.performance_rect, 2)
        self.screen.blit(performance_title, (self.performance_rect.left+5,self.performance_rect.top+5))
        self.screen.blit(pygame.font.Font(None, 23).render("Time taken: ", True, (0,0,0)), 
        (self.performance_rect.left+5, self.performance_rect.top+35))
        self.screen.blit(pygame.font.Font(None, 23).render("Mistakes made: ", True, (0,0,0)), 
        (self.performance_rect.left+5, self.performance_rect.top+55))
        # sets up the performace display
        
    def draw_grid(self, grid):
        square_size = 340/grid.__len__()
        # keeps the size of the sudoku grid 340 by ensuring the squares all fit within that size
        self.font = pygame.font.Font(None, round(square_size))
        col_offset = 45
        row_offset = 120
        # offsets needed to keep the squares inside the grid borders
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(col_offset, row_offset, 340, 340))
        # clears gridspace for any redraws
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
                pygame.draw.line(self.screen, (0, 0, 0), (col_offset, row_offset+(row*square_size)), 
                (col_offset+(grid.__len__()*square_size), row_offset+(row*square_size)), 8)
                # where the board is divided based on divisor, thicker lines are used to show the divisions that 
                # make up the sub-grids
            for col in range(grid.__len__()):
                square = pygame.Rect(col_offset+(col*square_size), row_offset+(row*square_size), square_size, square_size)
                value = self.font.render("" if grid[row][col] == 0 else str(grid[row][col]), True, (0, 0, 0))
                val_rect = value.get_rect()
                val_rect.center = square.center
                self.screen.blit(value, val_rect)
                self.board[row].append(square)
                pygame.draw.rect(self.screen, (0, 0, 0), square, 1)
                # the squares are created within the boundaries of the grid, and smaller rectangles with the preset
                # puzzle values are displayed within the squares where their coordinates are found from the input array
                if(col%column_divisor==0 and col != 0):
                    pygame.draw.line(self.screen, (0, 0, 0), (col_offset+(col*square_size), row_offset+(row*square_size)), 
                    (col_offset+(col*square_size), row_offset+(grid.__len__()*square_size)), 8)
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

    def print_performance(self, time, no_mistakes):
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(50, self.performance_rect.top+35, 330, 55))
        self.screen.blit(pygame.font.Font(None, 23).render("Time taken: "+str(time), True, (0,0,0)), 
        (self.performance_rect.left+5, self.performance_rect.top+35))
        self.screen.blit(pygame.font.Font(None, 23).render("Mistakes made: "+str(no_mistakes), True, (0,0,0)), 
        (self.performance_rect.left+5, self.performance_rect.top+55))
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