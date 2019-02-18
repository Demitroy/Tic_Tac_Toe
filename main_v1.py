# My Tic_Tac_Toe Game


# Setting up the play space.  Tic Tac Toe is comprised of 3 rows, each having 3 columns.
# To make checking for valid plays easier, each possible play location has been initiated with "0".
board = [[0,0,0],[0,0,0],[0,0,0]]
valid_play = ['00','01','02','10','11','12','20','21','22']
winner = False
turns = 0
mark = "O"

while winner == False:
    turns += 1
    if mark == "O":
        mark = "X"
    else:
        mark = "O"
    play = input("Play Location: ")
    if play == '99':
        quit
    while play not in valid_play:
        play = input("Play Location: ")
    while board[int(play[0])][int(play[1])] != 0:
        play = input("Play Location: ")
    board[int(play[0])][int(play[1])] = mark
    for i in board:
        print(i)
