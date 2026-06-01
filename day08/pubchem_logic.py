import requests


def get_compound_data(compound_name):
    """
    Download chemical data for one compound from PubChem.
    """

    url = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        f"{compound_name}/property/"
        "MolecularFormula,MolecularWeight,XLogP,TPSA,HBondDonorCount,HBondAcceptorCount/JSON"
    )

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()
    properties = data["PropertyTable"]["Properties"][0]

    return {
        "compound": compound_name,
        "formula": properties.get("MolecularFormula"),
        "molecular_weight": float(properties.get("MolecularWeight")),
        "xlogp": properties.get("XLogP"),
        "tpsa": properties.get("TPSA"),
        "h_bond_donors": properties.get("HBondDonorCount"),
        "h_bond_acceptors": properties.get("HBondAcceptorCount"),
    }


def analyze_compounds(compound_names):
    """
    Get data for several compounds and calculate simple summary values.
    """

    results = []

    for compound in compound_names:
        compound_data = get_compound_data(compound.strip())
        if compound_data is not None:
            results.append(compound_data)

    if len(results) == 0:
        return {
            "compounds": [],
            "average_molecular_weight": None,
            "heaviest_compound": None,
            "most_hydrophobic_compound": None,
        }

    average_molecular_weight = sum(
        compound["molecular_weight"] for compound in results
    ) / len(results)

    heaviest_compound = max(
        results,
        key=lambda compound: compound["molecular_weight"]
    )

    compounds_with_xlogp = [
        compound for compound in results if compound["xlogp"] is not None
    ]

    if compounds_with_xlogp:
        most_hydrophobic_compound = max(
            compounds_with_xlogp,
            key=lambda compound: compound["xlogp"]
        )
    else:
        most_hydrophobic_compound = None

    return {
        "compounds": results,
        "average_molecular_weight": average_molecular_weight,
        "heaviest_compound": heaviest_compound["compound"],
        "most_hydrophobic_compound": (
            most_hydrophobic_compound["compound"]
            if most_hydrophobic_compound is not None
            else None
        ),
    }
