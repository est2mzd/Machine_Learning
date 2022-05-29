#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt

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