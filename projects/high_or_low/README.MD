# Higher or Lower: Instagram Followers Edition

This is a command-line game where you guess which of two famous accounts has more Instagram followers. The game pulls data from a predefined dataset and continues until the player guesses incorrectly. Every correct guess increases your score!

## How to Play

1. The game will display two accounts (A and B), each with a name, description, and country.
2. You will have to guess which account has more followers by typing 'A' or 'B'.
3. If you're correct, your score increases and the game continues.
4. The game ends when you guess incorrectly, and your final score is displayed.

## How to Run

1. Ensure that you have Python installed (version 3.x).
2. Copy the code into a file, for example, `higher_lower.py`.
3. Create two additional files:
   - `game_data.py`: Contains the dataset of accounts.
   - `art.py`: Contains the ASCII art for the logo and the "vs" sign.
   
   Example structure:
   ```plaintext
   - higher_lower.py
   - game_data.py
   - art.py

* In game_data.py, include a list of dictionaries, where each dictionary contains the following keys for an account:

- "name": The name of the account holder.
- "follower_count": Number of followers (in millions).
- "description": A brief description of the account.
- "country": The account holder's countr

* In art.py, include two string variables:

- logo: Contains the ASCII logo for the game.
- vs: Contains the ASCII art for the 'vs' symbol.

## Functions
- format_data(account): Formats the account details (name, description, and country) for display.
- check_answer(user_guess, a_followers, b_followers): Compares the follower counts and checks if the user's guess is correct.
- The game continues in a loop until the user guesses incorrectly.