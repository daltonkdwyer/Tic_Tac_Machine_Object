import random
from statistics import mode
import csv
import machine_move
import stockfish_move

class Board():
    def __init__(self):
        self.board_dict = {1:".", 2:".", 3:".", 4:".", 5: ".", 6:".", 7:".", 8:".", 9:"."}
        self.move_list = []

    def update_board(self, user_move, player_piece):
        self.move_list.append(user_move)
        self.board_dict[int(user_move)] = player_piece

    def is_win(self, board_dict):
        self.board_dict = board_dict
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

    def print_board_dict(self):
        i = 1
        while i < 10:
            print(self.board_dict[i], self.board_dict[i + 1], self.board_dict[i + 2])
            i += 3
        # print('\n')

class Player():
    def __init__(self, player_piece, player_type):
        self.player_piece = player_piece
        self.player_type = player_type

    def make_move(self, move_list):
        if self.player_type == 'random':
            user_move = machine_move.make_move_random('', move_list)
            return user_move
        elif self.player_type == 'machine':
            user_move = machine_move.make_move_machine('', move_list)
            return user_move
        elif self.player_type == 'stockfish':
            user_move = machine_move.make_move_stockfish(board_dict, move_list)
            return user_move
        elif self.player_type == 'human':
            user_move = machine_move.make_move_human('', move_list)

class Game():
    def __init__(self, player_1_type, player_2_type):
        self.Game_Board = Board()
        self.Player_1 = Player('x', player_1_type)
        self.Player_2 = Player('o', player_2_type)
        self.move_list = []
        self.winner_id = ''
        self.move_list = self.Game_Board.move_list

    def play_game(self):
        turn_counter = 0

        while self.Game_Board.is_win(self.Game_Board.board_dict) is False and turn_counter < 9:
            if (turn_counter % 2) == 0:
                user_move = self.Player_1.make_move(self.Game_Board.move_list)
                self.Game_Board.update_board(user_move, self.Player_1.player_piece)
            if (turn_counter % 2) == 1:
                user_move = self.Player_2.make_move(self.Game_Board.move_list)
                self.Game_Board.update_board(user_move, self.Player_2.player_piece)
            turn_counter +=1

        if self.Game_Board.is_win(self.Game_Board.board_dict) is False:
            self.winner_id = 'Null'
        elif (turn_counter % 2) == 0:
            self.winner_id = 'Player_2'
        elif (turn_counter % 2) == 1:
            self.winner_id = 'Player_1'

        # UNHIGHLIGHT THE BELOW LINE TO PRINT THE BOARD FROM EACH GAME
        # self.Game_Board.print_board_dict(self.Game_Board.board_dict)
        # print(self.Game_Board.move_list)


class Game_Library():
    def __init__(self):
        self.games_dictionary_library = {}

    def make_library(self):
        self.game_id = 0
        while self.game_id < 100:
            list_for_file = []
            Game_Temp = Game()
            Game_Temp.play_game()
            self.games_dictionary_library[self.game_id] = Game_Temp.move_list, Game_Temp.winner_id

            # SWITCH THE BELOW THREE LINES AROUND TO PRINT THE winner_id BEFORE THE move_list
            for move in Game_Temp.move_list:
                list_for_file.append(int(move))
            list_for_file.append(Game_Temp.winner_id)

            self.game_id += 1

        # UNHIGHLIGHT THE BELOW TO PRINT EACH LINE IN THE GAMES DICTIONARY
        # for game in self.games_dictionary_library:
        #     print(self.games_dictionary_library[game])

    def make_file(self):
        GDL_File = open('GDL_File_Machine.csv', 'w')
        writer = csv.writer(GDL_File)

        self.game_id = 0
        while self.game_id < 100:
            list_for_file = []
            Game_Temp = Game()
            Game_Temp.play_game()
            self.games_dictionary_library[self.game_id] = Game_Temp.move_list, Game_Temp.winner_id

            # SWITCH THE BELOW THREE LINES AROUND TO PRINT THE winner_id BEFORE THE move_list
            for move in Game_Temp.move_list:
                list_for_file.append(int(move))
            list_for_file.append(Game_Temp.winner_id)

            writer.writerow(list_for_file)

            self.game_id += 1

        GDL_File.close()

    def count_results(self):
        player_1_count = 0
        player_2_count = 0
        player_draw_count = 0

        for game in self.games_dictionary_library:
            if self.games_dictionary_library[game][1] == 'Player_1':
                player_1_count += 1
            if self.games_dictionary_library[game][1] == 'Player_2':
                player_2_count += 1
            if self.games_dictionary_library[game][1] == 'Null':
                player_draw_count += 1

        win_ratio = player_1_count/self.game_id

        print("Player_1 won: " + str(player_1_count) + " times.")
        print("Player_2 won: " + str(player_2_count) + " times.")
        print("Draws happened: " + str(player_draw_count) + " times.")
        print("Win ratio: " + str(round(win_ratio, 2)))
