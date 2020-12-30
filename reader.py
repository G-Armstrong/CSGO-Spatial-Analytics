# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:34:59 2020

@author: Grant
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import os
import pickle
from src import Writer
writer = Writer()

#methods

# takes a fn as input and outputs all data for that file only 
#Inspiration: '003220156233449209995_1172535415.dem': [4] Why is this only printing one A attack? Need to see all rows from data associated with this file
# def search_by_file(file, _dict):
#    if (file in _dict):
#       output = data[(data['file'] == file)]
#       print(output.head(len(output)))
            
def write_data():
    writer.main()
    
def pointx_to_resolutionx(xinput,startX=-3217,endX=1912,resX=1024):
        sizeX=endX-startX
        if startX < 0:
            xinput += startX *(-1.0)
        else:
            xinput += startX
        xoutput = float((xinput / abs(sizeX)) * resX);
        return xoutput
    
def pointy_to_resolutiony(yinput,startY=-3401,endY=1682,resY=1024):
    sizeY=endY-startY
    if startY < 0:
        yinput += startY *(-1.0)
    else:
        yinput += startY
    youtput = float((yinput / abs(sizeY)) * resY);
    return resY-youtput
    
    
    
###############################################################################   

#make empty df   
data = pd.DataFrame()

#gets copy of original data
data = writer.get_data()


#code to run
#new data to write
#write_data()

#reading
with open('file_to_rounds.txt', 'rb') as handle:
    _input = handle.read()

#dictionary
file_to_rounds = pickle.loads(_input)

# print(len(file_to_rounds.keys()))
# total = 0
# for k,v in file_to_rounds.items():
#     total = total + len(v) 
# print(total / 352) #avg rounds per file


#search_by_file('003228534430448484583_1675258063.dem', file_to_rounds)  

#Array_of_Preplant_A = []
#Array_of_Postplant_A = []
r_total = 0
#T_Wins_Preplant = [] #Convert to dataFrame
#CT_Wins_Preplant = [] #convert to DataFreame

# T_Loses_Preplant = [] #Convert to dataFrame
# CT_Loses_Preplant = [] #convert to DataFreame

# T_Loses_Postplant = [] #Convert to dataFrame
# CT_Loses_Postplant = [] #convert to DataFreame

# T_Wins_Postplant = [] #Convert to dataFrame
# CT_Wins_Postplant = [] #convert to DataFreame

#number 6
T_Loses_Preplant_A_Vic = []
CT_Loses_Preplant_A_Vic = []

#number 7
T_Wins_Preplant_A_Vic = []
CT_Wins_Preplant_A_Vic = []

#number 8
T_Wins_Postplant_A_Vic = []
CT_Wins_Postplant_A_Vic = []

#number 9
T_Loses_Postplant_A_Vic = []
CT_Loses_Postplant_A_Vic = []


for k,v in file_to_rounds.items(): #taking a single round at a time and splitting by pre and post plant
    for rnd in v:
        #Array_of_Preplant_A.append(data[(data['bomb_site'] != 'A') & (data['bomb_site'] != 'B') & (data['round'] == rnd) & (data['file'] == k)])
        #Array_of_Postplant_A.append(data[(data['bomb_site'] == 'A') & (data['round'] == rnd) & (data['file'] == k)])
       
        # T_Wins_Preplant.append(data[(data['bomb_site'] != 'A') & (data['bomb_site'] != 'B') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'Terrorist') & (data['winner_side'] == 'Terrorist')].values.tolist())
        # CT_Wins_Preplant.append(data[(data['bomb_site'] != 'A') & (data['bomb_site'] != 'B') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'CounterTerrorist') & (data['winner_side'] == 'CounterTerrorist')].values.tolist())
        
        #number 3 in Spring 2021 project plan
        # T_Loses_Preplant.append(data[(data['bomb_site'] != 'A') & (data['bomb_site'] != 'B') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'Terrorist') & (data['winner_side'] == 'CounterTerrorist')].values.tolist())
        # CT_Loses_Preplant.append(data[(data['bomb_site'] != 'A') & (data['bomb_site'] != 'B') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'CounterTerrorist') & (data['winner_side'] == 'Terrorist')].values.tolist())

        #number 4 in Spring 2021 project plan
        # T_Loses_Postplant.append(data[(data['bomb_site'] == 'A')  & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'Terrorist') & (data['winner_side'] == 'CounterTerrorist')].values.tolist())
        # CT_Loses_Postplant.append(data[(data['bomb_site'] == 'A') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'CounterTerrorist') & (data['winner_side'] == 'Terrorist')].values.tolist())
        
        #number 5 in Spring 2021 project plan
        # T_Wins_Postplant.append(data[(data['bomb_site'] == 'A')  & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'Terrorist') & (data['winner_side'] == 'Terrorist')].values.tolist())
        # CT_Wins_Postplant.append(data[(data['bomb_site'] == 'A') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'CounterTerrorist') & (data['winner_side'] == 'CounterTerrorist')].values.tolist())       
        
        #number 6
        # T_Loses_Preplant_A_Vic.append(data[(data['bomb_site'] != 'A') & (data['bomb_site'] != 'B') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'CounterTerrorist') & (data['winner_side'] == 'CounterTerrorist')].values.tolist())
        # CT_Loses_Preplant_A_Vic.append(data[(data['bomb_site'] != 'A') & (data['bomb_site'] != 'B') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'Terrorist') & (data['winner_side'] == 'Terrorist')].values.tolist())
        
        # #number 7
        #T_Wins_Preplant_A_Vic.append(data[(data['bomb_site'] != 'A') & (data['bomb_site'] != 'B') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'CounterTerrorist') & (data['winner_side'] == 'Terrorist')].values.tolist())
        #CT_Wins_Preplant_A_Vic.append(data[(data['bomb_site'] != 'A') & (data['bomb_site'] != 'B') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'Terrorist') & (data['winner_side'] == 'CounterTerrorist')].values.tolist())
        
        # #number 8
        #T_Wins_Postplant_A_Vic.append(data[(data['bomb_site'] == 'A') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'CounterTerrorist') & (data['winner_side'] == 'Terrorist')].values.tolist())
        #CT_Wins_Postplant_A_Vic.append(data[(data['bomb_site'] == 'A') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'Terrorist') & (data['winner_side'] == 'CounterTerrorist')].values.tolist())
        
        # #number 9
        T_Loses_Postplant_A_Vic.append(data[(data['bomb_site'] == 'A') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'CounterTerrorist') & (data['winner_side'] == 'CounterTerrorist')].values.tolist())
        CT_Loses_Postplant_A_Vic.append(data[(data['bomb_site'] == 'A') & (data['round'] == rnd) & (data['file'] == k) & (data['att_side'] == 'Terrorist') & (data['winner_side'] == 'Terrorist')].values.tolist())

#remove empty lists
# t_remove_empties = [ele for ele in T_Wins_Preplant if ele != []]
# ct_remove_empties = [ele for ele in CT_Wins_Preplant if ele != []]

#number 3
# t_remove_empties = [ele for ele in T_Loses_Preplant if ele != []]
# ct_remove_empties = [ele for ele in CT_Loses_Preplant if ele != []]

#number 4
# t_remove_empties = [ele for ele in T_Loses_Postplant if ele != []]
# ct_remove_empties = [ele for ele in CT_Loses_Postplant if ele != []]

#number 5
# t_remove_empties = [ele for ele in T_Wins_Postplant if ele != []]
# ct_remove_empties = [ele for ele in CT_Wins_Postplant if ele != []]

#number 6
#t_remove_empties = [ele for ele in T_Loses_Preplant_A_Vic if ele != []]
#ct_remove_empties = [ele for ele in CT_Loses_Preplant_A_Vic if ele != []]

#number 7
#t_remove_empties = [ele for ele in T_Wins_Preplant_A_Vic if ele != []]
#ct_remove_empties = [ele for ele in CT_Wins_Preplant_A_Vic if ele != []]

# #number 8
#t_remove_empties = [ele for ele in T_Wins_Postplant_A_Vic if ele != []]
#ct_remove_empties = [ele for ele in CT_Wins_Postplant_A_Vic if ele != []]

# #number 9
t_remove_empties = [ele for ele in T_Loses_Postplant_A_Vic if ele != []]
ct_remove_empties = [ele for ele in CT_Loses_Postplant_A_Vic if ele != []]

#check if lists are the same
# t_remove_empties.sort() 
# ct_remove_empties.sort()
# print(t_remove_empties == ct_remove_empties)

#convert 3D array to 2D array
t_flat_list = [arr for sub_arrs in t_remove_empties for arr in sub_arrs]
ct_flat_list = [arr for sub_arrs in ct_remove_empties for arr in sub_arrs]

#make new dataframe from list (T_Wins_PrePlant)
# T_Wins_Preplant_A_df = pd.DataFrame(t_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

# CT_Wins_Preplant_A_df = pd.DataFrame(ct_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

#number 3
# T_Loses_Preplant_A_df = pd.DataFrame(t_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

# CT_Loses_Preplant_A_df = pd.DataFrame(ct_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

#number 4
# T_Loses_Postplant_A_df = pd.DataFrame(t_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

# CT_Loses_Postplant_A_df = pd.DataFrame(ct_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

#number 5
# T_Wins_Postplant_A_df = pd.DataFrame(t_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

# CT_Wins_Postplant_A_df = pd.DataFrame(ct_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

#number 6
#T_Loses_Preplant_A_Vic_df = pd.DataFrame(t_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

#CT_Loses_Preplant_A_Vic_df = pd.DataFrame(ct_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

#number 7
# T_Wins_Preplant_A_Vic_df = pd.DataFrame(t_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                               'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                  'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

# CT_Wins_Preplant_A_Vic_df = pd.DataFrame(ct_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                  'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                  'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

# #number 8
#T_Wins_Postplant_A_Vic_df = pd.DataFrame(t_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

#CT_Wins_Postplant_A_Vic_df = pd.DataFrame(ct_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

# #number 9
T_Loses_Postplant_A_Vic_df = pd.DataFrame(t_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
                                                                'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
                                                                'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

CT_Loses_Postplant_A_Vic_df = pd.DataFrame(ct_flat_list, columns =['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
                                                                'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
                                                                'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank'])

#Convert the data to radar positions
# T_Wins_Preplant_A_df['attacker_mapX'] = T_Wins_Preplant_A_df['att_pos_x'].apply(pointx_to_resolutionx)
# T_Wins_Preplant_A_df['attacker_mapY'] = T_Wins_Preplant_A_df['att_pos_y'].apply(pointy_to_resolutiony)
# T_Wins_Preplant_A_df['victim_mapX'] = T_Wins_Preplant_A_df['vic_pos_x'].apply(pointx_to_resolutionx)
# T_Wins_Preplant_A_df['victim_mapY'] = T_Wins_Preplant_A_df['vic_pos_y'].apply(pointy_to_resolutiony)

# CT_Wins_Preplant_A_df['attacker_mapX'] = CT_Wins_Preplant_A_df['att_pos_x'].apply(pointx_to_resolutionx)
# CT_Wins_Preplant_A_df['attacker_mapY'] = CT_Wins_Preplant_A_df['att_pos_y'].apply(pointy_to_resolutiony)
# CT_Wins_Preplant_A_df['victim_mapX'] = CT_Wins_Preplant_A_df['vic_pos_x'].apply(pointx_to_resolutionx)
# CT_Wins_Preplant_A_df['victim_mapY'] = CT_Wins_Preplant_A_df['vic_pos_y'].apply(pointy_to_resolutiony)

#number 3
# T_Loses_Preplant_A_df['attacker_mapX'] = T_Loses_Preplant_A_df['att_pos_x'].apply(pointx_to_resolutionx)
# T_Loses_Preplant_A_df['attacker_mapY'] = T_Loses_Preplant_A_df['att_pos_y'].apply(pointy_to_resolutiony)
# T_Loses_Preplant_A_df['victim_mapX'] = T_Loses_Preplant_A_df['vic_pos_x'].apply(pointx_to_resolutionx)
# T_Loses_Preplant_A_df['victim_mapY'] = T_Loses_Preplant_A_df['vic_pos_y'].apply(pointy_to_resolutiony)

# CT_Loses_Preplant_A_df['attacker_mapX'] = CT_Loses_Preplant_A_df['att_pos_x'].apply(pointx_to_resolutionx)
# CT_Loses_Preplant_A_df['attacker_mapY'] = CT_Loses_Preplant_A_df['att_pos_y'].apply(pointy_to_resolutiony)
# CT_Loses_Preplant_A_df['victim_mapX'] = CT_Loses_Preplant_A_df['vic_pos_x'].apply(pointx_to_resolutionx)
# CT_Loses_Preplant_A_df['victim_mapY'] = CT_Loses_Preplant_A_df['vic_pos_y'].apply(pointy_to_resolutiony)

# number 4
# T_Loses_Postplant_A_df['attacker_mapX'] = T_Loses_Postplant_A_df['att_pos_x'].apply(pointx_to_resolutionx)
# T_Loses_Postplant_A_df['attacker_mapY'] = T_Loses_Postplant_A_df['att_pos_y'].apply(pointy_to_resolutiony)
# T_Loses_Postplant_A_df['victim_mapX'] = T_Loses_Postplant_A_df['vic_pos_x'].apply(pointx_to_resolutionx)
# T_Loses_Postplant_A_df['victim_mapY'] = T_Loses_Postplant_A_df['vic_pos_y'].apply(pointy_to_resolutiony)

# CT_Loses_Postplant_A_df['attacker_mapX'] = CT_Loses_Postplant_A_df['att_pos_x'].apply(pointx_to_resolutionx)
# CT_Loses_Postplant_A_df['attacker_mapY'] = CT_Loses_Postplant_A_df['att_pos_y'].apply(pointy_to_resolutiony)
# CT_Loses_Postplant_A_df['victim_mapX'] = CT_Loses_Postplant_A_df['vic_pos_x'].apply(pointx_to_resolutionx)
# CT_Loses_Postplant_A_df['victim_mapY'] = CT_Loses_Postplant_A_df['vic_pos_y'].apply(pointy_to_resolutiony)

#number 5
# T_Wins_Postplant_A_df['attacker_mapX'] = T_Wins_Postplant_A_df['att_pos_x'].apply(pointx_to_resolutionx)
# T_Wins_Postplant_A_df['attacker_mapY'] = T_Wins_Postplant_A_df['att_pos_y'].apply(pointy_to_resolutiony)
# T_Wins_Postplant_A_df['victim_mapX'] = T_Wins_Postplant_A_df['vic_pos_x'].apply(pointx_to_resolutionx)
# T_Wins_Postplant_A_df['victim_mapY'] = T_Wins_Postplant_A_df['vic_pos_y'].apply(pointy_to_resolutiony)

# CT_Wins_Postplant_A_df['attacker_mapX'] = CT_Wins_Postplant_A_df['att_pos_x'].apply(pointx_to_resolutionx)
# CT_Wins_Postplant_A_df['attacker_mapY'] = CT_Wins_Postplant_A_df['att_pos_y'].apply(pointy_to_resolutiony)
# CT_Wins_Postplant_A_df['victim_mapX'] = CT_Wins_Postplant_A_df['vic_pos_x'].apply(pointx_to_resolutionx)
# CT_Wins_Postplant_A_df['victim_mapY'] = CT_Wins_Postplant_A_df['vic_pos_y'].apply(pointy_to_resolutiony)

#number 6
# T_Loses_Preplant_A_Vic_df['attacker_mapX'] = T_Loses_Preplant_A_Vic_df['att_pos_x'].apply(pointx_to_resolutionx)
# T_Loses_Preplant_A_Vic_df['attacker_mapY'] = T_Loses_Preplant_A_Vic_df['att_pos_y'].apply(pointy_to_resolutiony)
# T_Loses_Preplant_A_Vic_df['victim_mapX'] = T_Loses_Preplant_A_Vic_df['vic_pos_x'].apply(pointx_to_resolutionx)
# T_Loses_Preplant_A_Vic_df['victim_mapY'] = T_Loses_Preplant_A_Vic_df['vic_pos_y'].apply(pointy_to_resolutiony)

# CT_Loses_Preplant_A_Vic_df['attacker_mapX'] = CT_Loses_Preplant_A_Vic_df['att_pos_x'].apply(pointx_to_resolutionx)
# CT_Loses_Preplant_A_Vic_df['attacker_mapY'] = CT_Loses_Preplant_A_Vic_df['att_pos_y'].apply(pointy_to_resolutiony)
# CT_Loses_Preplant_A_Vic_df['victim_mapX'] = CT_Loses_Preplant_A_Vic_df['vic_pos_x'].apply(pointx_to_resolutionx)
# CT_Loses_Preplant_A_Vic_df['victim_mapY'] = CT_Loses_Preplant_A_Vic_df['vic_pos_y'].apply(pointy_to_resolutiony)

#number 7
# T_Wins_Preplant_A_Vic_df['attacker_mapX'] = T_Wins_Preplant_A_Vic_df['att_pos_x'].apply(pointx_to_resolutionx)
# T_Wins_Preplant_A_Vic_df['attacker_mapY'] = T_Wins_Preplant_A_Vic_df['att_pos_y'].apply(pointy_to_resolutiony)
# T_Wins_Preplant_A_Vic_df['victim_mapX'] = T_Wins_Preplant_A_Vic_df['vic_pos_x'].apply(pointx_to_resolutionx)
# T_Wins_Preplant_A_Vic_df['victim_mapY'] = T_Wins_Preplant_A_Vic_df['vic_pos_y'].apply(pointy_to_resolutiony)

# CT_Wins_Preplant_A_Vic_df['attacker_mapX'] = CT_Wins_Preplant_A_Vic_df['att_pos_x'].apply(pointx_to_resolutionx)
# CT_Wins_Preplant_A_Vic_df['attacker_mapY'] = CT_Wins_Preplant_A_Vic_df['att_pos_y'].apply(pointy_to_resolutiony)
# CT_Wins_Preplant_A_Vic_df['victim_mapX'] = CT_Wins_Preplant_A_Vic_df['vic_pos_x'].apply(pointx_to_resolutionx)
# CT_Wins_Preplant_A_Vic_df['victim_mapY'] = CT_Wins_Preplant_A_Vic_df['vic_pos_y'].apply(pointy_to_resolutiony)

# #number 8
# T_Wins_Postplant_A_Vic_df['attacker_mapX'] = T_Wins_Postplant_A_Vic_df['att_pos_x'].apply(pointx_to_resolutionx)
# T_Wins_Postplant_A_Vic_df['attacker_mapY'] = T_Wins_Postplant_A_Vic_df['att_pos_y'].apply(pointy_to_resolutiony)
# T_Wins_Postplant_A_Vic_df['victim_mapX'] = T_Wins_Postplant_A_Vic_df['vic_pos_x'].apply(pointx_to_resolutionx)
# T_Wins_Postplant_A_Vic_df['victim_mapY'] = T_Wins_Postplant_A_Vic_df['vic_pos_y'].apply(pointy_to_resolutiony)

# CT_Wins_Postplant_A_Vic_df['attacker_mapX'] = CT_Wins_Postplant_A_Vic_df['att_pos_x'].apply(pointx_to_resolutionx)
# CT_Wins_Postplant_A_Vic_df['attacker_mapY'] = CT_Wins_Postplant_A_Vic_df['att_pos_y'].apply(pointy_to_resolutiony)
# CT_Wins_Postplant_A_Vic_df['victim_mapX'] = CT_Wins_Postplant_A_Vic_df['vic_pos_x'].apply(pointx_to_resolutionx)
# CT_Wins_Postplant_A_Vic_df['victim_mapY'] = CT_Wins_Postplant_A_Vic_df['vic_pos_y'].apply(pointy_to_resolutiony)

# #number 9
T_Loses_Postplant_A_Vic_df['attacker_mapX'] = T_Loses_Postplant_A_Vic_df['att_pos_x'].apply(pointx_to_resolutionx)
T_Loses_Postplant_A_Vic_df['attacker_mapY'] = T_Loses_Postplant_A_Vic_df['att_pos_y'].apply(pointy_to_resolutiony)
T_Loses_Postplant_A_Vic_df['victim_mapX'] = T_Loses_Postplant_A_Vic_df['vic_pos_x'].apply(pointx_to_resolutionx)
T_Loses_Postplant_A_Vic_df['victim_mapY'] = T_Loses_Postplant_A_Vic_df['vic_pos_y'].apply(pointy_to_resolutiony)

CT_Loses_Postplant_A_Vic_df['attacker_mapX'] = CT_Loses_Postplant_A_Vic_df['att_pos_x'].apply(pointx_to_resolutionx)
CT_Loses_Postplant_A_Vic_df['attacker_mapY'] = CT_Loses_Postplant_A_Vic_df['att_pos_y'].apply(pointy_to_resolutiony)
CT_Loses_Postplant_A_Vic_df['victim_mapX'] = CT_Loses_Postplant_A_Vic_df['vic_pos_x'].apply(pointx_to_resolutionx)
CT_Loses_Postplant_A_Vic_df['victim_mapY'] = CT_Loses_Postplant_A_Vic_df['vic_pos_y'].apply(pointy_to_resolutiony)
    
# # Heat map
im = plt.imread('./input/de_mirage.png')

plt.figure(figsize=(20,20))

t = plt.imshow(im)
ct = plt.imshow(im)

#t = plt.scatter(T_Loses_Preplant_A_Vic_df['attacker_mapX'], T_Loses_Preplant_A_Vic_df['attacker_mapY'],alpha=0.04,c='orange')
#ct = plt.scatter(CT_Loses_Preplant_A_Vic_df['attacker_mapX'], CT_Loses_Preplant_A_Vic_df['attacker_mapY'],alpha=0.04,c='blue')

#t = plt.scatter(T_Loses_Postplant_A_Vic_df['victim_mapX'], T_Loses_Postplant_A_Vic_df['victim_mapY'],alpha=0.04,c='orange')
ct = plt.scatter(CT_Loses_Postplant_A_Vic_df['victim_mapX'], CT_Loses_Postplant_A_Vic_df['victim_mapY'],alpha=0.04,c='blue')
