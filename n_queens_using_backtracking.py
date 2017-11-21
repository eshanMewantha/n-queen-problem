import numpy as np

# total number of queens
n = 8


# The checking of an attacking queen needs to be done only on the columns to the left of the column given
def is_safe(board, row, col):
    # Check this for columns on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check this for the north east diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check this for the south west diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def place_queen_in_column(board, column_id):
    # Termination condition. If all columns are being placed with a queen properly
    if column_id == n:
        return True

    # Iterate through all the rows in the given column
    for row_id in range(n):
        if is_safe(board, row_id, column_id):
            # Place this queen in board[i][col]
            board[row_id][column_id] = 1

            # Go to placing the next queen in the next column (recursive call)
            if place_queen_in_column(board, column_id + 1):
                return True

            # Placement of the queen lead to non-solution during recursive checking.
            # Thus vacant the position and place the queen in next safe row in the given column
            board[row_id][column_id] = 0

    # returns false when a queen cannot be placed in any row of this column
    return False


def solve_n_queen():
    global n
    # Create the chess board
    board = np.zeros((n, n))

    if not place_queen_in_column(board, 0):
        return False, None
    else:
        return True, board

# Find the solution
found_solution, solution = solve_n_queen()

if found_solution:
    print("\nSolution Configuration Found")
    print(np.array(solution))
else:
    print("\nSolution Configuration Not Found")
