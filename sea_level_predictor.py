import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create first line of best fit
    result = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years_extended = range(1880, 2051)

    ax.plot(
        years_extended,
        result.intercept + result.slope * pd.Series(years_extended)
    )

    # Create second line of best fit using data from year 2000 through most recent year
    df_recent = df[df["Year"] >= 2000]

    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = range(2000, 2051)

    ax.plot(
        years_recent,
        result_recent.intercept + result_recent.slope * pd.Series(years_recent)
    )

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing
    fig.savefig("sea_level_plot.png")
    return fig
