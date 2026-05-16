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
```bash
python noe_ph_analysis.py
