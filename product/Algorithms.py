# the method containing the main backtracking algorithm
def backtracking(grid, sudoku):
    position = empty_space(grid)
    # locates an empty square on the grid and stores its location
    if position == None:
        return grid
        # if there are no empty squares, the solution has been found and the grid is returned
    for i in range(1, grid.__len__()+1):
        sudoku.update(i, position[0], position[1])
        # updates the GUI to display the current attempt for a viable value
        if safe_value(grid, position, i):
            grid[position[0]][position[1]] = i
            # test a viable number in the open position
            backtracking(grid, sudoku)
            # checks the next space after the previous viable solution
            if(empty_space(grid)==None):
                return grid
                # if the are no empty positions, this solution is correct
        grid[position[0]][position[1]] = 0
        # if the current value is not viable, it is set to 0, but the i remains as the none viable solution to be incremented
        sudoku.update(0, position[0], position[1])
        # updates the GUI to clear the current square
    return None
    # if there is no number that goes into the empty position, an empty grid is returned as there is no solution
            
    
def empty_space(grid):
    for i in range(grid.__len__()):
        for j in range(grid.__len__()):
            if grid[i][j] == 0:
                return [i,j]
    return None
# finds a position in the grid where there is a 0, an empty value to be filled

def check_row(grid, row, value):
    for i in range(grid.__len__()):           
        if(grid[row][i]==value):
            return False
    return True
# checks if the value has not been used in the row yet

def check_column(grid, column, value):
    for i in range(grid.__len__()):
        if(grid[i][column]==value):
            return False
    return True
# checks if the value has not been used in the column yet

def check_square(grid, row, column, value):
    divisor = grid.__len__() ** 0.5
    if(divisor%1!=0):
        row_divisor = round(divisor)
        column_divisor = round(divisor)+1
    else: row_divisor, column_divisor = divisor, divisor
    # divisor logic used in printing method to divide the grid into squares based off its rows and columns
    for i in range(int(row_divisor)):
        for j in range(int(column_divisor)):
            if(grid[int(row_divisor*(row//row_divisor))+i][int(column_divisor*(column//column_divisor))+j]==value):
                return False
    return True
# checks squares in which the sudoku is divided into, and returns if the value has not been used yet

def safe_value(grid, position, value):
    return check_row(grid, position[0], value) and check_column(grid, position[1], value) and check_square(grid, position[0], position[1], value)
# simplyfies the process of checking values in the main algorithm function