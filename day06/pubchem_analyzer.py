import requests
import pandas as pd
import matplotlib.pyplot as plt


def get_compound_data(compound_name):
    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        f"{compound_name}/property/"
        "MolecularFormula,MolecularWeight,XLogP,TPSA,HBondDonorCount,HBondAcceptorCount/JSON"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Could not find data for: {compound_name}")
        return None

    data = response.json()
    properties = data["PropertyTable"]["Properties"][0]

    return {
        "Compound": compound_name,
        "Formula": properties.get("MolecularFormula"),
        "Molecular Weight": properties.get("MolecularWeight"),
        "XLogP": properties.get("XLogP"),
        "TPSA": properties.get("TPSA"),
        "H-Bond Donors": properties.get("HBondDonorCount"),
        "H-Bond Acceptors": properties.get("HBondAcceptorCount"),
    }


def main():
    compounds = ["caffeine", "aspirin", "glucose", "ethanol", "acetone"]

    results = []

    for compound in compounds:
        compound_data = get_compound_data(compound)
        if compound_data is not None:
            results.append(compound_data)

    df = pd.DataFrame(results)

    print("\nDownloaded compound data:")
    print(df)

    df["Molecular Weight"] = pd.to_numeric(df["Molecular Weight"], errors="coerce")
    df["XLogP"] = pd.to_numeric(df["XLogP"], errors="coerce")

    df.to_csv("pubchem_results.csv", index=False)

    average_mw = df["Molecular Weight"].mean()
    print(f"\nAverage molecular weight: {average_mw:.2f}")

    heaviest = df.loc[df["Molecular Weight"].idxmax()]
    print(f"Heaviest compound: {heaviest['Compound']}")

    most_hydrophobic = df.loc[df["XLogP"].idxmax()]
    print(f"Most hydrophobic compound: {most_hydrophobic['Compound']}")

    plt.figure(figsize=(8, 5))
    plt.bar(df["Compound"], df["Molecular Weight"])
    plt.xlabel("Compound")
    plt.ylabel("Molecular Weight")
    plt.title("Molecular Weight of Selected Compounds")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("molecular_weight_graph.png")
    plt.show()


if __name__ == "__main__":
    main()
