# sudoku_board = [
#     [6, 8, 0, 4, 0, 3, 0, 5, 0],
#     [4, 0, 2, 0, 5, 0, 3, 6, 8],
#     [5, 9, 3, 6, 7, 8, 0, 0, 4],
#     [0, 1, 7, 2, 8, 6, 9, 4, 5],
#     [8, 0, 9, 5, 0, 4, 2, 0, 7],
#     [2, 5, 4, 3, 9, 7, 8, 1, 0],
#     [7, 0, 0, 8, 3, 1, 5, 9, 2],
#     [9, 3, 5, 0, 6, 0, 4, 0, 1],
#     [0, 2, 0, 9, 0, 5, 0, 7, 3]
# ]

sudoku_board = [
    [2, 0, 9, 0, 0, 0, 6, 0, 0],
    [0, 4, 0, 8, 7, 0, 0, 1, 2],
    [8, 0, 0, 0, 1, 9, 0, 4, 0],
    [0, 3, 0, 7, 0, 0, 8, 0, 1],
    [0, 6, 5, 0, 0, 8, 0, 3, 0],
    [1, 0, 0, 0, 3, 0, 0, 0, 7],
    [0, 0, 0, 6, 5, 0, 7, 0, 9],
    [6, 0, 4, 0, 0, 0, 0, 2, 0],
    [0, 8, 0, 3, 0, 1, 4, 5, 0]
]

def solve_sudoku():
    for i in range(len(sudoku_board)):
        for j in range(len(sudoku_board[i])):
            if sudoku_board[i][j] == 0:
                choices = list(range(1, 10))

                for x in range(9):
                    if sudoku_board[i][x] in choices:
                        choices.remove(sudoku_board[i][x])
                
                for y in range(9):
                    if sudoku_board[y][j] in choices:
                        choices.remove(sudoku_board[y][j])
                
                for m in range((i//3)*3, (i//3)*3+3):
                    for n in range((j//3)*3, (j//3)*3+3):
                        if sudoku_board[m][n] in choices:
                            choices.remove(sudoku_board[m][n])
                
                if len(choices) == 1:
                    sudoku_board[i][j] = choices[0]
            
    for row in sudoku_board:
        print(row)
    print()
    
    for row_index in range(len(sudoku_board)):
        if 0 in sudoku_board[row_index]:
            solve_sudoku()

solve_sudoku()