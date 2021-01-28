the_board = [i for i in range(1,10)]

def setup(board):
    global player1, player2
    print("Let's play tic-tac-toe! Please enter your names.\n")
    player1 = input("[Player 1] : ")
    player2 = input("[Player 2] : ")
    print("\nAlright! Let's begin.")

    draw_board(board)
    move(board)
    print("Game Over.")

def draw_board(board):
    spot = 1
    for tile in board:
        if spot == 3 or spot == 6:
            end = ' \n---------\n'
        elif spot == 9:
            end = ' \n'
        else:
            end = ' | '
        char = ' '
        if tile in ('X', 'O'):
            char = tile
        spot += 1
        print(char, end=end)
    
def player_turn(board):
    x_count = board.count('X')
    o_count = board.count('O')
    return x_count == o_count

def move(board):
    global player1, player2
    while check_win(board) == False:
        while True:
            try:
                slot = input(f"\n{player1 if player_turn(board) else player2}, pick a slot (1-9): ")
                if slot.isnumeric() == False:
                    raise ValueError
                elif int(slot) not in range(1,10) or board[int(slot)-1] in ('X', 'O'):
                    raise ValueError
                break
            except ValueError:    
                print("This slot is not available.\n")
                continue

        if player_turn(board):
            board[int(slot)-1] = 'X'  
        else:
            board[int(slot)-1] = 'O'         

        draw_board(board)
    return False
        
def check_win(board): 
    win_combinations = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))
    if board.count('X') + board.count('O') == 9:
        return True
    else:
        return any((board[comb[0]-1] == board[comb[1]-1] == board[comb[2]-1]) for comb in win_combinations)

def new_game(): #Not working...
    restart = input("Play again? [y/n] ")
    if restart == 'y':
        new_board = [i for i in range(1, 10)]
        print(new_board)
        print("\nAlright! Let's play again!")
        setup(new_board)
    else:
        print("Thanks for playing!")

setup(the_board)

if not move(the_board):
    new_game()
