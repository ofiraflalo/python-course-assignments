# Day04 - pH Calculator + Henderson-Hasselbalch

## Description
In this assignment, I extended my Day03 pH calculator by adding a new feature and improving the structure.

The program calculates the pH of a solution based on the hydrogen ion concentration using the formula:

pH = -log10[H+]

---

## New Feature (Day04)
Added Henderson-Hasselbalch equation:

[A-]/[HA] = 10^(pH - pKa)

This feature allows calculation of the ratio between conjugate base and weak acid.

- If pH > pKa → base (A-) is dominant  
- If pH < pKa → acid (HA) is dominant  

---

## Project Structure
- ph_library.py – pH calculation  
- henderson.py – Henderson calculation  
- ph_input.py – input version  
- ph_command_line.py – command line version  
- ph_gui.py – GUI version  
- henderson_cli.py – Henderson CLI version  
- test_ph.py – test cases  
- README.md – this file  

---

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

### 4. Henderson Calculation

python henderson_cli.py

Then enter values like:
pH: 7  
pKa: 6  

The program will calculate the ratio [A-]/[HA] and display which form is dominant.

---

### 5. Tests

python test_ph.py

This will run several test cases to verify that the calculations work correctly.

---

## Requirements
Built-in Python libraries:
- math  
- sys  
- tkinter  

---

## AI Use
I used ChatGPT to:
- Structure the project  
- Create separate modules  
- Add the Henderson-Hasselbalch feature  

**Prompts used:**
- Help me move my pH calculation into a function  
- Help me create separate files for input, command line, and GUI versions  
- Help me add Henderson-Hasselbalch equation  

---

## Interaction with other students
I reviewed other students repositories and opened issues.  
I also received feedback and improved my project accordingly.
