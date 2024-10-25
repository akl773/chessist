
# Random Chess Move API

This is a Flask-based backend for a chess game where the backend selects a random chess piece that the user must move. The project uses the `python-chess` library to handle chessboard logic and the `Stockfish` chess engine to assist with legal move validation.

## Features

- Returns a random chess piece that has at least one legal move.
- Does **not** move the piece on the board—only selects a piece that the user must move.
- Uses `python-chess` for board state management and move validation.
- Supports multiple chess games simultaneously.
- Stockfish integration for future enhancements.

## Prerequisites

1. **Python 3.7+**
2. **pip** for installing dependencies
3. **Stockfish** chess engine installed on your system. You can download it from [here](https://stockfishchess.org/download/).

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/chess-backend.git
   cd chess-backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Download and extract the **Stockfish** engine to a location on your system.

4. Create a `.env` file in the root directory of your project and specify the path to your Stockfish executable:

   ```
   STOCKFISH_PATH=/path/to/stockfish/stockfish-macos-m1-apple-silicon  # Update with your path
   ```

## Running the Server

To run the Flask development server:

```bash
python app.py
```

This will start the server on `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Start a New Game

**Endpoint**: `/start-game`  
**Method**: `POST`

Starts a new chess game and returns the game ID.

**Example Response**:

```json
{
  "message": "Game 1 started",
  "game_id": 1
}
```

### 2. Get a Random Piece

**Endpoint**: `/get-piece/<game_id>`  
**Method**: `GET`

Returns a random piece that the player must move. The piece is guaranteed to have at least one legal move.

**Example Response**:

```json
{
  "game_id": 1,
  "random_piece": "Rook"
}
```

## Directory Structure

```
chess-backend/
│
├── app.py               # Flask app to expose the API endpoints
├── game.py              # Chess game logic and state management
├── .env                 # Environment variables (Stockfish path)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Environment Variables

- **STOCKFISH_PATH**: The full path to your Stockfish executable.

Example for `.env` file:

```
STOCKFISH_PATH=/Users/yourusername/stockfish/stockfish-macos-m1-apple-silicon
```

## Dependencies

- `Flask`: For the web framework.
- `python-chess`: For chess logic and move validation.
- `python-dotenv`: For loading environment variables from the `.env` file.
- `stockfish`: For integrating the Stockfish chess engine.

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## How to Use

1. Start the server.
2. Use the `/start-game` endpoint to create a new game.
3. Use the `/get-piece/<game_id>` endpoint to retrieve the randomly selected piece for that turn.
4. You can integrate this backend with a chess frontend or CLI where the user makes a move based on the piece returned by the backend.

## License

This project is licensed under the MIT License.
