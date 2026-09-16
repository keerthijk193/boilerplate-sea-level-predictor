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

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create years from the first year through 2050
    years = pd.Series(
        range(int(df["Year"].min()), 2051)
    )

    # Plot first line of best fit
    ax.plot(
        years,
        slope * years + intercept
    )

    # Use data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]

    # Line of best fit using data from 2000 onwards
    slope_2000, intercept_2000, r_value, p_value, std_err = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Create years from 2000 through 2050
    years_recent = pd.Series(
        range(2000, 2051)
    )

    # Plot second line of best fit
    ax.plot(
        years_recent,
        slope_2000 * years_recent + intercept_2000
    )

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save and return plot
    fig.savefig("sea_level_plot.png")
    return ax