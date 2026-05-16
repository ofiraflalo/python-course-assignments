import pandas as pd
from noe_ph_analysis import estimate_ph_from_enhancement


def test_exact_calibration_value():
    calibration_df = pd.DataFrame({
        "pH": [5.0, 6.0, 7.0],
        "enhancement_percent": [10, 30, 50]
    })

    result = estimate_ph_from_enhancement(30, calibration_df)

    assert result == 6.0


def test_interpolation_between_two_values():
    calibration_df = pd.DataFrame({
        "pH": [5.0, 6.0, 7.0],
        "enhancement_percent": [10, 30, 50]
    })  

    result = estimate_ph_from_enhancement(40, calibration_df)

    assert result == 6.5


def test_lowest_value():
    calibration_df = pd.DataFrame({
        "pH": [5.0, 6.0, 7.0],
        "enhancement_percent": [10, 30, 50]
    })

    result = estimate_ph_from_enhancement(10, calibration_df)

    assert result == 5.0
