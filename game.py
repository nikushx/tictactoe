print "Welcome to Multiplayer TicTacToe"
print "Developed by: Nikush Dalia"
print "Created to use data structures for real-world implications"
print ""
print "Instructions: Enter the position you would like to play when it is your turn."
print "The format for the position is [#A], where # is the row from [1-3] and A is the column, either [L, M, or R]"

repeat = 'y'

while repeat == 'y':
    #Set Blank Board
    def setBoard():

        board = {

            '1L':' ' , '1M':' ', '1R':' ',

            '2L':' ' , '2M':' ', '2R':' ',

            '3L':' ' , '3M':' ', '3R':' ',

        }

        return board

    #Prints Current Board
    def printBoard():

        print ""
        print(board['1L'] + '|' + board['1M'] + '|' + board['1R'])
        print('-+-+-')
        print(board['2L'] + '|' + board['2M'] + '|' + board['2R'])
        print('-+-+-')
        print(board['3L'] + '|' + board['3M'] + '|' + board['3R'])
        print ""

    def getPosition(currentPlayer):

        position = raw_input(names[currentPlayer] + ', please enter a position (ex. 2R): ')
        while ((len(position) != 2 or (position[0].isdigit() == False or position[1].isalpha == False) or (int(position[0]) < 1 or int(position[0]) > 3) or (position[1] != 'L' and position[1] != 'M' and position[1] != 'R')) or board[position] == 'X' or board[position] == 'O'):
            print "Error: Invalid Input or Already Taken"
            position = raw_input(names[currentPlayer] + ', please enter a position (ex. 2R): ')

        return position

    #Get Player Names
    def getPlayerNames():

        print ""
        name1 = raw_input("Please enter the name of Player 1 (X): ")
        name2 = raw_input("Please enter the name of Player 2 (O): ")
        return name1, name2

    def checkWin(win):

        if ((board['1L'] == 'X' and board['1M'] == 'X' and board['1R'] == 'X')
            or (board['2L'] == 'X' and board['2M'] == 'X' and board['2R'] == 'X')
            or (board['3L'] == 'X' and board['3M'] == 'X' and board['3R'] == 'X')
            or (board['1L'] == 'X' and board['2L'] == 'X' and board['3L'] == 'X')
            or (board['1M'] == 'X' and board['2M'] == 'X' and board['3M'] == 'X')
            or (board['1R'] == 'X' and board['2R'] == 'X' and board['3R'] == 'X')
            or (board['1L'] == 'X' and board['2M'] == 'X' and board['3R'] == 'X')
            or (board['1R'] == 'X' and board['2M'] == 'X' and board['3L'] == 'X')
            or (board['1L'] == 'O' and board['1M'] == 'O' and board['1R'] == 'O')
            or (board['2L'] == 'O' and board['2M'] == 'O' and board['2R'] == 'O')
            or (board['3L'] == 'O' and board['3M'] == 'O' and board['3R'] == 'O')
            or (board['1L'] == 'O' and board['2L'] == 'O' and board['3L'] == 'O')
            or (board['1M'] == 'O' and board['2M'] == 'O' and board['3M'] == 'O')
            or (board['1R'] == 'O' and board['2R'] == 'O' and board['3R'] == 'O')
            or (board['1L'] == 'O' and board['2M'] == 'O' and board['3R'] == 'O')
            or (board['1R'] == 'O' and board['2M'] == 'O' and board['3L'] == 'O')):
            win = True

        return win

    board = setBoard()
    names = getPlayerNames()

    win = False
    currentPlayer = 0

    while (win == False):

        printBoard()

        position = getPosition(currentPlayer)

        if currentPlayer == 0:
            board[position] = 'X'
        else:
            board[position] = 'O'

        win = checkWin(win)

        if (win == False):
            if currentPlayer == 0:
                currentPlayer = 1
            else:
                currentPlayer = 0

    printBoard()
    print "Congratulations, " + names[currentPlayer] + "! You won the game!"

    repeat = raw_input("Play again (y/n): ")
    while (repeat != 'y' and repeat != 'n'):
        print "Error: Invalid response"
        repeat = raw_input("Play again (y/n): ")