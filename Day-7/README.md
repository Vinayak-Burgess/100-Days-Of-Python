# 🐍 Day 7: The Hangman Game & Logic Flow

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

---

### 🧪 Project Overview
Day 7 focused on **Logic Flow and Conditionals** within a complex, multi-stage application. The objective was to build a classic **Hangman Game**, which requires tracking user states (lives, guesses), manipulating lists in real-time, and importing custom modules for art and data. This project bridges the gap between simple scripts and interactive, state-aware applications.

### 🧠 Skills Mastered
* **While Loops & Flags:** Using a `game_over` boolean flag to keep the game loop running until a specific win/loss condition is met.
* **List Manipulation:** checking for existence (`in` keyword), appending new guesses, and replacing placeholders in a display list.
* **Module Imports:** separating code into logical files (`hangman_words.py`, `hangman_art.py`) to keep the main logic clean and professional.
* **String Methods:** Using `.join()` to convert list data into user-friendly strings for display.
* **User Input Validation:** implementing checks (`isalpha()`, `len()`) to prevent crashes from invalid keystrokes.

---

### 💀 Main Project: The Hangman Game
A CLI-based implementation of the classic word-guessing game with visual feedback.
* **The Logic:** The system selects a random word from an external module and generates a "blank" version (underscores). As the user guesses, the script iterates through the chosen word to find matches, revealing letters while preserving the positions of un-guessed characters.
* **Visual Feedback:** Integreates ASCII art stages that update dynamically based on the `lives` variable.
* **State Management:** Tracks "Guessed Letters" to prevent users from wasting turns on repeats and provides distinct feedback for "Already Guessed" vs. "Wrong Guess."

---

### 🧮 The Logic Lab (Supporting Scripts)
To prepare for the final game architecture, I focused on these sub-skills:
* **Random Word Picker:** A script to import and select random items from external lists.
* **Display Logic:** Exercises in replacing characters within a list based on index positions.
* **Life Tracker:** Logic that decrements a counter only on specific failure conditions while keeping the main loop active.

> "A While Loop is the difference between a machine that repeats and a machine that waits."

---

### 🛠️ Tech Stack
* **Language:** Python 3
* **Modules:** `random`, `hangman_words`, `hangman_art`
* **Concepts:** While Loops, `in` / `not in`, List Indexing, String Formatting

---
[↩ Return to Main Portfolio](https://github.com/Vinayak-Burgess)