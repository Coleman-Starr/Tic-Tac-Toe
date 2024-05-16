game_board = [
    ["-","-","-"], 
    ["-","-","-"], 
    ["-","-","-"]]
game = False
turn = 1

def data_check(data, message):
    works = False
    while works == False:
        try:
            int(data)
        except ValueError:
            data = input(message)
        else:
            if int(data) > 3 or int(data) < 1:
                data = input(message)
            else:
                return int(data)
            
def verify_place(vert, hort, game_board, message, message2):
    while game_board[vert-1][hort-1] == "X" or game_board[vert-1][hort-1] == "O":
        print("Space Already Taken!")
        vert = input(message)
        vert = data_check(vert, message)
        hort = input(message)
        hort = data_check(hort, message2)
    return [vert, hort]

def print_gameboard(game_board):
    for line in game_board: 
        print(line)

def is_board_full(game_board):
    for row in game_board:
        for line in row:
            if line == "-":
                return False
    return True

def check_winner(game_board, turn):
    is_full = is_board_full(game_board)
    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("Player 1 Wins!")
        return True
    elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("Player 2 Wins!")
        return True
    elif game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("Player 1 Wins!")
        return True
    elif game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("Player 2 Wins!")
        return True
    elif is_full == False:
        for row in game_board:
            if row == ["X","X","X"]:
                print("Player 1 Wins!")
                return True
            elif row == ["O","O","O"]:
                print("Player 2 Wins!")
                return True
            else:
                return False
    elif is_full == True:
        print("TIE!")
        return True
            
def player_turn(game_baord, turn, player, symbol):            
    player_vert = input("Turn " + str(turn) + ": Player " + str(player) + ", Which column would you like to place? (1-3)")
    player_vert = data_check(player_vert, ": Player " + str(player) + ", Incorect input, which column? (1-3)")

    player_hort = input("Turn " + str(turn) + ": Player " + str(player) + ", Which row would you like to place? (1-3)")
    player_hort = data_check(player_hort, "Player " + str(player) + ", Incorect input, which row? (1-3)")

    player_moves = verify_place(player_vert, player_hort, game_board, "Player " + str(player) + ", Incorect input, which column? (1-3)", "Player " + str(player) + ", Incorect input, which row? (1-3)")

    game_baord[player_moves[0] - 1][player_moves[1] - 1] = (symbol)
    print_gameboard(game_baord)
    return check_winner(game_board, turn)

while game == False:
    game = player_turn(game_board, turn, 1, "X")
    if game == False:
        game = player_turn(game_board, turn, 2, "O")
        turn += 1
