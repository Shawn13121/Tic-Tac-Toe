class Board:

    def __init__(self):
        self.board = [i for i in range(1,10)]

    def draw_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def game_over(self, first_player, second_player): 
        win_combinations = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
        win_X = any((self.board[comb[0]-1] == self.board[comb[1]-1] == self.board[comb[2]-1] == 'X') for comb in win_combinations)
        win_O = any((self.board[comb[0]-1] == self.board[comb[1]-1] == self.board[comb[2]-1] == 'O') for comb in win_combinations)
        if win_X:
            return first_player #Player 1 wins
        elif win_O:
            return second_player #Player 2 wins
        elif self.board.count('X') + self.board.count('O') == 9 and not win_O or win_X:
            return 'Nobody' #Tie
        else:
            return 'Game not over'


def main():
    game_board = Board()

    print("\nAlright! Let's begin.")

    def player_turn():
        x_count = game_board.board.count('X')
        o_count = game_board.board.count('O')
        return x_count == o_count   

    while Board.game_over(game_board, player1, player2) == 'Game not over':
        #This loop will keep running until it detects a win/tie.

        while True:
            try:
                slot = input(f"\n{player1 if player_turn() else player2}, pick a slot (1-9): ")
                if slot.isnumeric() == False: 
                    #If the input is not an integer
                    raise ValueError
                elif int(slot) not in range(1,10) or game_board.board[int(slot)-1] in ('X', 'O'):
                    #If the integer is not between 1 and 9, or it's already occupied
                    raise ValueError
                break
            except ValueError:    
                print("This slot is not available.\n")
                continue

        if player_turn():
            #If there's the same number of X's and O's on the board, then it's X's turn.
            game_board.board[int(slot)-1] = 'X'  
        else:
            game_board.board[int(slot)-1] = 'O'         

        Board.draw_board(game_board)

    #Specify who won once the game ends:
    print(f"\nGame Over. {Board.game_over(game_board, player1, player2)} won!")


#First round only: setting up the game
print("Let's play tic-tac-toe! Please enter your names.\n")
player1 = input("[Player 1] : ")
player2 = input("[Player 2] : ")

answer = 'y'
while answer.lower() == 'y':
    main()
    answer = input("Play again? [y/n] ")

print("Thanks for playing!")