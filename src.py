# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:20:03 2020

@author: Grant
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import os
import pickle

class Writer:
    def __init__(self):
        self.data = pd.read_csv('./input/mm_master_demos.csv')
        self.analyzed_map = 'de_mirage' 
        
        # Filter by map & type of rounds, we don't want eco rounds as those tend to be more aggressive
        self.data = self.data[(self.data.map == self.analyzed_map) & (self.data.round_type == 'NORMAL')]
    
     # def total_data_entries(self):
     #     print('Total data Entries:' + len(self.data))
    # def number_of_gs_changes(self):   #returns the total number of game state changes with no doulicates
    #     ticks = []
    #     for row in self.data:
    #         if row.tick not in ticks:
    #             tick.append(row['tick'])
    #     return len(ticks)
    
    # def total_no_rnds(self):
    #     print()
    
    # def total_gametime(self): #returns the total duration of game state changes across the entire dataset
    #     unique_files = []
    #     seconds=[]
    #     for row in self.data:
    #         if row.file not in unique_files:
    #             unique_files.append(row.file)   #creates an array of all files with no duplicates
    #         print(unique_files)
    #         break
        
    #     for i in unique_files:
    #         for self.data[self.data['file']] == unique_files[i]:              #accessing all rows in 'data' with 'file' == unique_files[i]
    #             seconds.append(self.data['seconds'].iloc[counter])       #creates and array of 'seconds' values for one file at a time
    #         for j in range (len(seconds)-1):
    #             total = total + (seconds[j+1] - second[j])
    #             j = j + 1
    #     return total
    
    # def list_of_player_IDs(self):   #returns a list containing all player IDs with no duplicates
    #     player_IDs = []
    #     for row in self.data:
    #         if row['att_id'] not in player_IDS:
    #             player_IDs.append(row['att_id'])
    #         if row['vic_id'] not in player_IDs:
    #             player_IDs.append(row['vic_id'])
    #     return player_IDs     
       
    # #Averages
    
    # # average time step between game state changes
    # def avg_timestep(self): 
    #     return total_gametime(self.data) / number_of_gs_changes(self.data)
    
    #average distance to teammates 
    
    #Deviation 
    
    #Distributions output to Excel File comma separated value for various values (rnd len, )
    
    
    
    #returns the player ID of the player who attacks other players most frequently 
    def max_no_of_att(self):
        print()
    
    
    def get_data(self):
        #returns a deep copy of protected variable 'data'
        return self.data.copy()
    
    
    def main(self):
        mask = self.data[(self.data['bomb_site'] == 'A')]
        
        
        #list of all unique files (games)
        fn = mask['file'].tolist() #[file1 (0), file2 (1)]
        fn = list(set(fn))
        
        #make round number a list of lists and then refer to them by the index of the filenumber
        file_to_rounds = {} #{FN:RN}
        
        
        for index, row in mask.iterrows():   
            if (row['file'] in file_to_rounds):
                if (row['round'] in file_to_rounds[row['file']]):
                    continue
                else:
                    file_to_rounds[row['file']].append(row['round'])
                    
            else:
                file_to_rounds[row['file']] = [(row['round'])]
        
        
        #write file_to_rounds to file
        file = open('file_to_rounds.txt', 'wb')
        pickle.dump(file_to_rounds, file)
        file.close()
        
       