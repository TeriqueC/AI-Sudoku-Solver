from Sudoku import Sudoku, pygame
from Algorithms import backtracking

grid_1 = [
    [2,0,3,0],
    [0,4,0,2],
    [0,2,0,3],
    [4,0,2,0]
]
# simple 4x4 sudoku

grid_2 = [
    [3,0,1,0,0,6],
    [0,0,4,0,0,0],
    [5,1,2,3,0,4],
    [4,6,0,1,2,5],
    [1,0,5,0,0,0],
    [2,0,6,0,1,0]
]
# slightly more challenging 6x6 sudoku

grid_3 = [
    [0,0,0,0,0,2,0,0,0],
    [1,0,3,4,0,0,0,0,5],
    [2,0,0,0,5,0,4,0,1],
    [3,4,0,0,0,5,0,9,0],
    [8,0,7,0,0,0,3,0,4],
    [0,9,0,3,0,0,0,1,7],
    [6,0,5,0,3,0,0,0,9],
    [4,0,0,0,0,8,7,0,2],
    [0,0,0,1,0,0,0,0,0]
]
# normal 9x9 sudoku

u_grid = [
    [0,0,0,0,0,0,0,0,2],
    [1,0,3,4,0,0,0,0,5],
    [2,0,0,0,5,0,4,0,1],
    [3,4,0,0,0,5,0,9,0],
    [8,0,7,0,0,0,3,0,4],
    [0,9,0,3,0,0,0,1,7],
    [6,0,5,0,3,0,0,0,9],
    [4,0,0,0,0,8,7,0,2],
    [0,0,0,1,0,0,0,0,0]
]
# this a sudoku with no solution as the last column has a repeated value,this is to see how the algorithms responds to unsolvable problems

U = "unsolved:"
S = "solved:"

sudoku = Sudoku()
current_grid = grid_3
print(U)
sudoku.print_grid(current_grid)
print(S)
# prints the unsolved sudoku grid to the terminal
sudoku.draw_grid(current_grid)
# creates window and displays the sudoku puzzle
running = True
while running:
    for event in pygame.event.get():
        # main application loop, checks for events to trigger actions in the GUI
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                sudoku.print_grid(backtracking(current_grid, sudoku))
                # when the enter key is pressed, it signals the start of the backtracking solver, the solution will be displayed to the
                # window while being solved, and the final solution will also be displayed to the terminal. unless a solution is not found
                # and a empty sudoku puzzle is displayed and "solution not found" printed in the terminal.
        elif event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.ACTIVEEVENT:
            continue
        # handles other events in way that does not interrupt or crash the GUI before the solving algorithm can find a solution
# a simple interface to link the printing and solving functionalities