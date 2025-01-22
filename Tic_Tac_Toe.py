def print_board(board):
    for row in board:
        print(" |  ".join(row))
        print("-" * 12)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)


def get_player_input(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row and column): ").strip()
            row, col = map(int, move.split())
            if row in range(3) and col in range(3) and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter row and column as two integers separated by a space (e.g., 1 2).")


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    current_player = 'X'
    while True:
        row, col = get_player_input(board, current_player)
        board[row][col] = current_player
        print_board(board)
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'


play_game()
