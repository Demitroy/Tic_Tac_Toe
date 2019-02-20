# My Tic_Tac_Toe Game

# functions for setting the mark to be placed for the next play
def set_mark(mark):
    if mark == "O":
        return "X"
    return "O"

def get_play():
    play = input("Play Location: ")
    if play not in valid_play:
        play = get_play()
    if board[int(play[0])][int(play[1])] != 0:
        play = get_play()
    return int(play[0]),int(play[1])

def check_winner(r,c):
    if board[r][0] == board[r][1] and board[r][0] == board[r][2]:
        return True
    if board[0][c] == board[1][c] and board[0][c] == board[2][c]:
        return True
    if board[1][1] != 0:
        if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
            return True
        if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
            return True
    return False
    
# Setting up the play space.  Tic Tac Toe is comprised of 3 rows, each having 3 columns.
# To make checking for valid plays easier, each possible play location has been initiated with "0".
board = [[0,0,0],[0,0,0],[0,0,0]]
valid_play = ['00','01','02','10','11','12','20','21','22']
winner = False
turns = 0
mark = "O"

while winner == False:
    turns += 1
    mark = set_mark(mark)
    r,c = get_play()
    board[r][c] = mark
    for i in board:
        print(i)
    print(turns)
    winner = check_winner(r,c)
    if turns >= 9 and winner == False:
        mark = "Draw"
        winner = True
print("Winner is: " + mark)
