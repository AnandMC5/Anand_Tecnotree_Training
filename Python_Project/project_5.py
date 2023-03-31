# import random

# # Define the board as a list of empty strings
# board = [""] * 9

# # Function to display the Tic Tac Toe board
# def display_board():
#     print(board[0] + " | " + board[1] + " | " + board[2])
#     print("---------")
#     print(board[3] + " | " + board[4] + " | " + board[5])
#     print("---------")
#     print(board[6] + " | " + board[7] + " | " + board[8])

# # Function to check if there is a winner
# def check_winner(player):
#     if board[0] == board[1] == board[2] == player:
#         return True
#     elif board[3] == board[4] == board[5] == player:
#         return True
#     elif board[6] == board[7] == board[8] == player:
#         return True
#     elif board[0] == board[3] == board[6] == player:
#         return True
#     elif board[1] == board[4] == board[7] == player:
#         return True
#     elif board[2] == board[5] == board[8] == player:
#         return True
#     elif board[0] == board[4] == board[8] == player:
#         return True
#     elif board[2] == board[4] == board[6] == player:
#         return True
#     else:
#         return False

# # Function to check if the game is a tie
# def check_tie():
#     for i in range(9):
#         if board[i] == "":
#             return False
#     return True

# # Main function to play the game
# def play_game():
#     print("Welcome to Tic Tac Toe!")
#     print("You are X, and the computer is O.")
#     print("The board is numbered from 0 to 8 as shown below:")
#     display_board()
#     print("Let's start the game!")
#     while True:
#         # Player's turn
#         while True:
#             player_move = input("Enter a number from 0 to 8 to place X: ")
#             if player_move.isdigit() and int(player_move) in range(9) and board[int(player_move)] == "":
#                 break
#             else:
#                 print("Invalid input. Please try again.")
#         board[int(player_move)] = "X"
#         display_board()
#         if check_winner("X"):
#             print("Congratulations! You won the game!")
#             break
#         if check_tie():
#             print("The game is a tie!")
#             break
#         # Computer's turn
#         while True:
#             computer_move = random.randint(0, 8)
#             if board[computer_move] == "":
#                 break
#         board[computer_move] = "O"
#         print("The computer placed O in", computer_move)
#         display_board()
#         if check_winner("O"):
#             print("Sorry! The computer won the game!")
#             break
#         if check_tie():
#             print("The game is a tie!")
#             break

# # Start the game
# play_game()

# Set up the board
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Function to display the board
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

# Function to check if there is a winner
def check_winner(player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

# Function to check if the game is a tie
def check_tie():
    for i in range(9):
        if board[i] == " ":
            return False
    return True

# Main function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Player 1 goes first (X)")
    display_board()
    while True:
        # Player 1's turn
        while True:
            move = input("Enter a position (1-9) for X: ")
            if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " ":
                break
            else:
                print("Invalid move. Please try again.")
        board[int(move)-1] = "X"
        display_board()
        if check_winner("X"):
            print("Congratulations! Player 1 (X) has won the game!")
            break
        if check_tie():
            print("The game is a tie!")
            break
        # Player 2's turn
        while True:
            move = input("Enter a position (1-9) for O: ")
            if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " ":
                break
            else:
                print("Invalid move. Please try again.")
        board[int(move)-1] = "O"
        display_board()
        if check_winner("O"):
            print("Congratulations! Player 2 (O) has won the game!")
            break

# Start the game
play_game()
