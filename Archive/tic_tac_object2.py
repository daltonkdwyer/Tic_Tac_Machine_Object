import random
from statistics import mode
import csv
import machine_move

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

    def print_board_dict(self, board_dict):
        self.board_dict = board_dict
        i = 1
        while i < 10:
            print(board_dict[i], board_dict[i + 1], board_dict[i + 2])
            i += 3
        print('\n')

class Player():
    def __init__(self, player_piece):
        self.player_piece = player_piece

    def make_move_random(self, board_dict, move_list):
        user_move = random.randint(1, 9)
        while board_dict[int(user_move)] != ".":
            user_move = random.randint(1, 9)
        return user_move

    def make_move_machine(self, board_dict, move_list):
        # COMMENTING OUT THE BELOW SECTION WHILE DOING THE SAVE-TO-FILE UPDATE
        # GL = Game_Library()
        # GL.make_library()
        # GL.count_results()
        # GDL = GL.games_dictionary_library

        temp_games_list = []
        temp_moves_list = []
        user_move = random.randint(1, 9)
        while board_dict[int(user_move)] != ".":
            user_move = random.randint(1, 9)

        print("A machine move is being made!")
        print("Move list: " + str(move_list))
        # TAKES OUT ALL THE GAMES PLAYER TWO WINS:
        # if len(move_list) > 2:
        #     print("Similar games in library: ")
        for game in GDL:
            if GDL[game][1] == 'Player_2':
                if move_list[:len(move_list)] == GDL[game][0][:len(move_list)]:
                    # NOTE THE BELOW MAKES A LIST OF EACH GAME, NOT INDIVIDUAL MOVES
                    temp_games_list.append(GDL[game][0])
                    # print(GDL[game][0])
        # TAKES OUT THE MOST COMMON MOVE FROM THE GAMES PLAYER TWO WINS:

        # print("Length move list: " + str(len(move_list)))

        for game in temp_games_list:
            temp_moves_list.append(game[len(move_list)])

        print("Temp moves list: ")
        print(temp_moves_list)

        if len(temp_moves_list) > 1:
            user_move = mode(temp_moves_list)
            print("Suggested Machine Move: " + str(user_move))


        # while board_dict[int(user_move)] != ".":
        #     user_move = random.randint(1, 9)
        # print("Actual User Move: " + str(user_move))

        return user_move

    def make_move_programed(self):
        aa

class Game():
    def __init__(self):
        self.move_list = []
        self.Player_1 = Player('x')
        self.Player_2 = Player('o')
        self.Game_Board = Board()
        self.winner_id = ''

    def play_game(self):
        turn_counter = 0
        while self.Game_Board.is_win(self.Game_Board.board_dict) is False and turn_counter < 9:
            if (turn_counter % 2) == 0:
                user_move = self.Player_1.make_move_random(self.Game_Board.board_dict, self.move_list)
                self.Game_Board.update_board(user_move, self.Player_1.player_piece)
                self.move_list.append(user_move)
            if (turn_counter % 2) == 1:
                user_move = self.Player_2.make_move_random(self.Game_Board.board_dict, self.move_list)
                self.Game_Board.update_board(user_move, self.Player_2.player_piece)
                self.move_list.append(user_move)
            turn_counter +=1

        if self.Game_Board.is_win(self.Game_Board.board_dict) is False:
            self.winner_id = 'Null'
        elif (turn_counter % 2) == 0:
            self.winner_id = 'Player_2'
        elif (turn_counter % 2) == 1:
            self.winner_id = 'Player_1'

        # UNHIGHLIGHT THE BELOW LINE TO PRINT THE BOARD FROM EACH GAME
        # self.Game_Board.print_board_dict(self.Game_Board.board_dict)
        # print(self.move_list)

    #THIS IS ONLY HERE TO MACHINE PLAY WITHOUT HAVING TO DO THE SAVE TO FILE THING
    def play_game1(self):
        turn_counter = 0
        while self.Game_Board.is_win(self.Game_Board.board_dict) is False and turn_counter < 9:
            if (turn_counter % 2) == 0:
                user_move = self.Player_1.make_move_random(self.Game_Board.board_dict, self.move_list)
                self.Game_Board.update_board(user_move, self.Player_1.player_piece)
                self.move_list.append(user_move)
            if (turn_counter % 2) == 1:
                user_move = self.Player_2.make_move_machine(self.Game_Board.board_dict, self.move_list)
                self.Game_Board.update_board(user_move, self.Player_2.player_piece)
                self.move_list.append(user_move)
            turn_counter +=1

        if self.Game_Board.is_win(self.Game_Board.board_dict) is False:
            self.winner_id = 'Null'
        elif (turn_counter % 2) == 0:
            self.winner_id = 'Player_2'
        elif (turn_counter % 2) == 1:
            self.winner_id = 'Player_1'

        # UNHIGHLIGHT THE BELOW LINE TO PRINT THE BOARD FROM EACH GAME
        self.Game_Board.print_board_dict(self.Game_Board.board_dict)
        print(self.move_list)


class Game_Library():
    def __init__(self):
        self.games_dictionary_library = {}

    def make_library(self):
        GDL_File = open('GDL_File.csv', 'w')
        writer = csv.writer(GDL_File)

        self.game_id = 0
        while self.game_id < 100000:
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

        # UNHIGHLIGHT THE BELOW TO PRINT EACH LINE IN THE GAMES DICTIONARY
        for game in self.games_dictionary_library:
            print(self.games_dictionary_library[game])

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


# THIS IS HOW TO PLAY A SINGLE GAME
# game1 = Game()
# game1.play_game()

# THIS IS HOW TO PLAY A MACHINE GAME
# game1 = Game()
# game1.play_game1()

# THIS IS HOW TO MAKE A LIBRARY
game1 = Game_Library()
game1.make_library()
game1.count_results()
















# Game_1 = Game()
# # print(Game.play_game())
#
# print(Game_1.play_game())
# Game.play_game('')
# Game.check_winner('')
# Game.print_result('')

#
# def play_game():
#     Player_1 = Player('x')
#     Player_2 = Player('o')
#     Board_game = Board()
#     winner_id = ''
#
#     turn_counter = 0
#
#     while Board_game.is_win(Board_game.board_dict) is False and turn_counter < 9:
#         if (turn_counter % 2) == 0:
#             user_move = Player_1.make_move_random(Board_game.board_dict, Player_1.player_piece)
#             Board_game.update_board(user_move, Player_1.player_piece)
#         if (turn_counter % 2) == 1:
#             user_move = Player_2.make_move_random(Board_game.board_dict, Player_2.player_piece)
#             Board_game.update_board(user_move, Player_2.player_piece)
#         turn_counter +=1
#
#     if Board_game.is_win(Board_game.board_dict) is False:
#         winner_id = 'Null'
#     elif (turn_counter % 2) == 0:
#         winner_id = 'Player_2'
#     elif (turn_counter % 2) == 1:
#         winner_id = 'Player_1'
#
#
#     Board_game.print_board_dict(Board_game.board_dict)
#     print(Board_game.move_list, winner_id)
#
#     return Board_game.move_list, winner_id
#
# play_game()
#
# # print(game[0].board_dict)
