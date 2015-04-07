def new_lines(board):
    new_board = ""
    delimiter = " | "
    
    for i in range(0, len(board) - 1):
        new_board += "| "
        for j in range(0, len(board[i])):
            new_board = new_board + board[i][j]
            if j != len(board) - 1:
                new_board += delimiter
        new_board += " |"
        new_board += str("\n")

    new_board += "| "
    for j in range(0, len(board)):
        new_board += board[len(board) - 1][j]
        if j != len(board) - 1:
            new_board += delimiter
        else:
            new_board += " |"        
    return new_board

def board_to_string(board):
    print(new_lines(board))

