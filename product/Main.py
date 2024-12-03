import time
from Sudoku import print_grid, grid_1, grid_2, grid_3, u_grid
from Algorithms import backtracking

U = "unsolved:"
S = "solved:"

print(U)
print_grid(grid_1)
print(S)
print_grid(backtracking(grid_1))
time.sleep(2)

print(U)
print_grid(grid_2)
print(S)
print_grid(backtracking(grid_2))
time.sleep(2)

print(U)
print_grid(grid_3)
print(S)
print_grid(backtracking(grid_3))
time.sleep(2)

print(U)
print_grid(u_grid)
print(S)
print_grid(backtracking(u_grid))
time.sleep(2)

# a simple interface to link the printing and solving functionalities