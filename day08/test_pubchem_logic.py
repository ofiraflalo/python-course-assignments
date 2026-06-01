from pubchem_logic import analyze_compounds


def test_analyze_compounds_with_valid_compounds():
    compounds = ["caffeine", "aspirin"]

    result = analyze_compounds(compounds)

    assert "compounds" in result
    assert "average_molecular_weight" in result
    assert "heaviest_compound" in result
    assert len(result["compounds"]) == 2
    assert result["average_molecular_weight"] > 0


def test_analyze_compounds_with_invalid_compound():
    compounds = ["notarealcompoundname12345"]

    result = analyze_compounds(compounds)

    assert result["compounds"] == []
    assert result["average_molecular_weight"] is None
    assert result["heaviest_compound"] is None
