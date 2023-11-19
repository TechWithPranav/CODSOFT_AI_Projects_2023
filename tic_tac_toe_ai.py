import random
from colorama import Fore, Style

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 13)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    scores = {'X': -1, 'O': 1, 'tie': 0, ' ': 0}


    if check_winner(board):
        return scores[board[1][1]]

    if is_board_full(board):
        return scores['tie']

    if is_maximizing:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        move_val = minimax(board, 0, False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = random.choice([True, False])

    while True:
        print_board(board)

        if player_turn:
            print(Fore.BLUE + "Your turn ---X---" + Style.RESET_ALL)
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        else:
            print(Fore.RED + "AI's turn ---O---" + Style.RESET_ALL)
            row, col = best_move(board)

        if board[row][col] == ' ':
            symbol = 'X' if player_turn else 'O'
            board[row][col] = symbol

            if check_winner(board):
                print_board(board)
                print('\n==============================================================\n')
                print(Fore.GREEN + f"{symbol} wins...!!!" + Style.RESET_ALL)
                print('\n==============================================================\n')
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            player_turn = not player_turn

        else:
            print("Cell already occupied. Try again.")

if __name__ == "__main__":
    main()
