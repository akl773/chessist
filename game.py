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
        self.piece_type_map = {
            chess.PAWN: 'pawn',
            chess.ROOK: 'rook',
            chess.KNIGHT: 'knight',
            chess.BISHOP: 'bishop',
            chess.QUEEN: 'queen',
            chess.KING: 'king',
        }

        # Get the Stockfish path from environment variable
        stockfish_path = os.getenv("STOCKFISH_PATH")
        if stockfish_path is None:
            raise EnvironmentError("STOCKFISH_PATH not set in environment variables")

        # Initialize Stockfish engine
        self.stockfish = Stockfish(stockfish_path)
        self.stockfish.set_depth(15)  # Set Stockfish calculation depth

    def get_board_state(self):
        # Return the board state in FEN (Forsyth–Edwards Notation)
        return self.board.fen()

    def get_random_piece(self):
        # Get all legal moves
        legal_moves = list(self.board.legal_moves)

        if not legal_moves:
            return None, "No legal moves available"

        # Get all pieces that have legal moves
        pieces_with_moves = self._get_pieces_with_legal_moves(legal_moves)
        # Randomly select a piece that has legal moves
        selected_piece = random.choice(list(pieces_with_moves.keys()))

        # Store the selected piece
        self.selected_piece = selected_piece

        return selected_piece

    def _get_pieces_with_legal_moves(self, legal_moves):
        """
        Returns a dictionary mapping piece types to their legal moves.
        Example output:
        {
            'pawn': [Move1, Move2],
            'rook': [Move3]
        }
        """
        pieces_with_moves = {}
        for move in legal_moves:
            piece = self.board.piece_at(move.from_square)
            if piece:
                piece_name = self._get_piece_name(piece)
                if piece_name not in pieces_with_moves:
                    pieces_with_moves[piece_name] = []
                pieces_with_moves[piece_name].append(move)
        return pieces_with_moves

    def _get_piece_name(self, piece):
        """Convert a piece type to a string name"""
        return self.piece_type_map.get(piece.piece_type)
