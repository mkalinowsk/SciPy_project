from dataclasses import replace
import pandas as pd
import matplotlib.pyplot as plt


#Do certain words appear more often in the ratings than others? Does this have anything to do with the characteristics of the wine?
#Plotting the word frequencies of the top n words for the characteristics price, province and points. 
#To make this plot interactive we are using jupyter widgets like a dropdown where the user can choose category and a slider to choose a prices/ point range
#Using the slider you could select different prices for which then the plot shows the respective word frequencies.

df = pd.read_csv("/Users/marijkekalinowski/Desktop/SciPy/SciPy_Project/winemag_data_130k_v2.csv")
def choose_data(df, choise):
    dfwine = df.loc[df['variety'] == choise]
    return dfwine


def make_plot(dfwine):    
    dfwine["text_new"] = dfwine["description"].str.lower().str.replace(r'[^\w\s]+','', regex = True)
    new_df = dfwine.text_new.str.split(expand=True).stack().value_counts().reset_index()
    new_df.columns = ['Word', 'Frequency'] 
    df = new_df[new_df['Word'].map(len) > 3]
    df.iloc[0:10].plot.bar(x = 'Word', y = 'Frequency', title = 'Wich is the most used word?', ylabel = 'Frequency')
    plt.show()

df = choose_data(df, choise = "Merlot")
dfwine = make_plot(df)


dfwine_selection = pd.read_csv("/Users/marijkekalinowski/Desktop/SciPy/SciPy_Project/winemag_data_130k_v2.csv")
df_short = dfwine_selection[["country", "price","variety","points","province"]]
df_short = df_short.dropna()
df_country = df_short.groupby(["country"]).size()
df_country = df_country.to_frame()
df_country_counted = df_country.drop(df_country[df_country.iloc[:,0]<10].index)

df_price = df_short.groupby(["price"]).size()
df_points = df_short.groupby(["points"]).size()
df_variety = df_short.groupby(["variety"]).size()
df_variety = df_variety.to_frame()
df_variety_counted = df_variety.drop(df_variety[df_variety.iloc[:,0]<2000].index)
df_variety_list= df_variety_counted.reset_index()
df_variety_list = df_variety_list.drop(df_variety_list.columns[1], axis = 1)
variety = df_variety_list.values.tolist()
a = "Cabernet Sauvignon"
# def generate_plot(a): 
#     dfwinev = dfwine_selection.groupby(["variety","description"]).size()
#     dfwinev = dfwinev.groupby([a], ["description"]).size()
#     df_variety_list= df_variety_counted.reset_index()
#     df_variety_list = df_variety_list.drop(df_variety_list.columns[1], axis = 1)
    
#     return make_plot(dfwinev)

# generate_plot(a)

