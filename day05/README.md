# Day05 - NMR pH Calibration Analysis

This project analyzes simulated NMR bicarbonate NOE data to estimate pH values of unknown samples.


## Description
This project analyzes simulated NMR bicarbonate NOE data.

The goal is to use a calibration file with known pH values and NOE enhancement percentages, and then estimate the pH of unknown samples based on their measured enhancement.

This is a useful calculation because in NMR experiments, calibration curves can help connect a measured signal to a chemical property such as pH.

## Input files
The project uses two CSV input files:

1. `calibration_data.csv`  
   Contains known pH values and their measured enhancement percentages.

2. `unknown_samples.csv`  
   Contains unknown samples with measured enhancement percentages.

## Output files
The program creates:

1. `estimated_ph_results.csv`  
   A table with the estimated pH for each unknown sample.

2. `calibration_plot.png`  
   A graph showing the calibration curve and the unknown samples.

## How to run

First install the required packages, then run the analysis:

```bash
pip install -r requirements.txt
python noe_ph_analysis.py
```

## How to run tests

Run the tests with:

```bash
python -m pytest test_noe_ph_analysis.py
```

## Test result

The tests were run using pytest, and all 3 tests passed.

## Notes

The data in this project is simulated and does not contain private lab data. The project is based on the idea of using NMR bicarbonate NOE enhancement as a possible pH-related measurement.

## AI use and prompts

I used chatGPT https://chatgpt.com/ to help plan the project, create tests and debug errors.

Example prompts:
- "Write pytest tests for the pH estimation function."
- "Help me debug missing package and file path errors."



