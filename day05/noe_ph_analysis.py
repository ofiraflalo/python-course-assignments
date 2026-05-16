import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def estimate_ph_from_enhancement(enhancement_value, calibration_df):
    """
    Estimate pH from an enhancement value using linear interpolation.

    Parameters
    ----------
    enhancement_value : float
        The measured NOE enhancement percentage.
    calibration_df : pandas.DataFrame
        DataFrame with columns: pH and enhancement_percent.

    Returns
    -------
    float
        Estimated pH value.
    """
    enhancement_values = calibration_df["enhancement_percent"].values
    ph_values = calibration_df["pH"].values

    estimated_ph = np.interp(enhancement_value, enhancement_values, ph_values)
    return estimated_ph


def analyze_samples(
    calibration_file="input/calibration_data.csv",
    unknown_file="input/unknown_samples.csv",
    output_file="output/estimated_ph_results.csv",
    plot_file="output/calibration_plot.png"
):
    """
    Read calibration and unknown sample data,
    estimate pH values, save results, and create a plot.
    """

    calibration_df = pd.read_csv(calibration_file)
    unknown_df = pd.read_csv(unknown_file)

    estimated_ph_values = []

    for enhancement in unknown_df["enhancement_percent"]:
        estimated_ph = estimate_ph_from_enhancement(enhancement, calibration_df)
        estimated_ph_values.append(round(estimated_ph, 2))

    unknown_df["estimated_pH"] = estimated_ph_values

    Path("output").mkdir(exist_ok=True)

    unknown_df.to_csv(output_file, index=False)

    plt.figure(figsize=(8, 5))

    plt.plot(
        calibration_df["pH"],
        calibration_df["enhancement_percent"],
        marker="o",
        label="Calibration data"
    )

    plt.scatter(
        unknown_df["estimated_pH"],
        unknown_df["enhancement_percent"],
        marker="x",
        s=80,
        label="Unknown samples"
    )

    for _, row in unknown_df.iterrows():
        plt.text(
            row["estimated_pH"],
            row["enhancement_percent"],
            row["sample_id"],
            fontsize=9
        )

    plt.xlabel("pH")
    plt.ylabel("NOE enhancement (%)")
    plt.title("Bicarbonate NOE pH Calibration")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(plot_file)
    plt.close()

    return unknown_df


if __name__ == "__main__":
    results = analyze_samples()
    print("Analysis completed.")
    print(results)
