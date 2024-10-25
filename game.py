import os
import random
import chess
from stockfish import Stockfish
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class ChessGame:
    def __init__(self, game_id):
        self.game_id = game_id
        self.board = chess.Board()  # Initialize the board using python-chess
        self.selected_piece = None

        # Get the Stockfish path from environment variable
        stockfish_path = os.getenv("STOCKFISH_PATH")
        if stockfish_path is None:
            raise EnvironmentError("STOCKFISH_PATH not set in environment variables")

        # Initialize Stockfish engine
        self.stockfish = Stockfish(stockfish_path)
        self.stockfish.set_depth(15)  # Set Stockfish calculation depth

        self.pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']  # Chess pieces

    def get_board_state(self):
        # Return the board state in FEN (Forsyth–Edwards Notation)
        return self.board.fen()

    def get_random_piece(self):
        # Choose a random piece type
        self.selected_piece = random.choice(self.pieces)
        return self.selected_piece

    def make_move(self, move):
        # Get all legal moves
        legal_moves = list(self.board.legal_moves)

        # Check if the move is legal
        move_obj = chess.Move.from_uci(move)
        if move_obj not in legal_moves:
            return False, "Invalid move"

        # Ensure that the move involves the randomly selected piece
        from_square = move_obj.from_square
        piece = self.board.piece_at(from_square)

        if not piece:
            return False, "No piece at the source square"

        if not self.piece_matches_selected(piece):
            return False, f"You must move a {self.selected_piece}"

        # Make the move
        self.board.push(move_obj)
        return True, "Move successful"

    def piece_matches_selected(self, piece):
        """Ensure that the piece matches the selected piece type"""
        piece_type = piece.piece_type
        piece_type_map = {
            chess.PAWN: 'pawn',
            chess.ROOK: 'rook',
            chess.KNIGHT: 'knight',
            chess.BISHOP: 'bishop',
            chess.QUEEN: 'queen',
            chess.KING: 'king',
        }

        return piece_type_map.get(piece_type) == self.selected_piece
