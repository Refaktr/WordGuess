# Python Wordle Clone 🎯

A terminal-based implementation of the popular word-guessing game Wordle, written in Python. This clone features multiple difficulty levels and a clean, colorful interface.

## 🎮 Features

- **Multiple Difficulty Levels:**
  - Easy: 4-letter words
  - Medium: 5-letter words  
  - Hard: 6-letter words

- **Visual Feedback:**
  - 🟩 Green: Correct letter in correct position
  - 🟨 Yellow: Correct letter in wrong position
  - 🟥 Red: Letter not in the word
  - Real-time alphabet tracking

- **Game Mechanics:**
  - 6 attempts to guess the word
  - Input validation (only valid words accepted)
  - Clean terminal interface with color coding
  - Play again option

## 📋 Requirements

- Python 3.6 or higher
- Terminal with ANSI color support (most modern terminals)

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd Wordle-Clone
   ```

2. Run the game:
   ```bash
   python wordle.py
   ```

3. Choose your difficulty level and start guessing!

## 🎯 How to Play

1. **Choose Difficulty:** Select from 4, 5, or 6-letter words
2. **Make Guesses:** Enter valid English words of the chosen length
3. **Use Feedback:** 
   - Green letters are in the correct position
   - Yellow letters are in the word but wrong position
   - Red letters are not in the word
4. **Win:** Guess the word within 6 attempts!

## 📁 Project Structure

```
Wordle-Clone/
├── wordle.py     # Main game file
├── 4.txt         # 4-letter word dictionary (2,252 words)
├── 5.txt         # 5-letter word dictionary (5,757 words)
├── 6.txt         # 6-letter word dictionary (374 words)
└── README.md     # This file
```

## 🛠️ Technical Details

- **Language:** Python 3
- **Libraries:** Built-in modules only (`random`, `os`)
- **Features:**
  - Object-oriented design with `LetterTracker` class
  - ANSI escape codes for terminal colors
  - Cross-platform screen clearing
  - Comprehensive input validation

## 🎨 Screenshots

```
🎯 Guess the 5-letter word!
Good luck! 🍀
Guess 1/6

==================================================
ALPHABET STATUS:
==================================================
 A  B  C  D  E  F  G  H  I  J 
   K  L  M  N  O  P  Q  R  S 
      T  U  V  W  X  Y  Z 
==================================================
🟩 Correct | 🟨 Wrong position | 🟥 Not in word | ⬜ Not guessed
==================================================

YOUR GUESSES:
------------------------------
  (No guesses yet)
------------------------------

Enter your guess: 
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements! Some ideas:
- Add more word lists
- Implement hints system
- Add statistics tracking
- Create a GUI version

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by the original Wordle game by Josh Wardle
- Word lists compiled from various public domain dictionaries
- Built as a learning project to practice Python programming

## 🐛 Known Issues

- Requires terminal with ANSI color support
- Word validation is dictionary-based (some valid words might not be included)

---

**Enjoy playing! 🎉**
