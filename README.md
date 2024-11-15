# Spy Codebreaker Game

A simple and interactive 4-digit code-breaking game where you have to guess the secret code! After each guess, the game provides feedback on how many digits are correct and in the correct place, as well as how many are correct but in the wrong place.

## Features

- Generate a secret 4-digit code with unique digits.
- User enters guesses, and feedback is provided:
  - Correct digits in the correct place.
  - Correct digits in the wrong place.
- Easy-to-use graphical user interface (GUI) built with Tkinter.

## Requirements

To run this game on your PC, you will need:

- **Python**: The game is written in Python, and you’ll need Python 3.7 or higher installed on your machine.
- **Tkinter**: Tkinter is used for the graphical user interface. It comes pre-installed with Python, so no additional installation is required.
- **Git**: To clone this repository and run the game locally.

## Instructions to Run the Game

### 1. Install Python (if not already installed)

If you don't have Python installed on your system, download and install Python from the official site:

- [Download Python](https://www.python.org/downloads/)

Make sure you select the option to "Add Python to PATH" during the installation.

### 2. Clone the Repository

To clone this repository to your local machine, open a terminal or command prompt and use the following command:

```bash
git clone https://github.com/MostafaTahboub/ai-game.git
```

### 3. Navigate to Game directory 
Once cloned, navigate into the game directory:

```bash
cd spy-codebreaker
```
### 4. Run the Game
Ensure that you're in the directory where the spy_codebreaker_ui.py file is located. To run the game, execute the following command in the terminal:
``` bash
python spy_codebreaker_ui.py

```
### 5. Enjoy the Game!
Once you run the script, the game window should open, allowing you to start guessing the secret code. Enter your guesses, and after each guess, the game will give you feedback on how many digits are correct and whether they are in the correct or incorrect places.

### 6. Exiting the Game
You can exit the game at any time by clicking on the close button in the game window or when you've guessed the secret code correctly.

### Additional Information
- The secret code is a 4-digit number with unique digits.
- If you make an invalid guess (e.g., fewer or more than 4 digits, non-numeric values, or repeated digits), an error message will be shown.

### License
This project is licensed under the MIT License - see the LICENSE file for details.




