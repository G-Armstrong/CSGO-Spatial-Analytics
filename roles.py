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

#main df
column_names = ['ID','Health','damage','kills','rifle','sniper','pistol','smg','grenade','preplant kill','postplant kill','fast_kill_rating (first_kill)','time of kills','total kills','total deaths', 'avg kill time', 'assists']
main_df = pd.DataFrame(columns = column_names)


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
def all_roles_in_round(df, file): 
    
############################### VARIABLES ###############################
    ct_list, t_list = find_team_ids(file)

    print("ct", ct_list)
    print("t", t_list)
    
    if len(ct_list) < 5:
        print("CT LIST TOO SMALL:", len(ct_list))
        print("Skipping")
        return
        
    if len(t_list) < 5:
        print("T LIST TOO SMALL:", len(t_list))
        print("Skipping")
        return
        
    # array_player_vals = []
    
    # for x in ct_list:
    #     array_player_vals.append([x])
        
    # for y in t_list:
    #     array_player_vals.append([y])
        
    
    # #add zeros
    # for  player in array_player_vals:
    #     for i in range(25):
    #         player.append(0)
    #     player[16] = []
    
    
    # value = 5
    # dup_ids_first = []
    
    # last_row_id = 0
    # dmg_pairs = []
    # health_tracker = []
    # kill_pairs = []
    # last_5_row_kill_pairs = [[],[],[],[],[]]
    # preplant_kills = []
    # postplant_kills = []
    
    # last_round_dmg_time = 0
    
    # new_dmg_pair_flag = 1
    ''' NOTES '''
    #May need to do average for Fast kill rating
    #test flag check for testing single round and single game (easy)
    #check id 2366 lol
    #check for tks
   
    
    
    ''' GAME VARIABLES '''
    #ID, Health, damage, kills, rifle, sniper, pistol, smg, grenade, preplant kill, postplant kill, fast_kill_rating (first_kill), time of kills, total kills, total deaths, avg kill time, assists
    ct_player_1 = [ct_list[0], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    ct_player_2 = [ct_list[1], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    ct_player_3 = [ct_list[2], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    ct_player_4 = [ct_list[3], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    ct_player_5 = [ct_list[4], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    
    t_player_1 = [t_list[0], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    t_player_2 = [t_list[1], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    t_player_3 = [t_list[2], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    t_player_4 = [t_list[3], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    t_player_5 = [t_list[4], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0]
    
    
    
    all_players = [ct_player_1, ct_player_2, ct_player_3, ct_player_4, ct_player_5, 
                   t_player_1, t_player_2, t_player_3, t_player_4, t_player_5]
        
    
    ''' ROUNDS LOOP '''
    
    single_game = data[(data['file'] == file)]
    highest_round = single_game.loc[single_game['round'].idxmax()]
    print("Running file", file,"with max round", highest_round['round'], "...")
    for i in range(1, highest_round['round'] + 1):
        
        #reset health at beginning of round
        for player in all_players:
            player[1] = 100

        
        ''' ROUND VARIABLES '''
        first_dmg_turn_counter = 20
        first_dmg_award = [1,1,2,2,3,3,4,4,5,5]
        first_dmg_index = len(first_dmg_award) - 1
        assists = []
        
        ''' ROWS LOOP '''
        print("Running round", i,"...")
        single_round = data[(data['round'] == i) & (data['file'] == file)]
        for index, row in single_round.iterrows():
            '''when a player dies in row do calucations then'''
            for victim in all_players:
                if victim[0] == row['vic_id']:
                    victim[1] -= row['hp_dmg']
                    for attacker in all_players:
                        if attacker[0] == row['att_id']:
                            attacker[2] += row['hp_dmg']
                            #if a attacker does damage give him an assist,
                            if ([attacker[0], victim[0]]) not in assists:
                                assists.append([attacker[0], victim[0]])
                            if victim[1] <= 0:
                                
                                #remove assist from list when they kill
                                assists.remove([attacker[0], victim[0]])
                                attacker[3] += 1
                                if row['wp_type'] == 'Rifle':
                                    attacker[4] += 1
                                if row['wp_type'] == 'Sniper':
                                    attacker[5] += 1
                                if row['wp_type'] == 'Pistol':
                                    attacker[6] += 1
                                if row['wp_type'] == 'SMG':
                                    attacker[7] += 1
                                if row['wp_type'] == 'Grenade':
                                    attacker[8] += 1
                                if row['is_bomb_planted'] != True:
                                    attacker[9] += 1
                                if row['is_bomb_planted'] == True:
                                    attacker[10] += 1
                                if first_dmg_turn_counter > 0 and attacker[11] == 0 and first_dmg_index >= 0:
                                    attacker[11] = first_dmg_award[first_dmg_index]
                                    first_dmg_index -= 1
                                attacker[12].append(row['seconds'])
                                attacker[13] += 1
                                victim[14] += 1

        ''' POST ROUND CHECKS '''
        for player in all_players:
            
            if player[0] == 76561198152153688:
                print("76561198152153688 kills:", player[3])
            
            time_delta = 0
            #assists checks
            if len(assists) > 0:
                for assist_pair in assists:
                    if assist_pair[0] == player[0]:
                        player[16] += 1
                        assists.remove(assist_pair)
                        
            if player[12] and len(player[12]) > 1:
                for i in range(len(player[12])):
                    if (i + 1) < (len(player[12])):
                        time_delta += player[12][i+1] - player[12][i]
                    else:
                        #will get more accurate each round and harder to change
                        player[15] = time_delta/(len(player[12]) - 1)

            ''' POST ROUND VARIABLE CHANGES '''
            first_dmg_turn_counter -= 1
                        
        
                
    players_df = pd.DataFrame(all_players)
    players_df.columns = column_names
    return players_df
    
    
all_files = data.file.unique()
index = 0

for f in all_files:
    if index == 5:
        break
    round_df = all_roles_in_round(data, f)
    print('--------------------------------------')
    main_df = main_df.append(round_df, ignore_index = True)
    index += 1

main_df = main_df.drop(['time of kills', 'Health'], axis=1)
pd.set_option("display.max_rows", None, "display.max_columns", None, 'expand_frame_repr', False)

print(main_df)
    
#save to csv
main_df.to_csv('players_df.csv', index = False, encoding='utf-8')
    
    
    
    
    
    
    
    
    
    
    
    
    
          
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



