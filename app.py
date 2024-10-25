from flask import Flask, jsonify, request
from game import ChessGame

app = Flask(__name__)
games = {}  # Dictionary to track multiple games


@app.route('/start-game', methods=['POST'])
def start_game():
    game_id = len(games) + 1
    game = ChessGame(game_id)
    games[game_id] = game
    return jsonify({"message": f"Game {game_id} started", "game_id": game_id})


@app.route('/get-piece/<int:game_id>', methods=['GET'])
def get_random_piece(game_id):
    if game_id not in games:
        return jsonify({"error": "Game not found"}), 404

    game = games[game_id]
    random_piece = game.get_random_piece()
    return jsonify({
        "game_id": game_id,
        "random_piece": random_piece
    })


@app.route('/move/<int:game_id>', methods=['POST'])
def make_move(game_id):
    if game_id not in games:
        return jsonify({"error": "Game not found"}), 404

    game = games[game_id]
    move = request.json.get('move')  # Player's move in UCI format (e.g., "e2e4")

    if not move:
        return jsonify({"error": "Move not provided"}), 400

    result, message = game.make_move(move)

    if result:
        return jsonify({
            "game_id": game_id,
            "move": move,
            "board": game.get_board_state()  # Return current board state in FEN notation
        })
    else:
        return jsonify({"error": message}), 400


if __name__ == '__main__':
    app.run(debug=True)
