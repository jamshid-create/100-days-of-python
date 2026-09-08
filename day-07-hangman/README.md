# 🎯 Hangman

A classic Hangman game built in Python where the player tries to guess a randomly selected word before running out of lives.

## 📌 About

This project was created as part of my learning journey through the **100 Days of Code – The Complete Python Pro Bootcamp** by Angela Yu.

The player attempts to guess a hidden word one letter at a time. For each correct guess, the letter is revealed. Incorrect guesses reduce the player's remaining lives. The game ends when the player guesses the word correctly or runs out of lives.

This project focuses on combining concepts learned in previous days and applying them together to build a complete Python game.

## 🧠 What I Learned

* Combining previously learned Python concepts to build a complete project
* Using Python modules to organize code across multiple files
* Importing variables and functions from custom modules
* Managing game state using variables
* Using loops and conditional logic together to control the game flow
* Tracking previously guessed letters using a list

## 🛠️ Technologies

* Python

## 🎮 How to Play

1. Run the program.
2. A random word will be selected.
3. Guess one letter at a time.
4. Correct guesses reveal the letter in the hidden word.
5. Incorrect guesses reduce your remaining lives.
6. Guess the entire word before you run out of lives to win.

## 📂 Files

* `main.py` — Contains the main game logic.
* `hangman_word.py` — Contains the list of possible words.
* `hangman_art.py` — Contains the Hangman ASCII art and game logo.

## 💻 Example

```text
Guess a letter: a

word to guess: -a--a-

**********************5/6 LIVES LEFT***********************

Guess a letter: z

You guessed z, that's not in the word. You lose a life.

**********************4/6 LIVES LEFT***********************
```

## 📚 Course

Part of **100 Days of Code – The Complete Python Pro Bootcamp** by **Angela Yu**.
