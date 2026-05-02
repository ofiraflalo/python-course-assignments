# Day 03 - pH Calculator

## Description

In this assignment, I improved my Day 02 pH calculator by organizing the code in a more structured way.

The main calculation (business logic) was moved into a separate function inside a dedicated library file.

The program calculates the pH of a solution based on the hydrogen ion concentration using the formula:

pH = -log10[H+]

---

## Project Structure

- ph_library.py – contains the pH calculation function  
- ph_input.py – program using standard input (input function)  
- ph_command_line.py – program using command line arguments (sys.argv)  
- ph_gui.py – program using a graphical user interface (tkinter)  
- test_ph.py – contains test cases to verify the calculation  
- README.md – this file  

---

## How to Run

### 1. Standard Input Version

python ph_input.py

Then enter a value like:
0.001

---

### 2. Command Line Version

python ph_command_line.py 0.001

---

### 3. GUI Version

python ph_gui.py

A window will open. Enter the concentration and click the button to calculate the pH.

---

### 4. Test File

python test_ph.py

This will run several test cases to verify that the calculation works correctly.

---


The program uses only built-in Python libraries:

- math  
- sys  
- tkinter  

---

## AI Use

I used ChatGPT to help me structure the assignment and improve my code.

Prompts used:

- Help me move my pH calculation into a function  
- Help me create separate files for input, command line, and GUI versions  
- Help me write test cases for my pH function  
