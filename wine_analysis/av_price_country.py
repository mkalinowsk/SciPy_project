import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Which country has the highest average price? What about those that have at least 10 wines?
def plot_av_price_country(df):

    df_country_price = df[["country", "price"]]
    df_country_price = df_country_price.dropna()

    av_price = df_country_price.groupby(["country"]).agg({"price":"mean"})
    country_amount_wine = df_country_price.groupby(["country"]).size()
    df_country_amount_wine = country_amount_wine.to_frame()

    # plot with all countries
    av_price_sorted = av_price.sort_values("price")
    av_price_sorted.plot.bar(y='price', use_index=True, figsize=(20, 8), fontsize=13)
    plt.title("Average wine price per country", fontsize=20)
    plt.xlabel("Country", fontsize=18)
    plt.ylabel("Average price for a bottle of wine", fontsize=18)
    plt.show()

    # plot with those countries with at least ten wines
    av_price_ten = av_price.drop(df_country_amount_wine[df_country_amount_wine.iloc[:,0] < 10].index)
    av_price_sorted = av_price_ten.sort_values("price")
    av_price_sorted.plot.bar(y='price', use_index=True, figsize=(20, 8), fontsize=13)
    plt.title("Average wine price per country in which at least ten wines are produced", fontsize=20)
    plt.xlabel("Country", fontsize=18)
    plt.ylabel("Average price for a bottle of wine", fontsize=18)
    plt.show()