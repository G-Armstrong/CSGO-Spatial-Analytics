# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:09:32 2021

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



#make empty df   
data = pd.DataFrame()

#gets copy of original data
data = writer.get_data()

#reading
with open('file_to_rounds.txt', 'rb') as handle:
    _input = handle.read()

#dictionary
file_to_rounds = pickle.loads(_input)

#get all player ids
def find_team_ids(file):
    list_of_ct_ids = []
    list_of_t_ids = []

    game_data = data[(data['file'] == file) & (data['round'] < 16) & (data['att_id'] != 0)]
    for index, row in game_data.iterrows():
        if row['att_side'] == "CounterTerrorist":
            if row['att_id'] not in list_of_ct_ids:
                list_of_ct_ids.append(row['att_id'])
            
        else:
            if row['att_id'] not in list_of_t_ids:
                list_of_t_ids.append(row['att_id'])
                
    return list_of_ct_ids, list_of_t_ids






# Make method to loop through single round to determine which player fills what role
def all_roles_in_round(df, file, rnd):
    single_round = data[(data['round'] == rnd) & (data['file'] == file)]
    
    ct_list, t_list = find_team_ids(file)
    
    array_player_vals = []
    
    for x in ct_list:
        array_player_vals.append([x])
        
    for y in t_list:
        array_player_vals.append([y])
        
    
    #add zeros
    for  player in array_player_vals:
        for i in range(22):
            player.append(0)
    
    
    first_dmg_counter = 20
    value = 5
    dup_ids_first = []
    last_row_rifler_id = 0
    last_row_sniper_id = 0
    last_row_pistol_id = 0
    
    dmg_pairs = []
    kill_pairs = []
    last_5_row_kill_pairs = [[],[],[],[],[]]
    new_dmg_pair_flag = 1
    
    
    for index, row in single_round.iterrows():
          #['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side',
          # 'vic_side','hp_dmg','arm_dmg','is_bomb_planted',
          #'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id',
          # 'att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
          # 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank']
          
          
        #tally dmg pairs
        if len(dmg_pairs) == 0:
            dmg_pairs.append([row['att_id'], row['vic_id'], row['hp_dmg']])
            
        for pair in dmg_pairs:
            if pair[0] == row['att_id'] and pair[1] == row['vic_id']:
                pair[2] = pair[2] + row['hp_dmg']
                new_dmg_pair_flag = 0
                
            
        if new_dmg_pair_flag == 1:
            dmg_pairs.append([row['att_id'], row['vic_id'], row['hp_dmg']])
        
        #check for kill pairs
        ''' TO DO
            check if victim was killed by 2 people (non solo kill), isoloate pair[1] and pair[2] over entire dmg list
            then add to last_5_row+kill pair ------- give credit to last player to dealt damage
        
        '''
        for pair in dmg_pairs:   
            if pair[2] >= 100:
                kill_pairs.append(pair)
                last_5_row_kill_pairs[4] = pair
                dmg_pairs.remove(pair)

        # First_kill
        if first_dmg_counter != 0:
            for player in array_player_vals:
                if player[0] == row['att_id'] and player[0] not in dup_ids_first:
                    player[1] = value
                    dup_ids_first.append(player[0])
                    if len(dup_ids_first) % 2 == 0:
                        value = value - 1
                    
            first_dmg_counter = first_dmg_counter - 1
       
        # SMG_kill
        # SHOTGUN_kill
        # MACHINEGUN_kill
        
        # RIFLE_kill
        for player in array_player_vals:
            if player[0] == row['att_id'] and row['wp_type'] == 'Rifle' and player[0] != last_row_rifler_id:
                player[4] += 1
                
        last_row_rifler_id = row['att_id']
            
        # SNIPER_kill
        for player in array_player_vals:
            if player[0] == row['att_id'] and row['wp_type'] == 'Sniper' and player[0] != last_row_sniper_id:
                player[5] += 1
                
        last_row_sniper_id = row['att_id']
        
        # PISTOL_kill
        if row['round_type'] == 'NORMAL':
            for player in array_player_vals:
                if player[0] == row['att_id'] and row['wp_type'] == 'Pistol' and player[0] != last_row_pistol_id:
                    player[6] += 1
                
        last_row_pistol_id = row['att_id']
        
        # TRADE_KILL
        ''' TO-DO
            change to only check in last 5 row kill pairs, cannot ref current row
        
        '''
        if len(last_5_row_kill_pairs) > 1:
            for pair in last_5_row_kill_pairs:
                #if not empty and if the current victim was an attacker
                if pair and [row['att_id'], row['vic_id'], 100] in last_5_row_kill_pairs and row['vic_id'] == pair[0]:
                    for player in array_player_vals:
                        if row['att_id'] == player[0]:
                            player[7] = player[7] + 1
                            index = last_5_row_kill_pairs.index(pair)
                            last_5_row_kill_pairs[index].clear()
                            print(last_5_row_kill_pairs)
                            break
                    break
                
            
        # SITE_KILL
        # Total_dmg
        # Grenade_used
        # MID_KILL
        # POST_PLANT_KILL
        # ALONE_KILL *
        # Distance_to_nearest_teammate (timegate) *
        # TIME_OF_KILL
        # ALONE_DEATH *
        # PRE_PLANT_KILL
        # VIC_FREQ
        # ATT_FREQ
        # Distance_to_bombsite
        # Distance_to_last_known
        # Distance_traveled
        
        #shift last 5 kill pairs 1
        for i in range(5):
            if i + 1 > 4:
                last_5_row_kill_pairs[i] = []
                break
            else:
                last_5_row_kill_pairs[i] = last_5_row_kill_pairs[i+1]
                
                
        new_dmg_pair_flag = 1
                
        print(last_5_row_kill_pairs)
        print()
    
    print(*array_player_vals, sep='\n')
    
all_roles_in_round(data, "003218553373129179487_1555113029.dem", 4) 
    
    
    
    
    
    
    
    
    
    

# # Make method to loop through entire game to determine which player fills what role (round to round)
# # Make method to loop through entire game to determine which player fills what role (first half / second half)
# # Make method to loop through entire game to determine which player fills what role (avg of all rounds
# # (Later) Have AI learn from each role (guess best move for each role)
# # Write point on map (Simple task)



