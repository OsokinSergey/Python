def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Проверка строк
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Проверка столбцов
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    player = "X"
    turns = 0

    while turns < 9:
        print_board(board)
        print(f"Ходит игрок {player}")

        row = int(input("Выберите строку (0, 1, 2): "))
        col = int(input("Выберите столбец (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = player
            turns += 1

            if check_winner(board):
                print_board(board)
                print(f"Игрок {player} победил!")
                return

            player = "O" if player == "X" else "X"
        else:
            print("Эта клетка уже занята!")

    print_board(board)
    print("Ничья!")

play_game()