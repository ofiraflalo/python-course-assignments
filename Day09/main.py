import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay


# -----------------------------
# Load dataset
# -----------------------------

file_name = "acetylcholinesterase_data.csv"

try:
    data = pd.read_csv(file_name)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    print("Please download the dataset and save it in the same folder as main.py.")
    exit()


# -----------------------------
# Display basic information
# -----------------------------

print("\nFirst rows of the dataset:")
print(data.head())

print("\nColumns in the dataset:")
print(data.columns)


# -----------------------------
# Clean and prepare the data
# -----------------------------

# This project uses IC50 values to classify molecules as active or inactive inhibitors.
# The column names may be slightly different depending on the downloaded dataset.
# Common ChEMBL/Kaggle column names include:
# "standard_value", "Standard Value", or "IC50"

possible_ic50_columns = ["standard_value", "Standard Value", "IC50", "pIC50"]

ic50_column = None

for col in possible_ic50_columns:
    if col in data.columns:
        ic50_column = col
        break

if ic50_column is None:
    print("\nError: Could not find an IC50 / activity value column.")
    print("Please check the dataset column names and update the code.")
    exit()

print(f"\nUsing activity column: {ic50_column}")

# Convert IC50 column to numeric values
data[ic50_column] = pd.to_numeric(data[ic50_column], errors="coerce")

# Remove rows without activity values
data = data.dropna(subset=[ic50_column])


# -----------------------------
# Create labels
# -----------------------------

# Active inhibitor: IC50 <= 1000 nM
# Inactive / weak inhibitor: IC50 > 1000 nM

data["activity_class"] = data[ic50_column].apply(
    lambda x: "active" if x <= 1000 else "inactive"
)

print("\nNumber of compounds in each class:")
print(data["activity_class"].value_counts())


# -----------------------------
# Select features
# -----------------------------

# The code tries to use common molecular descriptor columns if they exist.
# If the dataset has different column names, update this list.

possible_features = [
    "MW",
    "Molecular Weight",
    "molecular_weight",
    "LogP",
    "AlogP",
    "NumHDonors",
    "HBD",
    "NumHAcceptors",
    "HBA",
]

available_features = [col for col in possible_features if col in data.columns]

if len(available_features) < 2:
    print("\nNot enough molecular descriptor columns were found.")
    print("The dataset may only contain SMILES and IC50 values.")
    print("Please use a dataset that includes molecular descriptors such as MW, LogP, HBD, and HBA.")
    print("Available columns are:")
    print(data.columns)
    exit()

print("\nUsing features:")
print(available_features)

# Keep only selected feature columns and target
model_data = data[available_features + ["activity_class"]].copy()

# Convert all features to numeric
for feature in available_features:
    model_data[feature] = pd.to_numeric(model_data[feature], errors="coerce")

# Remove rows with missing feature values
model_data = model_data.dropna()

X = model_data[available_features]
y = model_data["activity_class"]


# -----------------------------
# Split the data
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -----------------------------
# Train model
# -----------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# -----------------------------
# Evaluate model
# -----------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(round(accuracy, 3))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# -----------------------------
# Confusion matrix
# -----------------------------

cm = confusion_matrix(y_test, y_pred, labels=model.classes_)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

disp.plot()
plt.title("Confusion Matrix - Enzyme Inhibition Prediction")
plt.savefig("confusion_matrix.png", dpi=300, bbox_inches="tight")
plt.show()

print("\nConfusion matrix saved as confusion_matrix.png")


# -----------------------------
# Example prediction
# -----------------------------

example = X_test.iloc[[0]]
example_prediction = model.predict(example)

print("\nExample molecule features:")
print(example)

print("\nPredicted activity class:")
print(example_prediction[0])
