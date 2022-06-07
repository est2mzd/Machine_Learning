#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np

#===============================================================#
#===============================================================#
def get_color_list_01():
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple", \
              "tab:brown","tab:pink","tab:gray","tab:olive","tab:cyan"]
    return colors
#===============================================================#
#===============================================================#
def display_unique_values(df, col_names_of_string_value):
    for i, col_name in enumerate(col_names_of_string_value):
        print("--------------------------")
        unique_names = df[col_name].unique()
        output_name  = ""
        print("{}. [{}] : unique value num = {}".format(i, col_name, len(unique_names)))
        #
        for j, unique_name in enumerate(unique_names):
            if j == 0:
                output_name = unique_name
            else:
                output_name = output_name + ", " + unique_name
        print(output_name)
        print("\n")
#===============================================================#
#===============================================================#
def display_text_file(file_path_text, line_start, line_end):
    counter = 0
    #
    with open(file_path_text) as f:
        while True:
            counter +=1
            line = f.readline()
            #
            if(counter >= line_start) & (counter <= line_end):
                print(line[:-2])
            #
            if (not line) | (counter >= line_end):
                break
#===============================================================#
#===============================================================#
def plot_nan_ratio_each_column(df,title,figsize=(16,4),fontsize=14,bRemoveZeroNanData=False):
    # Calculate Nan Ratio
    ser_num_of_nan = df.isnull().sum(axis=0)
    ser_num_of_nan.sort_values(ascending=False, inplace=True)
    ser_num_of_nan = ser_num_of_nan / df.shape[0] * 100
    # Plot
    plt.rcParams["figure.figsize"] = figsize
    plt.rcParams["font.size"]      = fontsize
    fig = plt.figure()
    if bRemoveZeroNanData:
        non_zero_flag = ser_num_of_nan[ser_num_of_nan > 0]
        plt.bar(ser_num_of_nan[non_zero_flag].index, ser_num_of_nan[non_zero_flag].values)
    else:
        plt.bar(ser_num_of_nan.index, ser_num_of_nan.values)
    #
    plt.xticks(rotation=90)
    plt.title(title)
    plt.ylabel("%")
    plt.grid()
    return fig, ser_num_of_nan
    
#===============================================================#
#===============================================================#
def plot_nan_ratio_each_row(df,title,figsize=(16,4),fontsize=14,bRemoveZeroNanData=False):
    # Calculate Nan Ratio
    ser_num_of_nan = df.isnull().sum(axis=1)
    ser_num_of_nan.sort_values(ascending=False, inplace=True)
    ser_num_of_nan = ser_num_of_nan / df.shape[1] * 100
    # Plot
    plt.rcParams["figure.figsize"] = figsize
    plt.rcParams["font.size"]      = fontsize
    #
    fig = plt.figure()
    x_data = np.arange(df.shape[0]) / df.shape[0] * 100
    y_data = ser_num_of_nan.values
    plt.plot(x_data, y_data);
    plt.grid()
    plt.xlabel("Data Row ID normalized from 0 to 100 / row num = " + str(df.shape[0]))
    plt.ylabel("%")
    plt.title(title)
    return fig, ser_num_of_nan   
    
#===============================================================#
#===============================================================#   
def plot_summary(df,title,figsize=(16,4),fontsize=14,ids_to_plot = ['min', 'mean', 'max', 'std']):
    # Get Summary
    summary   = df.describe()
    #
    col_names = summary.columns
    colors    = get_color_list_01()
    num_plot  = len(ids_to_plot)
    #
    # Plot
    plt.rcParams["figure.figsize"] = figsize
    plt.rcParams["font.size"]      = fontsize
    fig = plt.figure();
    #----------------------------------
    for id in range(len(ids_to_plot)): 
        plt.plot(col_names, summary.loc[ids_to_plot[id], :],  colors[id]);
        plt.grid();
        plt.legend([ids_to_plot[id]]); 
    #
    plt.xticks(rotation=90)
    plt.legend(ids_to_plot)
    plt.title(title)
    plt.grid()
    return fig 
    
#===============================================================#
#===============================================================#
def list_union(list_1, list_2):
    # Wa 
    return set(list_1) | set(list_2)

def list_intersection(list_1, list_2):
    # Seki
    return set(list_1) & set(list_2)
    
def list_difference(list_1, list_2):
    # Seki
    return set(list_1) - set(list_2)  