import pandas as pd
import vega_datasets
import ipywidgets as widgets
from ipywidgets import interactive, fixed
from av_price_country import plot_av_price_country
from price_point_correlation import plot_price_point_correlation
from taster_specialization import plot_taster_spec
from word_appearance import to_list, plot_word_freqs

if __name__ == '__main__':
    
    df = pd.read_csv("data/winemag_data_130k_v2.csv")

    plot_av_price_country(df)
    plot_price_point_correlation(df)
    plot_taster_spec(df)

    df_short = df[["country", "price","variety","points","province"]]
    df_short = df_short.dropna()

    countries = to_list(df_short, "country", 10)
    varieties = to_list(df_short, "variety", 1000)

    # using 'interactive' to make the plot modifiable in real time

    interactive(plot_word_freqs,
                df=fixed(df),
                category=fixed("country"),
                choice=widgets.Dropdown(options=countries, description='Country:', disabled=False))

    interactive(plot_word_freqs,
                df=fixed(df),
                category=fixed("variety"),
                choice=widgets.Dropdown(options=varieties, description='Variety:', disabled=False))
    
    interactive(plot_word_freqs,
                df=fixed(df),
                category=fixed("points"),
                choice=widgets.FloatRangeSlider(min=df["points"].min(), max=df["points"].max()))