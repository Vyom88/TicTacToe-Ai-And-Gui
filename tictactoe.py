import math
import copy

X = "X"
O = "O"
EMPTY = None

#good
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

#good
def player(board):
    x_count = 0
    o_count = 0
    for x in board:
        for y in x:
            if y == 'X':
                x_count += 1
            elif y == 'O':
                o_count += 1
    if x_count <= o_count:
        return "X"
    else:
        return "O"

#good
def actions(board):
    arr = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == None:
                arr.append((x, y))
    return arr



def result(board, action):
#    print (board)
    tempboard = copy.deepcopy(board)
    tempboard[action[0]][action[1]] = player(board)
#    print (board)
    return tempboard


def winner(board):
    out = utility(board)
    
    if out == 1:
        return 'X'
    
    if out == -1:
        return 'O'
    
    else:
        return 'Tie'


def terminal(board):
    ret = False
    waste = True
    for x in board:
        for y in x:
            if y == None:
                waste = False

    if waste == True:
        ret = True

    for x in board:
        if x[0] == x[1] == x[2] != None:
            ret = True

    for x in range(3):
        if board[0][x] == board[1][x] == board[2][x] != None:
            ret = True

    if board[0][0] == board[1][1] == board[2][2] != None:
        ret = True
    
    if board[0][2] == board[1][1] == board[2][0] != None:
        ret = True
    return ret


def utility(board):
    XO = 0
    for x in board:
        if x[0] == x[1] == x[2] == 'X':
            XO = 1
    
    for x in range(3):
        if board[0][x] == board[1][x] == board[2][x] == 'X':
            XO = 1
        
    if board[0][0] == board[1][1] == board[2][2] == 'X':
        XO = 1
    
    if board[0][2] == board[1][1] == board[2][0] == 'X':
        XO = 1


    for x in board:
        if x[0] == x[1] == x[2] == 'O':
            XO = -1
    
    for x in range(3):
        if board[0][x] == board[1][x] == board[2][x] == 'O':
            XO = -1
        
    if board[0][0] == board[1][1] == board[2][2] == 'O':
        XO = -1
    
    if board[0][2] == board[1][1] == board[2][0] == 'O':
        XO = -1
    
    return XO


def minimax(board, depth):
    waste = False
    for x in board:
        for y in x:
            if y == None:
                waste = True
            else:
                waste = False
                break
        
        if waste == False:
            break
    
    if waste == True:
        return [0, 0, 0]

    out = 0
    m = []
    if player(board) == 'O':
        for x in range(3):
            for y in range(3):
                if board[x][y] != None:
                    out += 1
                    m = [x, y]
                    if out > 1:
                        break
            if out > 1:
                break

        if out == 1:
            if board[0][0] == 'X':
                return [0, 2, 2]
            elif board[2][0] == 'X':
                return [0, 0, 2]
            elif board[0][2] == 'X':
                return [0, 2, 0]
            elif board[2][2] == 'X':
                return [0, 0, 0]

    
    tempboard = copy.deepcopy(board)
    lis = []
    count = [0, 0, 0]
    for action in actions(tempboard):
        tempboard2 = result(tempboard, action)
        if terminal(tempboard2):
            l = [utility(tempboard2), action[0], action[1], depth]
        else:
            l = minimax(tempboard2, depth+1)
        if l[0] == -1:
            count[0] += 1
        elif l[0] == 0:
            count[1] += 1
        elif l[0] == 1:
            count[2] += 1
        
        lis.append(l)
#    print (lis)
#    print (board)
    if player(tempboard) == 'X':
        lis2 = []
        max = 1
        for x in lis:
            if x[0] < max:
                max = x[0]
                lis2 = x
            elif lis2 == []:
                max = x[0]
                lis2 = x
            elif x[0] == max and x[3] <= lis2[3]:
                max = x[0]
                lis2 = x
            
        if lis2[0] == -1:
            lis2[3] -= count[0]
        elif lis2[0] == 0:
            lis2[3] -= count[1]
        elif lis2[0] == 1:
            lis2[3] -= count[2]
            
        return lis2

    elif player(tempboard) == 'O':
        lis2 = []
        min = -1
        for x in lis:
            if x[0] > min:
                min = x[0]
                lis2 = x
            elif lis2 == []:
                min = x[0]
                lis2 = x
            elif x[0] == min and x[3] >= lis2[3]:
                min = x[0]
                lis2 = x
            
        if lis2[0] == -1:
            lis2[3] -= count[0]
        elif lis2[0] == 0:
            lis2[3] -= count[1]
        elif lis2[0] == 1:
            lis2[3] -= count[2]
            
        return lis2