# 🐍 Day 6: Escaping the Maze & Logic Gates

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

---

### 🧪 Project Overview
Day 6 shifted focus from "Iterating over data" to **Algorithmic Control Flow**. The mission was to master **While Loops** and **Functions**—teaching the code to think and react to changing conditions rather than just repeating a fixed set of instructions. The primary project, **The Labyrinth Escape**, implements a pathfinding algorithm to navigate a robot through a dynamic maze.

### 🧠 Skills Mastered
* **Defining Functions:** Creating custom blocks of code using `def` to modularize logic and improve readability.
* **While Loops:** executing code blocks repeatedly *only* while a specific condition remains true (Indefinite Iteration).
* **Algorithmic Thinking:** Breaking down complex navigation problems into small, reusable steps.
* **Control Flow Management:** Handling "Infinite Loops" and ensuring exit conditions are always met.
* **Scope & Indentation:** Understanding how code blocks adhere to hierarchy in Python.

---

### 🔐 Main Project: The Labyrinth Escape
A logic-based script designed to guide an agent (Reeborg) out of a procedurally generated maze.
* **The Challenge:** The agent does not know the map layout and must react to walls and open spaces in real-time.
* **The Logic (Right-Hand Rule):** The algorithm prioritizes turning right whenever possible. If the path is blocked, it attempts to move straight; if that is also blocked, it turns left. This guarantees an exit in any standard "simply connected" maze.
* **Key Function:** `while not at_goal():` ensures the agent continues solving until the objective is reached, regardless of maze size.

---

### 🧮 The Logic Lab (Supporting Scripts)
To prepare for the final maze, I built several logic gates to handle variable obstacles:
* **The Hurdle Jumper:** A script using `while` loops to detect walls of varying heights and execute a "jump" function only when necessary.
* **The Variable Flag:** Logic that accounts for random start and end points, requiring the code to "search" for the finish line rather than counting steps.
* **Square Route:** A simple function exercise to practice calling custom commands within other loops to create geometric patterns.

> "A While Loop is the difference between a machine that repeats and a machine that waits."

---

### 🛠️ Tech Stack
* **Language:** Python 3
* **Concepts:** While Loops, Function Definitions, Logical Operators (`not`, `and`)
* **Algorithm:** Depth-First Search (Simplified/Wall Follower)

---
[↩ Return to Main Portfolio](https://github.com/Vinayak-Burgess)