import math
board = [" " for _ in range(9)]
def print_board():
    print("\n")
    for i in range(3):
        print(" " + board[3*i] + " | " + board[3*i+1] + " | " + board[3*i+2])
        if i < 2:
            print("---|---|---")
    print("\n")
def check_winner(b, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]           
    ]
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False
def is_draw(b):
    return " " not in b
def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw(b):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth+1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth+1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
def player_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if 0 <= pos < 9 and board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except:
            print("Enter a valid number.")
def play_game():
    print("TIC-TAC-TOE AI")
    print("Player = X | AI = O")
    while True:
        print_board()
        player_move()
        if check_winner(board, "X"):
            print_board()
            print("Player wins.")
            break
        if is_draw(board):
            print_board()
            print("Game is a draw.")
            break
        ai_move()
        if check_winner(board, "O"):
            print_board()
            print("AI wins.")
            break
        if is_draw(board):
            print_board()
            print("Game is a draw.")
            break
if __name__ == "__main__":
    play_game()