import random
import chess
from stockfish import Stockfish


class ChessGame:
    def __init__(self, game_id):
        self.game_id = game_id
        self.board = chess.Board()  # Initialize the board using python-chess

        # Path to your Stockfish engine executable
        self.stockfish = Stockfish("/path/to/stockfish")
        self.stockfish.set_depth(15)  # Set Stockfish calculation depth

        self.pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']  # Chess pieces

    def get_board_state(self):
        return self.board.fen()

    def make_random_move(self):
        # Choose a random piece type
        piece = random.choice(self.pieces)

        # Get all legal moves
        legal_moves = list(self.board.legal_moves)

        if legal_moves:
            # Set the current board state for Stockfish
            self.stockfish.set_fen_position(self.board.fen())

            # Let Stockfish suggest the best move
            best_move = self.stockfish.get_best_move()

            # Push the move onto the board (using python-chess)
            move = chess.Move.from_uci(best_move)
            self.board.push(move)

            return piece, best_move
        else:
            return piece, None  # No available legal moves
