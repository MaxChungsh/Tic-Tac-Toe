import random

def display_board(board):
    print("-1-+-2-+-3-")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-4-+-5-+-6-")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-7-+-8-+-9-")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def get_player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == ' ':
            return int(move) - 1
        print("Invalid move. Try again.")

def get_computer_move(board):
    # Implement your own AI algorithm here
    # Stop/attain win
    for i in range(0, 9, 3):
        if board[i] == board[i+1] != ' ' and board[i+2] == ' ':
            return i+2
        if board[i] == board[i+2] != ' ' and board[i+1] == ' ':
            return i+1
        if board[i+1] == board[i+2] != ' ' and board[i] == ' ':
            return i
    for i in range(3):
        if board[i] == board[i+3] != ' ' and board[i+6] == ' ':
            return i+6
        if board[i] == board[i+6] != ' ' and board[i+3] == ' ':
            return i+3
        if board[i+3] == board[i+6] != ' ' and board[i] == ' ':
            return i
    if board[0] == board[4] != ' ' and board[8] == ' ':
        return 8
    if board[0] == board[8] != ' ' and board[4] == ' ':
        return 4
    if board[4] == board[8] != ' ' and board[0] == ' ':
        return 0
    if board[2] == board[4] != ' ' and board[6] == ' ':
        return 6
    if board[2] == board[6] != ' ' and board[4] == ' ':
        return 4
    if board[4] == board[6] != ' ' and board[2] == ' ':
        return 2

    # No stress
    if board[4] == ' ':
        return 4
    if board[0] == ' ':
        return 0
    if board[2] == ' ':
        return 2
    if board[6] == ' ':
        return 6
    if board[8] == ' ':
        return 8
    available_moves = [i for i, space in enumerate(board) if space == ' ']
    return random.choice(available_moves)




def play_game():
    board = [' '] * 9
    current_player = 'X'
    print("You are X")
    print("The order will be random")
    if random.randint(0, 1) == 0:
        print("You first")
    else:
        print("Computer first")
        move = get_computer_move(board)
        print(f"Computer plays at position {move}.")

    while True:
        display_board(board)
        print("Your turn.")

        if current_player == 'X':
            move = get_player_move(board)
        else:
            move = get_computer_move(board)
            print(f"Computer plays at position {move}.")

        board[move] = current_player

        if check_win(board, current_player):
            display_board(board)
            if current_player == 'X':
                print("You win!")
            elif current_player == 'O':
                print("You lose!")
            return

        if all(space != ' ' for space in board):
            display_board(board)
            print("It's a tie!")
            return

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

play_game()