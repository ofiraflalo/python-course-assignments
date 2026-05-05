Day04 - pH Calculator + Henderson-Hasselbalch

Description
In this assignment, I extended my Day03 pH calculator by adding a new feature and improving the structure.

The program calculates the pH of a solution based on the hydrogen ion concentration using the formula:

pH = -log10[H+]

New Feature (Day04)
Added Henderson-Hasselbalch equation:

[A-]/[HA] = 10^(pH - pKa)

This feature allows calculation of the ratio between conjugate base and weak acid.
It also helps determine which form is dominant:
- If pH > pKa → base (A-) is dominant
- If pH < pKa → acid (HA) is dominant

Project Structure
ph_library.py – contains the pH calculation function
henderson.py – contains the Henderson-Hasselbalch calculation
ph_input.py – program using standard input (input function)
ph_command_line.py – program using command line arguments (sys.argv)
ph_gui.py – program using a graphical user interface (tkinter)
henderson_cli.py – command line program for Henderson calculation
test_ph.py – contains test cases to verify the calculation
README.md – this file

How to Run

1. Standard Input Version
python ph_input.py

Then enter a value like: 0.001

2. Command Line Version
python ph_command_line.py 0.001

3. GUI Version
python ph_gui.py

A window will open. Enter the concentration and click the button to calculate the pH.

4. Henderson Calculation
python henderson_cli.py

Enter values for pH and pKa to calculate the ratio [A-]/[HA].

5. Test File
python test_ph.py

This will run several test cases to verify that the calculation works correctly.

Requirements
The program uses only built-in Python libraries:
math
sys
tkinter

AI Use
I used ChatGPT to help me:
- Structure the assignment
- Create separate modules for different program versions
- Add the Henderson-Hasselbalch feature

Prompts used:
- Help me move my pH calculation into a function
- Help me create separate files for input, command line, and GUI versions
- Help me add Henderson-Hasselbalch equation to my project

Interaction with other students
I reviewed other students' repositories and opened issues.
I also received feedback and improved my project accordingly.
