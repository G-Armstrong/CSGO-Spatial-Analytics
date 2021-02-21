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
    
############################### VARIABLES ###############################
    single_round = data[(data['round'] == rnd) & (data['file'] == file)]
    
    ct_list, t_list = find_team_ids(file)
    
    array_player_vals = []
    
    for x in ct_list:
        array_player_vals.append([x])
        
    for y in t_list:
        array_player_vals.append([y])
        
    
    #add zeros
    for  player in array_player_vals:
        for i in range(25):
            player.append(0)
        player[16] = []
    
    first_dmg_counter = 20
    value = 5
    dup_ids_first = []
    
    last_row_id = 0
    
    
    ct_player_1 = []
    ct_player_2 = []
    ct_player_3 = []
    ct_player_4 = []
    ct_player_5 = []
    
    t_player_1 = []
    t_player_2 = []
    t_player_3 = []
    t_player_4 = []
    t_player_5 = []
    
    '''setup all players with id's and health'''
    
    
    dmg_pairs = []
    health_tracker = []
    kill_pairs = []
    last_5_row_kill_pairs = [[],[],[],[],[]]
    preplant_kills = []
    postplant_kills = []
    
    last_round_dmg_time = 0
    
    new_dmg_pair_flag = 1

############################### GAMES LOOP ###############################
    
############################### ROUNDS LOOP ###############################


############################### ROWS LOOP ###############################

    
    for index, row in single_round.iterrows():
        
          '''when a player dies in row do calucations then'''
          ''' pick 5=10 features to run throuhg kmeans first'''
          
#         print()
#         print()
#         print(kill_pairs)
#         print()
#         print()
#         #loop through EXISTING dmg_pairs and tally damages up to 100
#         #if tally adds up to 100 add to kill_pair
#         #consolodates dmg pairs
#         skip_me = 0
#         for pair in dmg_pairs:
#             if pair[2] >= 100:
#                 skip_me = 1
#                 kill_pairs.append(pair)
#                 last_5_row_kill_pairs[4] = pair.copy()
#                 dmg_pairs.remove(pair)
                
#                 for player in array_player_vals:
#                    # RIFLE_kill 5
#                    if player[0] == row['att_id'] and row['wp_type'] == 'Rifle':
#                        player[5] += 1
                       
#                    # SNIPER_kill 6
#                    if player[0] == row['att_id'] and row['wp_type'] == 'Sniper':
#                        player[6] += 1
                       
#                    # PISTOL_kill 7
#                    if player[0] == row['att_id'] and row['wp_type'] == 'Pistol' and row['round_type'] == 'NORMAL':
#                        player[7] += 1
                       
#                    # Grenade_used 11
#                    if player[0] == row['att_id'] and row['wp_type'] == 'Grenade':
#                        player[11] += 1
                
#             if pair[1] == row['vic_id'] and pair[0] == row['att_id']:
#                 pair[2] = pair[2] + row['hp_dmg']
#                 new_dmg_pair_flag = 0
                
                
#             #if dmg > 100
#             if pair[2] >= 100 and skip_me == 0:
#                 #teammate (row['att_id]) stole kill from pair[0]
#                 if row['att_id'] != pair[0]:
#                     #print(row['att_id'], "stole kill", pair[1])
#                     kill_pairs.append([row['att_id'], pair[1], 100, row['seconds'] - last_round_dmg_time])
#                     last_5_row_kill_pairs[4] = [row['att_id'], pair[1], 100]
#                     dmg_pairs.remove(pair) 
#                 #print(row['att_id'], row['wp_type'])
#                 for player in array_player_vals:
#                     # RIFLE_kill 5
#                     if player[0] == row['att_id'] and row['wp_type'] == 'Rifle':
#                         player[5] += 1
                        
#                     # SNIPER_kill 6
#                     if player[0] == row['att_id'] and row['wp_type'] == 'Sniper':
#                         player[6] += 1
                        
#                     # PISTOL_kill 7
#                     if player[0] == row['att_id'] and row['wp_type'] == 'Pistol' and row['round_type'] == 'NORMAL':
#                         player[7] += 1
                        
#                     # Grenade_used 11
#                     if player[0] == row['att_id'] and row['wp_type'] == 'Grenade':
#                         player[11] += 1
            
#             skip_me = 0
            
            
#         #Adds new pairs to dmg_pairs
#         if len(dmg_pairs) == 0 or new_dmg_pair_flag == 1:
#             dmg_pairs.append([row['att_id'], row['vic_id'], row['hp_dmg'], row['seconds'] - last_round_dmg_time])
                           
                

#         # First_kill 1
#         if first_dmg_counter != 0:
#             for player in array_player_vals:
#                 if player[0] == row['att_id'] and player[0] not in dup_ids_first:
#                     player[1] = value
#                     dup_ids_first.append(player[0])
#                     if len(dup_ids_first) % 2 == 0:
#                         value = value - 1
                    
#             first_dmg_counter = first_dmg_counter - 1
       
#         # SMG_kill 2
#         # SHOTGUN_kill 3
#         # MACHINEGUN_kill 4         
        
#         # TRADE_KILL 8
#         if len(last_5_row_kill_pairs) > 1:
#             for pair1 in last_5_row_kill_pairs:
#                 for pair2 in last_5_row_kill_pairs:
#                     #if neither are empty and if pair1[0] attacker is now dead (pair2[1]), give trade kill credit to attacker (pair2[0])
#                     if pair1 and pair2 and pair1[0] == pair2[1]:
#                         for player in array_player_vals:
#                             if pair2[0] == player[0]:
#                                 #print("trade kill found", pair1, pair2)
#                                 player[8] = player[8] + 1
#                                 #remove credit for orginal attacker (pair1)
#                                 index = last_5_row_kill_pairs.index(pair1)
#                                 last_5_row_kill_pairs[index].clear()
                            
#                                 # RIFLE_kill 5
#                                 if player[0] == row['att_id'] and row['wp_type'] == 'Rifle':
#                                     player[5] += 1
                                    
#                                 # SNIPER_kill 6
#                                 if player[0] == row['att_id'] and row['wp_type'] == 'Sniper':
#                                     player[6] += 1
                                    
#                                 # PISTOL_kill 7
#                                 if player[0] == row['att_id'] and row['wp_type'] == 'Pistol' and row['round_type'] == 'NORMAL':
#                                     player[7] += 1
                                    
#                                 # Grenade_used 11
#                                 if player[0] == row['att_id'] and row['wp_type'] == 'Grenade':
#                                     player[11] += 1
                                
#                                 break
#                         break
                
            
#         # SITE_KILL 9
                    
#         # Total_dmg 10
#         for player in array_player_vals:
#             if player[0] == row['att_id']:
#                 player[10] = player[10] + row['hp_dmg']
#                 break
            
#         # MID_KILL 12
            
#         # POST_PLANT_KILL 13 (part 1)
#         if len(kill_pairs) > 0:
#             for pair in kill_pairs:
#                 if pair and row['is_bomb_planted'] == True and pair not in postplant_kills and pair not in preplant_kills:
#                     #print(kill_pairs)
#                     #print()
#                     postplant_kills.append(pair)
                    
#         # ALONE_KILL *14 - check distance to nearst # of teammates and give a point if a certain distance away
#         # Distance_to_nearest_teammate (timegate)
#         # ALONE_DEATH *17
        
#         # PRE_PLANT_KILL 18 (part 1)
#         if len(kill_pairs) > 0:
#             for pair in kill_pairs:
#                 if pair and row['is_bomb_planted'] == False and pair not in preplant_kills:
#                     #print(kill_pairs)
#                     #print()
#                     preplant_kills.append(pair)
                
        
#         # Distance_to_bombsite 21
#         # Distance_to_last_known 22
#         # Distance_traveled 23
                    
# ################################ CLEAN UP ################################
#         #shift last 5 kill pairs 1
#         for i in range(5):
#             if i + 1 > 4:
#                 last_5_row_kill_pairs[i] = []
#                 break
#             else:
#                 last_5_row_kill_pairs[i] = last_5_row_kill_pairs[i+1]
                
#         new_dmg_pair_flag = 1
#         last_row_id = row['att_id']

        
# ######################### AFTER ROW LOOP PROCESSES #########################
# # check values we put in the arrays -- saves processing time/easier to do it here
#     for dead in kill_pairs:
#         for player in array_player_vals:
#             # VIC_FREQ 19
#             if dead and player[0] == dead[1]:
#                 player[19] = player[19] + 1
#             # ATT_FREQ 20
#             if dead and player[0] == dead[0]:
#                 player[20] = player[20] + 1
                
 
#     # PRE_PLANT_KILL 18 (part 2)
#     for pair in preplant_kills:
#         for player in array_player_vals:
#             if pair and player[0] == pair[0]:
#                 player[18] = player[18] + 1
                
 
#     # POST_PLANT_KILL 13 (part 2)
#     for pair in postplant_kills:
#         for player in array_player_vals:
#             if pair and player[0] == pair[0]:
#                 player[13] = player[13] + 1
    

#     # TIME_OF_KILLS (in array) 16
#     for pair in kill_pairs:
#         for player in array_player_vals:
#             if pair and player[0] == pair[0]:
#                 player[16].append(pair[3])
    
#     last_round_dmg_time = row['seconds']
#     #Total num of kills 24
#     #Track deaths 25
                
#     #Can give credit to asists here
#     #If a pair is still in damage pair, then that player did damage didn't get kill               
                
    
                
#     print(*array_player_vals, sep='\n')
    
# all_roles_in_round(data, "003218553373129179487_1555113029.dem", 4) 
    
    
    

# # # Make method to loop through entire game to determine which player fills what role (round to round)
# # # Make method to loop through entire game to determine which player fills what role (first half / second half)
# # # Make method to loop through entire game to determine which player fills what role (avg of all rounds
# # # (Later) Have AI learn from each role (guess best move for each role)
# # # Write point on map (Simple task)



