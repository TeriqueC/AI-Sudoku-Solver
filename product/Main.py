from copy import deepcopy
import time
from Sudoku import Sudoku, pygame
from Backtracking import backtracking, mistakes_made
from CNN import solve_sudoku, calc_mistakes_made

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
    [1,0,4,0,6,8,0,7,0],
    [8,0,0,0,7,1,6,2,4],
    [0,0,5,0,3,0,0,0,0],
    [0,0,1,0,0,7,4,6,2],
    [2,0,0,3,0,0,7,0,0],
    [0,0,7,0,2,0,3,0,5],
    [0,7,6,0,1,0,0,0,9],
    [0,8,0,0,0,0,1,0,0],
    [4,0,3,0,8,0,2,0,6]
]
# normal 9x9 sudoku

grid_4 = [
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
# hard 9x9 sudoku

grid_5 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# this is the solution to the test puzzle
"""
[[5, 3, 4, 6, 7, 8, 9, 1, 2],
 [6, 7, 2, 1, 9, 5, 3, 4, 8],
 [1, 9, 8, 3, 4, 2, 5, 6, 7],
 [8, 5, 9, 7, 6, 1, 4, 2, 3],
 [4, 2, 6, 8, 5, 3, 7, 9, 1],
 [7, 1, 3, 9, 2, 4, 8, 5, 6],
 [9, 6, 1, 5, 3, 7, 2, 8, 4],
 [2, 8, 7, 4, 1, 9, 6, 3, 5],
 [3, 4, 5, 2, 8, 6, 1, 7, 9]]
"""

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
                solution = deepcopy(current_grid)
                start = time.time()
                sudoku.print_grid(backtracking(solution, sudoku))
                end = time.time()
                time_taken= end-start
                sudoku.print_performance(time_taken, mistakes_made())
                # when the enter key is pressed, it signals the start of the backtracking solver, the solution will be displayed to the
                # window while being solved, and the final solution will also be displayed to the terminal. unless a solution is not found
                # and a empty sudoku puzzle is displayed and "solution not found" printed in the terminal.
            elif event.key == pygame.K_SPACE:
                start = time.time()
                solution = solve_sudoku(current_grid).tolist()
                end = time.time()
                time_taken= end-start
                sudoku.print_performance(time_taken, calc_mistakes_made(solution))
                sudoku.print_grid(solution)
                sudoku.draw_grid(solution)
            elif event.key == pygame.K_BACKSPACE:
                sudoku.draw_grid(current_grid)
            elif event.key == pygame.K_1:
                current_grid = grid_3
                sudoku.draw_grid(current_grid)
            elif event.key == pygame.K_2:
                current_grid = grid_5
                sudoku.draw_grid(current_grid)
            elif event.key == pygame.K_3:
                current_grid = grid_4
                sudoku.draw_grid(current_grid)
            elif event.key == pygame.K_4:
                current_grid = u_grid
                sudoku.draw_grid(current_grid)
        elif event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.ACTIVEEVENT:
            continue
        # handles other events in way that does not interrupt or crash the GUI before the solving algorithm can find a solution
# a simple interface to link the printing and solving functionalities