# 🤖 Reeborg's World - Escaping the Maze

A Python program that guides a robot through a maze and helps it reach the goal using conditional logic, functions, and `while` loops.

## 📌 About

This project was created as part of my learning journey through the **100 Days of Code – The Complete Python Pro Bootcamp** by Angela Yu.

The challenge was completed in **Reeborg's World**, an interactive environment where Python code is used to control a robot.

The program uses the **right-hand rule** to navigate through the maze and reach the goal.

## 🧠 What I Learned

* Defining and using functions with `def`
* Creating a custom `turn_right()` function
* Using `while` loops
* Using `while` with conditions
* Using `if`, `elif`, and `else` for decision-making
* Using built-in Reeborg functions such as `move()`, `turn_left()`, `front_is_clear()`, `right_is_clear()`, and `at_goal()`

## 🛠️ Technologies

* Python
* Reeborg's World

## ▶️ How It Works

The program first moves the robot to the starting position of the maze.

It then repeatedly checks the environment:

1. If the right side is clear, the robot turns right and moves forward.
2. If the right side is blocked but the front is clear, the robot moves forward.
3. If both the right side and front are blocked, the robot turns left.
4. The loop continues until the robot reaches the goal.

## 🌐 Environment

This project was completed using **Reeborg's World**, an interactive Python programming environment.

The `solution.py` file contains the code used to solve the maze.

## 📚 Course

Part of **100 Days of Code – The Complete Python Pro Bootcamp** by **Angela Yu**.
