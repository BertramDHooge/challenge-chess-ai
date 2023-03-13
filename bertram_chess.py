import random
import chess
from tensorflow import keras

model_early = keras.model.load_model("early")
model_late = keras.model.load_model("late")

with open('tokenizer_early.pickle', 'rb') as handle:
    tokenizer_early = pickle.load(handle)

with open('tokenizer_late.pickle', 'rb') as handle:
    tokenizer_late = pickle.load(handle)

def pick_a_move(board):
    legal_moves = []
    legal_moves_tokenized =[]

    for move in board.legal_moves:
        if board.piece_at(move.from_square).__str__() != "p" and board.piece_at(move.from_square).__str__() != "P":
            legal_moves.append(board.piece_at(move.from_square).__str__() + chess.square_name(move.to_square).__str__())
        elif board.piece_at(move.to_square) is not None:
            legal_moves.append(chess.FILE_NAMES[chess.square_file(move.from_square)] + chess.square_name(move.to_square).__str__())
        else:
            legal_moves.append(chess.square_name(move.to_square))

    played_moves = []
    predictable = []

    for move in board.move_stack:
        if board.piece_at(move.from_square).__str__() != "p" and board.piece_at(move.from_square).__str__() != "P":
            played_moves.append(board.piece_at(move.from_square).__str__() + chess.square_name(move.to_square).__str__())
        elif board.piece_at(move.to_square) is not None:
            played_moves.append(chess.FILE_NAMES[chess.square_file(move.from_square)] + chess.square_name(move.to_square).__str__())
        else:
            played_moves.append(chess.square_name(move.to_square))

    predicted = {}
    tokendict={}
    
    if len(played_moves) > 9:
        predictable = tokenizer_late(played_moves[-9:])
        predicted = model_late.predict([predictable])
        for index in range(len(predicted[0])):
            tokendict[tokenizer_late.sequences_to_texts([[index]])[0]] = predicted[0][index]
    elif len(played_moves) < 9:
        for _ in range(9-len(played_moves)):
            predictable.append(0)
        predictable += tokenizer_early(played_moves)
        predicted = model_late.predict([predictable])
        for index in range(len(predicted[0])):
            tokendict[tokenizer_early.sequences_to_texts([[index]])[0]] = predicted[0][index]
    else:
        predictable += tokenizer_early(played_moves)
        predicted = model_late.predict([predictable])
        for index in range(len(predicted[0])):
            tokendict[tokenizer_early.sequences_to_texts([[index]])[0]] = predicted[0][index]

    




