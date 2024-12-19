# Quizzler App

This is a simple quiz app that fetches trivia questions from an API and lets you answer them through a graphical interface.

## How It Works

1. The app fetches 10 true/false trivia questions from the Open Trivia Database.
2. Each question is displayed in the app's GUI.
3. You can answer "True" or "False" by clicking the corresponding button.
4. Your score is updated as you answer questions.
5. When you finish all the questions, your final score is displayed.

## Files in the Project

- **data.py**: Fetches trivia questions from the API.
- **question_model.py**: Defines the `Question` class for storing question data.
- **quiz_brain.py**: Handles the quiz logic, including tracking the current question and checking answers.
- **ui.py**: Builds the GUI using Tkinter and interacts with the quiz logic.
- **main.py**: Sets up the app by creating the question bank and starting the GUI.

## How to Run the App

1. Make sure Python is installed on your computer.
2. Clone this repository or download the files.
3. Install the `requests` library by running:
   ```bash
   pip install requests
   ```
4. Run the `main.py` file:
   ```bash
   python main.py
   ```
5. The app window will open, and you can start answering the quiz questions!

## Features

- Fetches random trivia questions from the Open Trivia Database.
- Simple and user-friendly GUI built with Tkinter.
- Tracks your score and shows the final result at the end.

## Dependencies

- Python 3
- Requests library
- Tkinter (comes pre-installed with Python)

## Notes

- Make sure you have the `images/true.png` and `images/false.png` files in the correct directory for the buttons to work.
- The app might need an active internet connection to fetch trivia questions.

Enjoy the quiz!

