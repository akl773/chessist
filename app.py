from flask import Flask, jsonify
from game import ChessGame

app = Flask(__name__)
games = {}  # Dictionary to track multiple games


@app.route('/start-game', methods=['POST'])
def start_game():
    game_id = len(games) + 1
    game = ChessGame(game_id)
    games[game_id] = game
    return jsonify({"message": f"Game {game_id} started", "game_id": game_id})


@app.route('/move/<int:game_id>', methods=['POST'])
def make_move(game_id):
    if game_id not in games:
        return jsonify({"error": "Game not found"}), 404

    game = games[game_id]
    random_piece, move = game.make_random_move()
    return jsonify({
        "game_id": game_id,
        "random_piece": random_piece,
        "move": move,
        "board": game.get_board_state()  # Return current board state in FEN notation
    })


if __name__ == '__main__':
    app.run(debug=True)
