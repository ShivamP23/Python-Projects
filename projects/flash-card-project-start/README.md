# Flashy - A Flashcard Learning App

Flashy is a simple flashcard app that helps you learn French vocabulary through an interactive and visual experience. The app randomly displays French words and their English translations, making it fun and easy to expand your vocabulary. Words you learn are saved so you can focus on new ones!

## Features
- Randomly displays French words with their translations.
- Automatically flips cards after 3 seconds to show the translation.
- Removes words you already know from your learning list.
- Saves your progress for future sessions.

## How It Works
1. A French word is displayed on the flashcard.
2. After 3 seconds, the card flips to reveal the English translation.
3. Use the check (✅) button if you know the word or the cross (❌) button to skip it.
4. Known words are removed from the learning list and saved to a file.

4. Place your dataset files in the `data` folder and images in the `images` folder. Make sure the following files are present:
   - `data/french_words.csv` (list of French-English word pairs)
   - `images/card_front.png` (image for front side of the card)
   - `images/card_back.png` (image for back side of the card)
   - `images/wrong.png` (image for cross button)
   - `images/right.png` (image for check button)

   
## File Structure
- `main.py`: Main program file.
- `data/french_words.csv`: Initial vocabulary file.
- `data/words_to_learn.csv`: File that tracks words you haven’t learned yet.
- `images/`: Folder containing card images and button icons.

## How to Add Your Own Words
1. Replace or edit the `french_words.csv` file in the `data` folder with your own French-English pairs.
2. Ensure the CSV file has two columns: `French` and `English`.

## Requirements
- Python 3.7+
- Pandas library
- Tkinter (comes pre-installed with Python)

## Future Improvements
- Add more languages.
- Include audio pronunciation for each word.
- Track user statistics like total words learned.

## License
This project is open-source and free to use. Feel free to modify and improve it as you like!

---
Happy learning! 😊
