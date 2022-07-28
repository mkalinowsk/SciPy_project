import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#csv tschick machen
#Which country has the highest average price?
dfwine = pd.read_csv("/Users/marijkekalinowski/Desktop/SciPy/SciPy_Project/winemag_data_130k_v2.csv")
df_provice_price = dfwine[["country", "price"]]
df_provice_price = df_provice_price.dropna()
df_av_country = df_provice_price.groupby(["country"]).agg({"price":"mean"})
df_country_no_wine = df_provice_price.groupby(["country"]).size()
print(df_country_no_wine)
df_country_no_wine = df_country_no_wine.to_frame()

# #plot mit 10 min Weinen
df_av_country = df_av_country.drop(df_country_no_wine[df_country_no_wine.iloc[:,0] < 10].index)
df_av_country_sorted = df_av_country.sort_values("price")
df_av_country_sorted.plot.bar(y = 'price', use_index = True, title = "Which country has the highest average price?", ylabel = 'Average price for a bottle of wine')
plt.show()




