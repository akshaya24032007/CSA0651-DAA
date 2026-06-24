def game(board):
    b = [row[:] for row in board]

    for i in range(len(board)):
        for j in range(len(board[0])):
            c = 0
            for r in range(max(0,i-1), min(len(board),i+2)):
                for k in range(max(0,j-1), min(len(board[0]),j+2)):
                    c += b[r][k]

            c -= b[i][j]

            if b[i][j] and c not in [2,3]:
                board[i][j] = 0
            elif not b[i][j] and c == 3:
                board[i][j] = 1

    return board

print(game([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
