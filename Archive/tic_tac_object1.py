#Playing tic_tac_machine but objecto orientated


# Three types of player:
# random = 1
# taught = 2
# Machine (Machine 1 will use random & Machine 2 will use taught to teach itself) = 3
#
#
# player_1 = random
# player_2 = taught
# num_repetitions = x


class Board():
    def __init__ (self, size = 3, board_dictionary):
        self.size = size
        self.board_dictionary = {1:".", 2:".", 3:".", 4:".", 5: ".", 6:".", 7:".", 8:".", 9:".", }

    def update_board(user_move, player_piece):
        self.board_dictionary[int(user_move)] = player_piece

    def is_win():
        is_win = False
        count = 1
        while count <= 7:
            if board_dict[count] == board_dict[count + 1] == board_dict[count + 2] != '.':
                is_win = True
            count += 3
        count = 1

        while count <= 3:
            if board_dict[count] == board_dict[count + 3] == board_dict[count + 6] != '.':
                is_win = True
            count += 1
        count = 1

        if board_dict[1] == board_dict[5] == board_dict[9] != '.':
            is_win = True
        if board_dict[3] == board_dict[5] == board_dict[7] != '.':
            is_win = True

        return is_win

class Player():
    def __init__ (self, player_id, player_piece):
        self.player_id = player_id
        self.player_piece = player_piece

    def make_move():
        aa
        return player_move

class Game_Library():
    # Play a lot of games
    def __init__(self, Player_1, Player_2, Game_Library):
        self.Game_Library = Game_Library

    def Play_Game():
            player_counter = 0
            turn_counter = 0

            board = Board.make_board()

            player_1 = Player("player_1", 'x')
            player_2 = Player("player_2", 'o')
            player_list = [player_1, player_2]

            while Board.is_win is False:
                player_move = player_list[player_counter].make_move()
                player_piece = player_list[player_counter].player_piece
                Board.update_board(player_move, )
                player_counter += 1
                turn_counter += 1

            return Board

    def make_library():
        games_dictionary_library = {}
        game_id = 0

        while game_id < 1000:
            games_dictionary_library[game_id] = Play_Game()
            game_id += 1

        count_results(games_dictionary_library, game_id)
        return games_dictionary_library

        player_1_count = 0
        player_2_count = 0
        player_draw_count = 0

        for game in game_dictionary:
            if game_dictionary[game][1] == 'player_1':
                player_1_count += 1
            if game_dictionary[game][1] == 'player_2':
                player_2_count += 1
            if game_dictionary[game][1] == 'Null':
                player_draw_count += 1

        win_ratio = player_1_count/game_id

        return

    def print_results(games_dictionary_library):
        print("Player_1 won: " + str(player_1_count) + " times.")
        print("Player_2 won: " + str(player_2_count) + " times.")
        print("Draws happened: " + str(player_draw_count) + " times.")
        print("Win ratio: " + str(round(win_ratio, 2)))


if __name__ == '__main__':

    Game_Library()
