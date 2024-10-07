# Blackjack Game

This is a simple command-line Blackjack game written in Python. The user plays against the computer to try and get as close to 21 as possible without going over. The game handles card dealing, score calculation, and comparing the user's hand with the computer's to determine the winner.

## How to Play

- You and the computer start with two cards each.
- You can choose to take more cards ("Hit") or stick with your current hand ("Stand").
- The goal is to have a score as close to 21 as possible without exceeding it.
- If either you or the computer has exactly 21 with two cards, it’s a **Blackjack**!
- The game continues until either you or the computer goes over 21 or both players decide to stand.

## Rules
- The game uses a simplified deck where cards are represented as numbers:
  - Number cards 2-10 have their face value.
  - Face cards (Jack, Queen, King) are all worth 10.
  - Aces are worth 11 unless that would cause a score over 21, in which case they count as 1.
- The game continues until the player or computer either reaches 21 or goes bust (over 21).
- You win by getting a higher score than the computer without going over 21.

## How to Run

1. Make sure you have Python installed (version 3.x).
2. Copy the code into a file, for example, `blackjack.py`.
3. Open your terminal or command prompt.
4. Navigate to the folder containing `blackjack.py`.
5. Run the following command:
   ```bash
   python blackjack.py

## Functions 
* deal_card(): Returns a random card from the deck.
* calculate_score(cards): Calculates the current score of a hand.
* compare(u_score, c_score): Compares the user's score with the computer's and determines the result.
* play_game(): Manages the entire game flow.