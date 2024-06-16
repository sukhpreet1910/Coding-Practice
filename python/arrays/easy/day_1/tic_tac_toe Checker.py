def is_solved(board):
    # TODO: Check if the board is solved!
    
    def is_winner(player, set):
        return all(cell == player for cell in set)
    
    
#     forward diagonal

    forward_diag = [board[0][0], board[1][1], board[2][2]]
    
    if is_winner(1, forward_diag):
        return 1
    elif is_winner(2, forward_diag):
        return 2
    
    
#     back_diag

    back_diag = [board[0][2], board[1][1], board[2][0]]
    
    if is_winner(1, back_diag):
        return 1
    elif is_winner(2, back_diag):
        return 2
    
    
#     row 
    for i in range(3):
        row = board[i]
        if is_winner(1, row):
            return 1
        elif is_winner(2, row):
            return 2
    
    for i in range(3):
        col = [board[0][i], board[1][i], board[2][i]]
        if is_winner(1, col):
            return 1
        elif is_winner(2, col):
            return 2
        
    if all(cell != 0 for row in board for cell in row ):
        return 0
    
    return -1
    