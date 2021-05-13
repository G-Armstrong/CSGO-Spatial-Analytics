# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:42:12 2021

@author: Grant
"""

import numpy as np
import pandas as pd

#get player_df from csv
imported_df = pd.read_csv('keep_me_df.csv')
main_df = pd.read_csv('doNOTdelete.csv')

#every 5 players is a team and every 10 is game
#need to add back dropped / or delete their teams

temp = []
for index, row in imported_df.iterrows():
    try: 
        if row['Role'] in [0.0, 1.0, 2.0, 3.0, 4.0]:
            temp.append([int(row['id']), int(row['Role'])])
    except:
        continue
        
print("temp length", len(temp))

main_df['Role'] = ""
random_var = 0
found_pair = False
for index, row in main_df.iterrows():
    found_pair = False
    for x in temp:
        if int(row['ID']) == int(x[0]) and found_pair == False:
            print(row['ID'], int(x[0]))
            main_df.at[index,'Role'] = x[1]
            random_var += 1
            found_pair = True

       
# print(main_df.index)
print("assigned labels (256)", random_var)
print("# of labeled rows", len(main_df[main_df['Role'] != ""]['Role']))
#main_df.to_csv('players_df.csv', index = False, encoding='utf-8')