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
    print("Please make sure the dataset is in the same folder as main.py.")
    exit()


# -----------------------------
# Display basic information
# -----------------------------

print("\nFirst rows of the dataset:")
print(data.head())

print("\nColumns in the dataset:")
print(data.columns)


# -----------------------------
# Keep relevant columns
# -----------------------------

# The dataset contains SMILES strings and activity values.
# SMILES represents the molecular structure as text.
# standard_value represents the measured activity value, usually IC50.

required_columns = ["canonical_smiles", "standard_value"]

for col in required_columns:
    if col not in data.columns:
        print(f"\nError: Missing required column: {col}")
        exit()

# Keep only IC50 measurements if the column exists
if "standard_type" in data.columns:
    data = data[data["standard_type"] == "IC50"]

# Convert activity values to numeric
data["standard_value"] = pd.to_numeric(data["standard_value"], errors="coerce")

# Remove rows with missing SMILES or missing activity values
data = data.dropna(subset=["canonical_smiles", "standard_value"])


# -----------------------------
# Create activity labels
# -----------------------------

# Active inhibitor: IC50 <= 1000 nM
# Weak/inactive inhibitor: IC50 > 1000 nM

data["activity_class"] = data["standard_value"].apply(
    lambda x: "active" if x <= 1000 else "inactive"
)

print("\nNumber of compounds in each class:")
print(data["activity_class"].value_counts())


# -----------------------------
# Create simple molecular features from SMILES
# -----------------------------

def create_smiles_features(smiles):
    """
    This function creates simple numerical features from a SMILES string.
    These features are not full chemical descriptors, but they allow us
    to build a basic prediction model from molecular structure text.
    """

    smiles = str(smiles)

    features = {
        "smiles_length": len(smiles),
        "num_C": smiles.count("C"),
        "num_N": smiles.count("N"),
        "num_O": smiles.count("O"),
        "num_S": smiles.count("S"),
        "num_F": smiles.count("F"),
        "num_Cl": smiles.count("Cl"),
        "num_Br": smiles.count("Br"),
        "num_double_bonds": smiles.count("="),
        "num_triple_bonds": smiles.count("#"),
        "num_rings": sum(char.isdigit() for char in smiles),
        "num_branches": smiles.count("(") + smiles.count(")"),
        "num_aromatic_c": smiles.count("c"),
        "num_aromatic_n": smiles.count("n"),
        "num_aromatic_o": smiles.count("o"),
    }

    return pd.Series(features)


features = data["canonical_smiles"].apply(create_smiles_features)

model_data = pd.concat([features, data["activity_class"]], axis=1)

# Remove possible missing values
model_data = model_data.dropna()

X = model_data.drop(columns=["activity_class"])
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
# Feature importance
# -----------------------------

feature_importance = pd.DataFrame({
    "feature": X.columns,
    "importance": model.feature_importances_
}).sort_values(by="importance", ascending=False)

print("\nFeature Importance:")
print(feature_importance)


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
