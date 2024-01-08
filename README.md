# Tic-Tac-Toe: AI vs Human

This Python project implements a Tic-Tac-Toe game where you can challenge an AI opponent using the Minimax algorithm. The inspiration for this project comes from Freecodecamp, and it serves as a great opportunity to explore artificial intelligence in the context of a classic game.

## Introduction

Tic-Tac-Toe is a two-player game where each player takes turns marking a cell in a 3x3 grid with their symbol (X or O). The goal is to get three of your symbols in a row, either horizontally, vertically, or diagonally. This project extends the traditional gameplay by allowing you to challenge an AI opponent, which utilizes the Minimax algorithm to make strategic decisions.

## Features

- Play against an AI opponent using the Minimax algorithm.
- Simple and intuitive user interface.
- Automatic detection of game outcomes (win, lose, draw).
- End-to-end Python implementation.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/tic-tac-toe-ai.git
2. Navigate to the project directory in your terminal:

3. Run the game:

   ```bash
   python tic_tac_toe.py

## Gameplay

- You play as "X," and the AI opponent plays as "O."
- Input your move by specifying the row and column (e.g., "1,2" for the first row and second column).
- The game continues until there is a winner, a draw, or you decide to exit.

## Algorithm

- The AI opponent utilizes the Minimax algorithm, a decision-making algorithm commonly used in two-player turn-based games.
- It explores all possible moves, evaluates them based on the current game state, and chooses the move that leads to the best outcome. 
- In the context of Tic-Tac-Toe, this means the AI strives for the optimal strategy to either win or force a draw.

## Acknowledgements

This project draws inspiration from Freecodecamp's educational content, providing a practical implementation of AI in the context of a classic game. 
