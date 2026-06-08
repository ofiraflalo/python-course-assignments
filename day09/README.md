# Enzyme Inhibition Prediction

## Project Description

This project analyzes bioactivity data of molecules tested against the enzyme acetylcholinesterase.  
The goal is to build a machine learning model that predicts whether a molecule is likely to be an active enzyme inhibitor or a weak/inactive inhibitor.

This topic is related to protein and enzyme inhibition, which connects to research areas such as protein recognition, ligand-protein interactions, and regulation of protein activity.

## Dataset

The dataset contains acetylcholinesterase inhibition data from ChEMBL / Kaggle.

The data includes molecular information such as SMILES strings and biological activity values such as IC50.

## Prediction Task

The model predicts whether a molecule is:

- Active inhibitor
- Weak or inactive inhibitor

The classification is based on IC50 values.

## How to Run

1. Download the dataset from Kaggle:
   Human Acetylcholinesterase Dataset from ChEMBL

2. Save the CSV file inside the project folder.

3. Install the required packages:

```bash
pip install -r requirements.txt
```

Then run the script:

```bash
python main.py
```

## Output

The program prints:

* Dataset preview
* Number of active and inactive compounds
* Model accuracy
* Classification report

The program also saves a confusion matrix figure as:

```text
confusion_matrix.png
```

## AI Use

ChatGPT was used to help:

* Choose the project topic
* Connect the project to enzyme inhibition research
* Design the machine learning workflow

The prompts used during the project are included in the file:

## Prompts

```text

Prompts:
Please help me design a Python machine learning project that predicts whether a molecule is an active enzyme inhibitor based on bioactivity data such as IC50 values.
Please write Python code using pandas and scikit-learn to train a Random Forest model that classifies molecules as active or inactive inhibitors based on IC50 values and molecular descriptors.
Please improve and organize the README section that explains how to run the script, what the output is, and how ChatGPT was used in the project.
```

