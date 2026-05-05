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

## How to Run

### 1. Standard Input
```bash
python ph_input.py
```

### 2. Command Line
```bash
python ph_command_line.py 0.001
```

### 3. GUI
```bash
python ph_gui.py
```

### 4. Henderson Calculation
```bash
python henderson_cli.py
```

### 5. Tests
```bash
python test_ph.py
```

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
I reviewed other students' repositories and opened issues.  
I also received feedback and improved my project accordingly.
