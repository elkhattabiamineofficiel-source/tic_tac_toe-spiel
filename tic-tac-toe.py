def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Reihen prüfen
    for row in board:
        if all(s == player for s in row):
            return True
    # Spalten prüfen
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonalen prüfen
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    moves = 0

    print("Willkommen zum Tic-Tac-Toe!")
    print_board(board)

    while moves < 9:
        player = players[turn % 2]
        try:
            row = int(input(f"Spieler {player}, Reihe (0-2) wählen: "))
            col = int(input(f"Spieler {player}, Spalte (0-2) wählen: "))
            if board[row][col] == " ":
                board[row][col] = player
                print_board(board)
                if check_winner(board, player):
                    print(f"🎉 Spieler {player} gewinnt!")
                    return
                turn += 1
                moves += 1
            else:
                print("❌ Feld schon besetzt, erneut wählen.")
        except (ValueError, IndexError):
            print("❌ Ungültige Eingabe. Bitte 0, 1 oder 2 eingeben.")
    print("Unentschieden!")

if __name__ == "__main__":
    tic_tac_toe()
