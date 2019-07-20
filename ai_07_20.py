from math import inf as infinity

computer_mark = "o"
user_mark = "x"

def minmax(state, depth, player):
    if player == "computer":
        best = [-1, -infinity]
    else:
        best = [-1, +infinity]
    if depth == 0 or checkGame(game_board):
        score = evaluate()
        return [-1, -1, score]

    for cell in empty_cells():
        location = cell
        game_board[location] = player

        if(player == "computer"):
            player = "user"
        else:
            player = "computer"

        score = minmax(state, depth -1, player)
        game_board[location] = "U"
        score[0] = location

        if player == "computer":
            if(score[1] > best[1]):
                best = score #max
            else:
                if(score[1] < best[1]):
                    best = score # min
    return best

def evaluate():
    if(wins( computer_mark )):
        score = 1
    elif(wins(user_mark)):
        score = 1
    else:
        score = 0
    return score

def empty_cells():
    cells = []
    for i, y in enumerate(game_board):
        if(y == 'U'):
            cells.append(i)

    return cells