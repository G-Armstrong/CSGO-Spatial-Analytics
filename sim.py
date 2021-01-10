import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import os
import pickle
from src import Writer
writer = Writer()

""" 
TO-DO:
get a single player in a single round x10
check unqiue att_id/vic_id (sanity)
Follow att_id for 1 side on a single round, should disappear on round end or death
"""

#make empty df   
data = pd.DataFrame()

#gets copy of original data
data = writer.get_data()

#reading
with open('file_to_rounds.txt', 'rb') as handle:
    _input = handle.read()

sim_round_one = []

#dictionary
file_to_rounds = pickle.loads(_input)

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

#returns two arrays of victims and attackers in one game from one round
#find a round where A is attacked
#find a file that contains the most lines of captured data 
def find_players(file, rnd):
    sim_round_one = (data[(data['round'] == rnd) & (data['file'] == file)].values.tolist())

    #make sure there are <= 10 att_id's
    #attid = 21, vic_id = 23
    att_id_list = []
    vic_id_list = []

    for aids in sim_round_one:
        att_id_list.append(aids[21])
        vic_id_list.append(aids[23])
    
    filtered_att_id_list = list(set(att_id_list))
    filtered_vic_id_list = list(set(vic_id_list))
    
    return filtered_att_id_list,filtered_vic_id_list

#track 1 player through round
def track_player(player_id, file, rnd, attacking):
    if attacking == True:
        single_round = data[(data['round'] == rnd) & (data['file'] == file) & (data['att_id'] == player_id)]
        
    else:
        single_round = data[(data['round'] == rnd) & (data['file'] == file) & (data['vic_id'] == player_id)]
    
    return single_round

def find_team_ids(file):
    #['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id',
#                                                                 'att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank']
    list_of_ct_ids = []
    list_of_t_ids = []

    game_data = data[(data['file'] == file) & (data['round'] < 16) & (data['att_id'] != 0)]
    for index, row in game_data.iterrows():
        if row['att_side'] == "CounterTerrorist":
            print(row['att_id'])
            if row['att_id'] not in list_of_ct_ids:
                list_of_ct_ids.append(row['att_id'])
            
        else:
            if row['att_id'] not in list_of_t_ids:
                list_of_t_ids.append(row['att_id'])
                
    return list_of_ct_ids, list_of_t_ids

#track 1 player through round
# def produce_maps_for_team(df, team):
#     df_copy = df.copy()
    
#     if team == "CT":
#         df_copy['attacker_mapX'] = df_copy['att_pos_x'].apply(pointx_to_resolutionx)
#         df_copy['attacker_mapY'] = df_copy['att_pos_y'].apply(pointy_to_resolutiony)

#     else:


def produce_maps_from_list(df, attacking):
    df_copy = df.copy()
    if attacking == True:
            df_copy['attacker_mapX'] = df_copy['att_pos_x'].apply(pointx_to_resolutionx)
            df_copy['attacker_mapY'] = df_copy['att_pos_y'].apply(pointy_to_resolutiony)
    
    else:
            df_copy['victim_mapX'] = df_copy['vic_pos_x'].apply(pointx_to_resolutionx)
            df_copy['victim_mapY'] = df_copy['vic_pos_y'].apply(pointy_to_resolutiony)
    
    # # Heat map
    im = plt.imread('./input/de_mirage.png')
    
    for index, row in df_copy.iterrows():
        plt.figure(figsize=(20,20))

        new_plt = plt.imshow(im)
        
        if attacking == True:
            new_plt = plt.scatter(row['attacker_mapX'], row['attacker_mapY'],alpha=1,c='blue')
        
        else:
            new_plt = plt.scatter(row['victim_mapX'], row['victim_mapY'],alpha=0.04,c='orange')
        
    

att_list, vic_list = find_players("003218553373129179487_1555113029.dem", 4)

single_round_df = track_player(76561198152153688, "003218553373129179487_1555113029.dem", 4, True)

#produce_maps_from_list(single_round_df, True)

ct_ids, t_ids = find_team_ids("003218553373129179487_1555113029.dem")

print(ct_ids)
print()
print(t_ids)

#save maps to folder in addition to printing 


