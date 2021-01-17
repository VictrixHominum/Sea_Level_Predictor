import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level", s=3, label="Sea Level",)

    res = linregress(x=df.Year, y=df["CSIRO Adjusted Sea Level"])

    x2 = list(range(1880, 2050))
    y2 = []

    for year in x2:
        y2.append(res.intercept+res.slope*year)

    plt.plot(x2, y2, 'r', label="Historic Increase")


    df_mod = df[df['Year']>=2000]

    res2 = linregress(x=df_mod.Year, y=df_mod["CSIRO Adjusted Sea Level"])

    x3 = list(range(2000, 2050))
    y3 = []

    for year in x3:
        y3.append(res2.intercept + res2.slope * year)

    plt.plot(x3, y3, 'r', label="Modern Increase")

    plt.title('Rise in Sea Level')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.xticks(ticks=[1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

    plt.savefig('sea_level_plot.png')
    return plt.gca()