import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# Do appraisers tend to specialize in one or two provinces? Do they specialize in certain varieties? 
def plot_taster_spec(df):

    def to_percentages(tot_vals, spec_vals):
        
        '''
        Converts a series containing specific values into a series with percentages in order to compare values
        '''
        
        # double loop to go through each values for each taster
        for ix_tot, val_tot in tot_vals.items():
            for ix_spec, val_spec in spec_vals.loc[ix_tot].items():
                spec_vals.loc[ix_tot, ix_spec] = round(val_spec / val_tot * 100, 2)
                    
        return spec_vals

    # Series of all tasters with total number of tastings in which they have participated
    taster_tot = df.groupby(["taster_name"]).size()

    # Appraisers and provinces

    # filtering out the three provinces per taster in which they have done the most tastings  
    taster_prov = df.groupby(["taster_name", "province"]).size()
    taster_largest_prov = taster_prov.groupby(level="taster_name").nlargest(3).reset_index(level=0, drop=True)

    # calculating percentages of those participations (but still considering all other participations)
    taster_largest_prov = to_percentages(taster_tot, taster_largest_prov).to_frame()

    # Appraisers and varieties

    # filtering out the three varieties per taster with which they have done the most tastings
    taster_var = df.groupby(["taster_name", "variety"]).size()
    taster_largest_var = taster_var.groupby(level="taster_name").nlargest(3).reset_index(level=0, drop=True)

    # calculating percentages
    taster_largest_var = to_percentages(taster_tot, taster_largest_var).to_frame()

    tasters = []

    # inserting all taster names into an array
    for taster_name, total in taster_tot.items():
        tasters.append(taster_name)

    def best_three_arrays(tot_vals, spec_vals):
        
        ''' 
        Returns three arrays, one for the highest participation in provinces / regions (first), one for the second highest (second) 
        and one for the third highest (third).
        
        Takes a Series (to get first indices of Multiindex Dataframe) and a Dataframe which is to be split up.
        '''
        
        first = []
        second = []
        third = []
        
        # double loop to go through each (max) three values for each taster
        for ix_tot, val_tot in tot_vals.items():
            for ix_spec, val_spec in spec_vals.loc[ix_tot].items():
                arr = val_spec.to_numpy()
                try:
                    first.append(arr[0])

                except:
                    first.append(0)
                try:

                    second.append(arr[1])
                except:

                    second.append(0)
                try:
                    third.append(arr[2])
                except:

                    third.append(0)
                    
        return (first, second, third)

    def sort_arrays(first, second, third, fourth):
        
        ''' 
        Returns sorted version of four arrays from lowest to highest percentage of participations regarding the array with
        most participations (first)
        '''
        sort_array = np.argsort(first)
        
        first = np.array(first)[sort_array]
        second = np.array(second)[sort_array]
        third = np.array(third)[sort_array]
        fourth = np.array(fourth)[sort_array]
        
        return (first, second, third, fourth)

    best_three_prov = best_three_arrays(taster_tot, taster_largest_prov)
    best_three_var = best_three_arrays(taster_tot, taster_largest_var)

    bars_provinces = sort_arrays(best_three_prov[0], best_three_prov[1], best_three_prov[2], tasters)
    bars_varieties = sort_arrays(best_three_var[0], best_three_var[1], best_three_var[2], tasters)

    # x axis steps
    x_steps = np.arange(len(tasters))

    # plot for provinces 

    # defining figure size 
    figure(figsize=(20, 8), dpi=80)

    # plotting each bars for first, second and third
    plt.bar(x_steps - 0.2, bars_provinces[0], 0.2, label="First")
    plt.bar(x_steps + 0, bars_provinces[1], 0.2, label="Second")
    plt.bar(x_steps + 0.2, bars_provinces[2], 0.2, label="Third")

    # defining labels
    plt.xticks(x_steps, bars_provinces[2], rotation=90, fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel("Tasters", fontsize=18)
    plt.ylabel("Percentage of province participation", fontsize=18)
    plt.title("Participation of each taster for their three most visited provinces", fontsize=20)

    plt.legend()
    plt.show()

    # plot for varieties 

    # defining figure size 
    figure(figsize=(20, 8), dpi=80)

    # plotting each bars for first, second and third
    plt.bar(x_steps - 0.2, bars_varieties[0], 0.2, label="First")
    plt.bar(x_steps + 0, bars_varieties[1], 0.2, label="Second")
    plt.bar(x_steps + 0.2, bars_varieties[2], 0.2, label="Third")

    # defining labels
    plt.xticks(x_steps, bars_varieties[3], rotation=90, fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel("Tasters", fontsize=18)
    plt.ylabel("Variety participation", fontsize=18) 
    plt.title("Participation of each taster for their most tasted varieties of wines", fontsize=20)

    plt.legend()
    plt.show()