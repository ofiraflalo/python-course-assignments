# Day 06 - PubChem Compound Analyzer

## Description

This project uses the PubChem database to download chemical information about selected compounds.  
PubChem is a public scientific database provided by the NIH. It contains information about chemical compounds, including molecular formulas, molecular weights, chemical structures, identifiers, and calculated chemical properties.

The program uses the PubChem PUG-REST API to retrieve compound data in JSON format.  
After downloading the data, the program processes it and creates a summary table and a graph.

## Data Source

The data is downloaded from PubChem:

https://pubchem.ncbi.nlm.nih.gov/

PubChem provides information about many chemical compounds, including:
- Molecular formula
- Molecular weight
- XLogP
- TPSA
- Hydrogen bond donors
- Hydrogen bond acceptors
- Chemical identifiers

## What the Program Does

The program downloads data for several selected compounds:

- caffeine
- aspirin
- glucose
- ethanol
- acetone

For each compound, the program retrieves:

- Molecular formula
- Molecular weight
- XLogP
- TPSA
- Number of hydrogen bond donors
- Number of hydrogen bond acceptors

Then, the program processes the data by:

- Creating a table of the results
- Calculating the average molecular weight
- Finding the compound with the highest molecular weight
- Finding the most hydrophobic compound based on XLogP
- Saving the results to a CSV file
- Creating a bar graph of molecular weight values

## How to Run

First, install the required packages:

```bash
pip install -r requirements.txt
```

Then run the program:

```bash
python pubchem_analyzer.py
```

## Output

The program creates two output files:

```text
pubchem_results.csv
molecular_weight_graph.png
```

The program also prints a short summary to the console, including the average molecular weight, the heaviest compound, and the most hydrophobic compound.

## Requirements

The required Python packages are listed in `requirements.txt`:

```text
requests
pandas
matplotlib
```

## AI Use## AI Use

I used AI to help me write and improve the Python code for this project.    
I also used AI to help organize the code, create the output table, save the results to a CSV file, and generate a graph.

Examples of prompts I used:

```text
I am working on a Python assignment that uses the PubChem API. 
Please help me write a Python program that downloads chemical properties for a list of compounds.
How can I create a bar graph of molecular weights using matplotlib?
