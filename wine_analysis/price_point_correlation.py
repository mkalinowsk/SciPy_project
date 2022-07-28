import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Does the price of the wine correlate with the points (given by the wine taster)?
def plot_price_point_correlation(df):

    # correlation analysis
    df_price_points = df[["price","points"]]
    df_price_points = df_price_points.dropna()

    av_price = df_price_points.groupby(["points"]).agg({"price": "mean"})

    av_price.plot(y='price', use_index=True, marker="o", grid=True, color="orange", figsize=(10, 6), fontsize=12)
    plt.title("Average price of wines at each pointlevel", fontsize=15)
    plt.xlabel("Points", fontsize=13)
    plt.ylabel("Average price", fontsize=13)
    plt.show()

    # calculate correlation coefficient 
    cov_price_points = np.cov(df_price_points["price"], df_price_points["points"])[0][1]
    std_price = np.std(df_price_points["price"])
    std_points = np.std(df_price_points["points"])

    p_val = cov_price_points / (std_price * std_points)

    print("Correlation coefficient = {}".format(p_val))