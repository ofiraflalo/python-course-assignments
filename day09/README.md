# Enzyme Inhibition Prediction

##  Description

This project analyzes bioactivity data of molecules tested against the enzyme acetylcholinesterase.
The goal is to build a machine learning model that predicts whether a molecule is likely to be an active enzyme inhibitor or a weak/inactive inhibitor.


## Dataset

The dataset contains acetylcholinesterase inhibition data from Kaggle.

The data includes molecular information such as SMILES strings and biological activity values such as IC50.

The dataset file used in this project is:

```text
acetylcholinesterase_data.csv
```

## Prediction Task

The model predicts whether a molecule is:

* Active inhibitor
* Weak or inactive inhibitor

The classification is based on IC50 values.

In this project, molecules are classified as:

```text
Active inhibitor: IC50 <= 1000 nM
Weak/inactive inhibitor: IC50 > 1000 nM
```

## Machine Learning Approach

This project uses a supervised machine learning approach.

The dataset contains SMILES strings, which represent molecular structures as text, and IC50 activity values.

Because the dataset does not include calculated molecular descriptors such as molecular weight or LogP, the script creates simple numerical features directly from the SMILES strings.

Examples of features used in the model include:

* SMILES length
* Number of carbon atoms
* Number of nitrogen atoms
* Number of oxygen atoms
* Number of aromatic carbons
* Number of rings
* Number of branches
* Number of double bonds

The model used in this project is a Random Forest Classifier.

## How to Run

1. Download the dataset from Kaggle:

```text
Human Acetylcholinesterase Dataset from ChEMBL
```

2. Save the CSV file inside the project folder with the following name:

```text
acetylcholinesterase_data.csv
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the script:

```bash
python main.py
```

## Output

The program prints:

* Dataset preview
* Number of active and inactive compounds
* Model accuracy
* Classification report
* Feature importance

The program also saves a confusion matrix figure as:

```text
confusion_matrix.png
```

## Results

The model achieved an accuracy of approximately:

```text
0.819
```

This means that the model correctly predicted whether a molecule was active or inactive in about 82% of the test cases.

The confusion matrix shows the number of correct and incorrect predictions for both active and inactive inhibitors.

## AI Use

ChatGPT was used to help:

* Connect the project to enzyme inhibition research
* Design the machine learning workflow
* Write and update the Python code


The prompts used during the project are included below.

## Prompts

```text
Prompt 1:
Please help me design a Python machine learning project that predicts whether a molecule is an active enzyme inhibitor based on bioactivity data such as IC50 values.

Prompt 2:
Please write Python code using pandas and scikit-learn to train a Random Forest model that classifies molecules as active or inactive inhibitors based on IC50 values.


```




