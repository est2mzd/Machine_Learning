#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt

def convert_dict_md_to_csv(file_path_dictionary):
    # Read File
    # e.g. file_path_dictionary = 'Data_Dictionary.md'
    file_obj = open(file_path_dictionary, 'r')
    buf      = file_obj.read()
    file_obj.close()

    # String -> List
    text_data = buf.split('\n')

    # Get Name & Explanation
    flag_find_key    = 0
    tmp_name_list    = []
    name_list        = []
    explanation_list = []
    id_1_list        = []
    id_2_list        = []
    id_3_list        = []
    #-----------------------------------------------
    for line in text_data:
        # Ignore "Table of Contents"
        if line.find("Table of Contents") > -1:
            continue
        
        # Find Key Word
        pos_find = line.find("###")
        
        #------------------------------------------
        # get name of columns
        if pos_find >= 0:
            # remove ","
            line = line.replace("," , "")
            
            # translate multi-space to single-space
            for i in range(5):
                line = line.replace("  ", " ")
            
            # split line by space       
            flag_find_key += 1
            line_split     = line.split(" ")
            
            # save names as list
            if flag_find_key == 1:
                tmp_id_1  = line_split[1][0:-1]
                tmp_id_2  = tmp_id_1.split(".")
                data_id_1 = tmp_id_2[0]
                #
                if len(tmp_id_2) == 1:
                    data_id_2 = "0"
                else:
                    data_id_2 = tmp_id_2[1]
                #
                tmp_name_list.extend(line_split[2:])
            else:
                tmp_name_list.extend(line_split[1:])
                
        #------------------------------------------
        # get explanations of columns
        if (pos_find == -1) and (flag_find_key > 0):
            # save data as list 
            for name in tmp_name_list:
                name_list.append(name)
                explanation_list.append(line)
                id_1_list.append(data_id_1)
                id_2_list.append(data_id_2)
                #
                data_id_3 = str( int(data_id_1)*100 + int(data_id_2) )
                id_3_list.append(data_id_3)
                
            # initilize
            flag_find_key = 0
            tmp_name_list      = []
            
    # Write to Text File
    # e.g. file_path_csv = 'Data_Dictionary.csv'
    file_path_csv = file_path_dictionary.replace(".md", ".csv")
    with open(file_path_csv, 'w') as file_obj:
        cnt = 0
        # write header
        file_obj.write("id_1" + "\t" + "id_2" + "\t" + "id_3" + "\t" + "attribute" + "\t" + "explanation" + "\n")
        #
        for name, explanation, id_1, id_2, id_3 in zip(name_list, explanation_list, id_1_list, id_2_list, id_3_list):
            cnt +=1
            if cnt < len(name_list):
                file_obj.write(id_1 + "\t" + id_2 + "\t" + id_3 + "\t" + name + "\t" + explanation + "\n")
            else:
                file_obj.write(id_1 + "\t" + id_2 + "\t" + id_3 + "\t" + name + "\t" + explanation)        

#===============================================================#                
#===============================================================#
def plot_summary( df, xlim=[[],[],[],[],[],[],[]], ylim=[[],[],[],[],[],[],[]]):
    print("================================")
    print('X-Axis is the ID of columns.')
    print('Y-Axis is the value of columns.')
    print("================================")
    plt.rcParams['figure.figsize'] = (16,8);
    plt.subplots_adjust(top=4);
    plt.rcParams['font.size']      = 14;
    #
    x_data      = list(range(df.shape[0]))
    y_list      = ['min', 'mean', 'max', 'std', '25%', '50%', '75%']
    y_data_min  = df['min']
    y_data_mean = df['mean']
    y_data_max  = df['max']
    y_data_std  = df['std']
    colorlist   = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#a65628', '#f781bf', '#ffff33']
    #
    plt.figure();
    #----------------------------------
    for id in range(len(y_list)): 
        plt.subplot(2,4,id+1);
        plt.plot(x_data, df[y_list[id]],  colorlist[id]);
        plt.grid();
        plt.legend([y_list[id]]);

        if len(xlim[id]) >= 2:
            plt.xlim(xlim[id]);
        #
        if len(ylim[id]) >= 2:
            plt.ylim(ylim[id]);

#===============================================================#
#===============================================================#
