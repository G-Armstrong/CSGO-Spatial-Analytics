# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:09:32 2021

Make method to loop through single round to determine which player fills what role
create train set size vs accuracy graph

The General Making Choices Approach

####Raymond To-Do####
TRADE_KILL                       

Distance_traveled

####Grant To-Do####
ALONE_DEATH

####PreGame##### Making use of Clustering 

Finish clustering with new features, classify test set into clusters, make a new column for cluster
Determine success and faiulure statistics for team comp matchups (Team Gamma vs Team Omega)
    - 11111 vs 01342
    - Who is 11111's best and worst matchup
Determine which individual team comp is the most winningest -
    - 11111 win rate alone
Win percentage of team comp before and after switch
    - How does 11111 do on T vs CT?
If matchup between team is bad, AI system could recommend different comp

Do individual players occupy different clusters?
Check if individual players occur in different games?  



####MidGame/Post-Plant Applied Statistics#####

Within +-5 seconds of A site bomb plant determine where T players are playing (boxes) regardless of the round outcome
Look at their team comp-> is it a succeessful team comp? Or do they lose bc of the wrong combination of players and match up. 
Do they play in the positions we think are supposed to succeed based off heat maps or statistics of successful box loactions for individual player types, their clusters? Or do they succeed from new postions? How is the team spread spatially?
    We can extract spatial features of player sot one another and bombsite and perform statistics on what wins

# # # (Later) Have AI learn from each role (guess best move for each role)

@author: Grant
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
import os
import pickle
from src import Writer
import sim as sim
writer = Writer()

#make empty df   
data = pd.DataFrame()

#iterations = 245
iterations = 245

#gets copy of original data\
writer.main()
data = writer.get_data()

#reading
with open('file_to_rounds.txt', 'rb') as handle:
    _input = handle.read()
    

#dictionary
file_to_rounds = pickle.loads(_input)

#main df
column_names = ['ID','Health','damage','kills','rifle','sniper','pistol','smg',
                'grenade','preplant kill','postplant kill','fast_kill_rating (first_kill)',
                'time of kills','total kills','total deaths', 'avg kill time', 
                'assists', 'team','positioning type', 'last x', 'last y', 
                'alone kills', 'distance to A bomb (on kill list)', 'Avg Distance to A bomb (on kill)',
                'times in catwalk_box', 'times in topmid_box', 'times in chair_box', 'times in midlane_box', 'times in underpass_box', 'times in window_box',\
                'times in stairs_box', 'times in tetris_box', 'times in sandwhich_box', 'times in Asite_box', 'times in firebox_box', 'times in jungle_box', 'times in connector_box',
                'times in opening_box', 'times in opening2_box', 'times in A_main_box', 'times in T_ramp_box', 'times in hell_box', 'times in palace_box', 'times in pillars_box', 
                'times in ticket_box', 'times in CT_ramp_box', 'alone_death']

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

def distance_between_points(P, Q):
    
    x1 = P[0]
    x2 = Q[0]
    y1 = P[1]
    y2 = Q[1]
    
    result = ((((x2 - x1 )**2) + ((y2-y1)**2) )**0.5)
    return result

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
   
    
    
    ''' GAME VARIABLES '''
    #ID, Health, damage, kills, rifle, sniper, pistol, smg, grenade, preplant kill, 
    # postplant kill, fast_kill_rating (first_kill), time of kills, total kills, 
    #total deaths, avg kill time, assists, 'team', positioning type (att or vic), 
    # last x (vic/att), last y(vic/att), alone kills, 
    # distance to A bomb (on kill list), Avg Distance to A bomb (on kills)
    #'times in catwalk_box', 'times in topmid_box', 'times in chair_box', 'times in midlane_box', 'times in underpass_box', 'times in window_box'(29), 
    #'times in stairs_box', 'times in tetris_box', 'times in sandwhich_box', 'times in Asite_box', 'times in firebox_box', 'times in jungle_box', 'times in connector_box',
    # 'times in opening_box', 'times in opening2_box', 'times in A_main_box', 'times in T_ramp_box', 'times in hell_box', 'times in palace_box', 'times in pillars_box', 
    # 'times in ticket_box', 'times in CT_ramp_box', alone_death (46),
    
    ct_player_1 = [ct_list[0], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ct_player_2 = [ct_list[1], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ct_player_3 = [ct_list[2], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ct_player_4 = [ct_list[3], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ct_player_5 = [ct_list[4], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    t_player_1 = [t_list[0], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    t_player_2 = [t_list[1], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    t_player_3 = [t_list[2], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    t_player_4 = [t_list[3], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    t_player_5 = [t_list[4], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0, [], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    
    
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
            '''when a player dies in row do calculations then'''
            victim = []
            attacker = []
            kill_flag = False
            for curr_player in all_players:
                if curr_player[0] == row['vic_id']:
                    victim = curr_player
                    
                    #Set postioning type == VIC
                    victim[18] = "VIC"
                    #Set last x and last y
                    victim[19] = row['victim_mapX']
                    victim[20] = row['victim_mapY']
                    
                    victim[1] -= row['hp_dmg']
                    
                if curr_player[0] == row['att_id']:
                    attacker = curr_player
                    
                    #Set postioning type == ATT
                    attacker[18] = "ATT"
                    #Set last x and last y
                    attacker[19] = row['attacker_mapX']
                    attacker[20] = row['attacker_mapY']
                    
                    attacker[2] += row['hp_dmg']
                    
                if len(attacker) != 0 and len(victim) != 0:
                    
                    #if a attacker does damage give him an assist,
                    if ([attacker[0], victim[0]]) not in assists:
                        assists.append([attacker[0], victim[0]])
                        
                   
                    if victim[1] <= 0 and kill_flag == False:
                        kill_flag = True
                    
                        
                        #alone kill and alone death
                        alone_kill = True
                        alone_death = True
                        distance_to_nearest_teammate = 99999
                        for player in all_players:
                            if ((player[17] == attacker[17]) and (player[1] > 0) and player[0] != attacker[0]):
                                result = distance_between_points([player[19], player[20]], [attacker[19], attacker[20]])
                                if result < distance_to_nearest_teammate:
                                    distance_to_nearest_teammate = result
                                if result < 400:
                                    alone_kill = False
                            if ((player[17] == victim[17]) and (player[1] > 0) and player[0] != victim[0]):
                                result2 = distance_between_points([player[19], player[20]], [victim[19], victim[20]])
                                if result2 < distance_to_nearest_teammate:
                                    distance_to_nearest_teammate = result2
                                if result2 < 400:
                                    alone_death = False
                                    
                        if alone_kill == True:
                            attacker[21] += 1
                        if alone_death == True:
                            victim[46] += 1

                        #remove assist from list when they kill
                        assists.remove([attacker[0], victim[0]])
                        attacker[3] += 1
                        if row['round'] == 9:
                            print(attacker[0],"killed", victim[0])
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
                        
                        #Append distance to A bomb on kill
                        attacker[22].append(distance_between_points([attacker[19], attacker[20]], sim.CenterA))
                        
                        #mid boxes and A_site boxes check (attacker only)
                        if row['att_id'] == attacker[0]:
                            pos_data = np.array([[row['attacker_mapX'], row['attacker_mapY']], [row['victim_mapX'], row['victim_mapY']]])
                            x, y = pos_data.T
                            index_counter = 0
                            for box in sim.list_of_boxes:
                                if (box[0] < x[0] < box[2]) and (box[3] < y[0] < box[1]):
                                    print("Attacker", row['att_id'], "in", box[4],"box")
                                    print(index_counter)
                                    if index_counter == 0:
                                        attacker[24] += 1
                                        
                                    elif index_counter == 1:
                                        attacker[25] += 1
                                        
                                    elif index_counter == 2:
                                        attacker[26] += 1
                                        
                                    elif index_counter == 3:
                                        attacker[27] += 1
                                        
                                    elif index_counter == 4:
                                        attacker[28] += 1
                                        
                                    elif index_counter == 5:
                                        attacker[29] += 1    
                                        
                                    elif index_counter == 6:
                                        attacker[30] += 1
                                        
                                    elif index_counter == 7:
                                        attacker[31] += 1
                                        
                                    elif index_counter == 8:
                                        attacker[32] += 1
                                        
                                    elif index_counter == 9:
                                        attacker[33] += 1
                                        
                                    elif index_counter == 10:
                                        attacker[34] += 1
                                    
                                    elif index_counter == 11:
                                        attacker[35] += 1
                                        
                                    elif index_counter == 12:
                                        attacker[36] += 1
                                        
                                    elif index_counter == 13:
                                        attacker[37] += 1
                                        
                                    elif index_counter == 14:
                                        attacker[38] += 1
                                        
                                    elif index_counter == 15:
                                        attacker[39] += 1
                                    
                                    elif index_counter == 16:
                                        attacker[40] += 1
                                        
                                    elif index_counter == 17:
                                        attacker[41] += 1
                                        
                                    elif index_counter == 18:
                                        attacker[42] += 1
                                        
                                    elif index_counter == 19:
                                        attacker[43] += 1
                                        
                                    elif index_counter == 20:
                                        attacker[44] += 1
                                    
                                    else:
                                        attacker[45] += 1
                                index_counter += 1
                    
                        

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
            
            #average time of kills
            if player[12] and len(player[12]) > 1:
                for i in range(len(player[12])):
                    if (i + 1) < (len(player[12])):
                        time_delta += player[12][i+1] - player[12][i]
                    else:
                        #will get more accurate each round and harder to change
                        player[15] = time_delta/(len(player[12]) - 1)
                        
            #average of distance to A bomb kills                        
            if player[22] and len(player[22]) > 1:
                for i in range(len(player[22])):
                    if (i + 1) < (len(player[22])):
                        time_delta += player[22][i+1] - player[22][i]
                    else:
                        #will get more accurate each round and harder to change
                        player[23] = time_delta/(len(player[22]) - 1)

            ''' POST ROUND VARIABLE CHANGES '''
            first_dmg_turn_counter -= 1
                        
        
                
    players_df = pd.DataFrame(all_players)
    players_df.columns = column_names
    return players_df
    
    
all_files = data.file.unique()

index = 0

for f in all_files:
    if index == iterations:
        break
    round_df = all_roles_in_round(data, f)
    print('--------------------------------------')
    main_df = main_df.append(round_df, ignore_index = True)
    index += 1

main_df = main_df.drop(['ID', 'time of kills', 'Health', 'team', 'positioning type', 'last x', 'last y', 'distance to A bomb (on kill list)'], axis=1)
pd.set_option("display.max_rows", None, "display.max_columns", None, 'expand_frame_repr', False)


print(main_df.head())
    
#save to csv
main_df.to_csv('players_df.csv', index = False, encoding='utf-8')
    



    
    
    





