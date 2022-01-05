import random


class TicTacToe:

    #here I define a game board for general use; it is a list, which is empty at first.
    def __init__(self):
        self.board = []

    #here the method creates actually the specific board. First it fills up a column with the 3 items with the '-' sign to form the list of the row, which it puts into the board. Then twice it does the same thing to complete the board with the '-' signs.  
    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    #method to define who starts first; the module random was imported from a predefined file.
    def get_random_first_player(self):
        return random.randint(0, 1)

    # method used to put the sign of the player to the right coordinate (place) chosen by the player and assign it to the player (X or O). It is a nested list. In self board there are 3 lists and in each list there are 3 elments. So the player value is defined as one element (col value) of one of the three lists (row value). In fact the board is a pseudo 2 dimensional array, despite that when it is printed it looks like one. This is because in the printed form the code 'end' was introduced, so lists (colums) were put next to each other and not underneath as with a \n. 
    def fix_spot(self, row, col, player):
        self.board[row][col] = player
    # method to analyse at what stage the game stands
    def is_player_win(self, player):
        win = None
        # n=3 because there are 3 elements named rows.
        n = len(self.board)

        # checking rows, if the player has not 3 of his sign win turns false, stop verifying the remaining items  and  the winner will not be printed when called; if win then win stays true and the winner will be printed when called in the while loop.
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns, see comment above
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals, see comment above. It is a bit more tricky specially when diagonal from the right end is analysed.
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        # here we need n-1 because i values are 0, 1 or 2.
        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        # I am not sure that this code is necessary, because when it is called the while loop is disrupted anyway. Do we need it because the computer is still working behind the scenes?
        return False

    # it seems this code is a duplicate and an error, what we can delete.
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
    
    # this code is necessary to verify whether the game has ended or not, and if ended then in the while loop it will stand for True and printed there is no winner. Otherwise False and the code skipped when called.
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True
    
    # change the player
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'
    
    #  when the board was created, it was assigned memory boxes, but actually could not be printed. the end code is important, otherwise we have 3 times 3 columns printed and not an array of 3X3. Actually we are not working with an array.
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    # Here is where the game starts. First the board is called in and the first player is chosen randomnly.
    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        
        # the game here enters a loop until it ends.
        while True:
            #it prints whose turn it is
            print(f"Player {player} turn")
            #shows the board, so the player can chose the right box
            self.show_board()

            # taking user input; several functions in one code line; split function tells that two inputs were given and should be treated separately; inputs are always strings, so we have to convert them into integers; map iterates the function int for the two entries; the player entered values of row and col are elements of a lisst. 
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # the method fix_spot is called; -1 is needed because for the player row number starts with 1, while in a list it starts with 0. 
            self.fix_spot(row - 1, col - 1, player)

            # the method self.is_player_win is called; print is excecuted only if win = True, then the game is over and the loop is terminated.
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not; see also comment above.
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn; it is called within the loop inspite there is no if term with true or false assigned to it. If it were outside the loop a new player would be assigned while the game was over.
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
