import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Do certain words appear more often in the ratings than others? 
# Does this have anything to do with the characteristics of the wine?

def to_list(df, category, min_size):

    '''
    Converts specific dataframe to a list, wich will be used in dropdown menu     
    '''

    series = df.groupby([category]).size()
    df_size = series.to_frame()
    df_minsize = df_size.drop(df_size[df_size.iloc[:,0] < min_size].index)

    df_minsize = df_minsize.reset_index()
    df_minsize = df_minsize.drop(df_minsize.columns[1], axis = 1)

    my_list = df_minsize[category].tolist()
    return my_list


def choose_data(df, category, choice):

    '''
    Customises data set to choosen category  
    '''

    if category == "points":
        df = df.loc[(df[category] > choice[0]) & (df[category] < choice[1])] 
    else:
        df = df.loc[df[category] == choice]

    return df

def count_words(df):

    '''
    Counts the appearance of characteristic words in the descriptions
    '''
    # This will suppress a SettingWithCopyWarning entirely. For the porpuse of our project we ignore the warning
    pd.options.mode.chained_assignment = None

    # Creating a new column in the dataframe with all words in the description seperated to count them seperately
    df["text_new"] = df["description"].str.lower().str.replace(r'[^\w\s]+','', regex=True)
    df_tot_quants = df.text_new.str.split(expand=True).stack().value_counts().to_frame()
    df_tot_quants.columns = ["Frequency"]

    # New dataframe with specific flavours as indices to merge the counted words with that dataframe.
    # These flavours appear most often in the whole data set.
    df_flav_index = pd.DataFrame(index=["fruit", "acidity", "tannins", "cherry", "ripe", "spice", "rich", 
                                        "fresh", "berry", "plum", "soft", "apple", "blackberry", "sweet"])
    df_flav_quants = df_tot_quants.merge(df_flav_index, how='right', left_index=True, right_index=True)

    return df_flav_quants

def plot_word_freqs(df, category, choice):

    '''
    Plots the frequencies of the most used flavours for each country 
    '''

    df_chosen = choose_data(df, category, choice)
    df_freqs = count_words(df_chosen)

    df_freqs.plot.bar(ylabel='Frequency', figsize=(13, 6), fontsize=13)
    plt.title("Frequency of flavours mentioned by the taster considering", fontsize=18)
    plt.xlabel("Flavours", fontsize=15)
    plt.ylabel("Frequency", fontsize=15)

    plt.show()