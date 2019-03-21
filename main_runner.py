import logging
import os
import numpy as np
import keras
import sys


class Board:
    POS_TO_LETTER = 'abcdefghjklmnop'
    LETTER_TO_POS = {letter: pos for pos, letter in enumerate(POS_TO_LETTER)}

    @staticmethod
    def to_move(pos):
        return Board.POS_TO_LETTER[pos[1]] + str(pos[0] + 1)

    @staticmethod
    def to_pos(move):
        return int(move[1:]) - 1, Board.LETTER_TO_POS[move[0]]

    @staticmethod
    def is_empty(t):
        for i in range(15):
            for j in range(15):
                if t[i][j][0] != 0 or t[i][j][1] != 0:
                    return False
        return True

    @staticmethod
    def create_empty_table(color):
        x = np.zeros((15, 15, 3))
        for i in range(15):
            for j in range(15):
                x[i][j][2] = color
        return x

    @staticmethod
    def wait_for_game_update():
        if not sys.stdin.closed:
            game_dumps = sys.stdin.readline()
            if game_dumps:
                return game_dumps
        return None

    @staticmethod
    def create_table(moves: str):
        moves = moves.replace('\n', '')
        moves = moves.split(' ') if moves != '' else []
        me = -1 if len(moves) % 2 == 0 else 1
        table = Board.create_empty_table(me)
        for ind, move in enumerate(moves):
            x, y = Board.to_pos(move)
            if ind % 2 == 0:
                table[x][y][0] = -1
            else:
                table[x][y][1] = 1
        return table

    @staticmethod
    def set_move(move):
        if sys.stdout.closed:
            return False
        sys.stdout.write(move + '\n')
        sys.stdout.flush()
        return True

    @staticmethod
    def has_winner(board):
        directions = ((1, 0), (0, 1), (1, 1), (-1, 1))
        for i in range(15):
            for j in range(15):
                if Board.get(board, i, j, 0) == 0:
                    continue
                for dir_i, dir_j in directions:
                    equals = True
                    for t in range(5):
                        if Board.get(board, i + t * dir_i, j + t * dir_j, 0) != Board.get(board, i, j, 0):
                            equals = False
                    if equals:
                        return Board.get(board, i, j, 0)
        for i in range(15):
            for j in range(15):
                if Board.get(board, i, j, 1) == 0:
                    continue
                for dir_i, dir_j in directions:
                    equals = True
                    for t in range(5):
                        if Board.get(board, i + t * dir_i, j + t * dir_j, 1) != Board.get(board, i, j, 1):
                            equals = False
                    if equals:
                        return Board.get(board, i, j, 1)
        return 0  # draw

    @staticmethod
    def get(board, x, y, z):
        if 0 <= x < 15 and 0 <= y < 15:
            return board[x][y][z]
        return 0


class Predictor:
    @staticmethod
    def choose_move(model_black, model_white, board):
        if Board.is_empty(board):
            return 7, 7

        res = Predictor.can_win_by_1_move(board, color=board[0][0][2])
        if res:
            return res[0], res[1]

        if board[0][0][2] == -1:
            res = model_black.predict(np.array((board,)))[0]
        else:
            res = model_white.predict(np.array((board,)))[0]
        while True:
            # q = []
            # for i, d in enumerate(res):
            #     q.append((d, i))
            # print(sorted(q, reverse=True))
            a = np.argmax(res)
            x = a // 15
            y = a % 15
            if board[x][y][0] != 0 or board[x][y][1] != 0:
                res[x * 15 + y] = -100000
                continue
            return x, y

    @staticmethod
    def can_win_by_1_move(board, color):
        for i in range(15):
            for j in range(15):
                if board[i][j][0] == 0 and board[i][j][1] == 0:
                    if color == -1:
                        board[i][j][0] = -1
                    else:
                        board[i][j][1] = 1
                    if Board.has_winner(board):
                        return i, j
                    board[i][j][0] = 0
                    board[i][j][1] = 0
        return None


def main():
    pid = os.getpid()
    log_format = f'{pid}:%(levelname)s:%(asctime)s: %(message)s'

    logging.basicConfig(format=log_format, level=logging.DEBUG)
    logging.debug('Start dummy backend...')

    model_black = keras.models.load_model('../model/myModelBlack.h5')
    model_white = keras.models.load_model('../model/myModelWhite.h5')

    logging.debug('')

    try:
        while True:
            logging.debug("Wait for game update...")
            game = Board.wait_for_game_update()

            if not game:
                logging.debug("Game is over!")
                return
            game = Board.create_table(game)
            result = Predictor.choose_move(model_black, model_white, game)
            move = Board.to_move(result)

            if not Board.set_move(move):
                logging.error("Impossible set move!")
                return

            logging.debug('Move: %s', move)

    except:
        logging.error('Error!', exc_info=True, stack_info=True)


if __name__ == "__main__":
    main()
