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

def print_grid(grid):
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

print_grid(grid_1)
print()
print_grid(grid_2)
print()
print_grid(grid_3)