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
        
def player_turn(game_baord, turn):            
    player_one_vert = input("Turn " + str(turn) + ": Player 1, Which column would you like to place? (1-3)")
    player_one_vert = data_check(player_one_vert, "Player 1, Incorect input, which column? (1-3)")

    player_one_hort = input("Turn " + str(turn) + ": Which row would you like to place? (1-3)")
    player_one_hort = data_check(player_one_hort, "Player 1, Incorect input, which row? (1-3)")

    player_one_moves = verify_place(player_one_vert, player_one_hort, game_board, "Player 1, Incorect input, which column? (1-3)", "Player 1, Incorect input, which row? (1-3)")

    game_baord[player_one_moves[0] - 1][player_one_moves[1] - 1] = ("X")
    print_gameboard(game_baord)

    player_two_vert = input("Turn " + str(turn) + ": Player 2, Which column would you like to place? (1-3)")
    player_two_vert = data_check(player_two_vert, "Player 2, Incorect input, which column? (1-3)")

    player_two_hort = input("Turn " + str(turn) + ": Player 2, Which row would you like to place? (1-3)")
    player_two_hort = data_check(player_two_hort, "Player 2, Incorect input, which row? (1-3)")

    player_two_moves = verify_place(player_two_vert, player_two_hort, game_board, "Player 2, Incorect input, which column? (1-3)", "Player 2, Incorect input, which row? (1-3)")

    game_baord[player_two_moves[0] - 1][player_two_moves[1] - 1] = ("O")
    print_gameboard(game_baord)


while game == False:
    player_turn(game_board, turn)
    turn += 1
