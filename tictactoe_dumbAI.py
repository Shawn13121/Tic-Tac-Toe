import random

class Board:

    def __init__(self):
        self.board = [i for i in range(1,10)]

    def draw_board(self):
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def check_win(self): 
        win_combinations = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
        if self.board.count('X') + self.board.count('O') == 9: #Check if the board is full in case of a tie
            return True
        return any((self.board[comb[0]-1] == self.board[comb[1]-1] == self.board[comb[2]-1]) for comb in win_combinations)

game_board = Board()

def who_first_move():
    first = random.randint(0, 1)
    if first == 0:
        return 1 #Player
    return 0 #Computer

def player_turn():
    #Computer is O.
    # Player is X.  
    x_count = game_board.board.count('X')
    o_count = game_board.board.count('O')
    return x_count == o_count  

def available_slots():
    available = []
    for i in game_board.board:
        if str(i).isdigit():
            available.append(i)
    random.shuffle(available)
    return available

def computer_move():
    copy = game_board

    #First: Try to win
    for i in available_slots():
        copy.board[i-1] = 'O'
        if Board.check_win(copy):
            return i
        copy.board[i-1] = i
        
            
    #Second: Try to block player from winning
    for i in available_slots():
        copy.board[i-1] = 'X'
        if Board.check_win(copy):
            return i
        copy.board[i-1] = i

    #Third: Try to get a corner tile
    for i in available_slots():
        if i in (1, 3, 7, 9):
            return i
    
    #Fourth: Try to get the center tile
    for i in available_slots():
        if i == 5:
            return i

    #Fifth: Try to get a side tile
    for i in available_slots():
        if i in (2, 4, 6, 8):
            return i
    
def player_move():
    while True:
        try:
            slot = input(f"\n{player}, pick a slot (1-9): ")
            if slot.isnumeric() == False:
                raise ValueError
            elif int(slot) not in range(1,10) or game_board.board[int(slot)-1] in ('X', 'O'):
                raise ValueError
            break
        except ValueError:    
            print("This slot is not available.\n")
            continue
    return slot

def main():
    print("\nAlright! Let's begin.")
    turn = who_first_move()
    print(f"The {'player' if turn == 1 else 'computer'} will go first.")

    while Board.check_win(game_board) == False:
        if turn%2 == 0:
            print("\nIt's the computer's turn.")
            game_board.board[int(computer_move())-1] = 'O'
            turn += 1
        elif turn%2 == 1:
            print("\nIt's your turn.")
            game_board.board[int(player_move())-1] = 'X'
            turn += 1
        Board.draw_board(game_board)

def place_char(pos):
    if player_turn():
        game_board.board[int(player_move())-1] = 'X'
    else:
        game_board.board[int(computer_move())-1] = 'O'  


player = input("Let's play tic-tac-toe! What is your name? ")

answer = 'y'
while answer.lower() == 'y':
    main()
    print("\nGame Over.")
    answer = input("Play again? [y/n] ")

print("Thanks for playing!")