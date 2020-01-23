import tic_tac_object_4
import random


def make_move_stockfish(move_list, player_id, board_dict):
    possible_move_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # HAVE TO TURN THE MOVE LIST INTO STRINGS FOR SOME REASON
    new_move_list = []
    for move in move_list:
        new_move_list.append(str(move))
    move_list = new_move_list

    for move in possible_move_list:
        if move in move_list:
            continue
        if player_id == 'Player_1':
            board_dict[int(move)] = 'x'
        elif player_id == 'Player_2':
            board_dict[int(move)] = 'o'

        temp_Board = tic_tac_object_4.Board()
        temp_Board.board_dict = board_dict
        if temp_Board.is_win(board_dict) == True:
            user_move = move
            return user_move

        board_dict[int(move)] = '.'
    if '1' not in move_list:
        user_move = 1
    else:
        user_move = random.randint(1, 9)
        while board_dict[int(user_move)] != ".":
            user_move = random.randint(1, 9)

    return user_move


    #
    # for move in move_list:
    #     board_dict[int(user_move)] = player_piece
    #     if
