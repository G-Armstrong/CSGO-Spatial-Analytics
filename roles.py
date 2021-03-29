# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 19:09:32 2021

Make method to loop through single round to determine which player fills what role
create train set size vs accuracy graph

The General Making Choices Approach

####Raymond To-Do####
Add distance to A bombsite 
Add mid kill
Add columns for each box
Move box code over from sim.py
Add avg distance to all teammates for T players?

####Grant To-Do####
Map boxes around vital areas of the map for A post plant
Get A x/y
Get mid x/y

####Features to add####
SMG_kill
SHOTGUN_kill
MACHINEGUN_kill        
TRADE_KILL
SITE_KILL
MID_KILL                            
ALONE_DEATH
Distance_to_bombsite
Distance_to_last_known
Distance_traveled
TIME_OF_KILLS


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
writer = Writer()


#make empty df   
data = pd.DataFrame()

#iterations = 245
iterations = 5

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
                'time of kills','total kills','total deaths', 'avg kill time', 'assists', 'team','positioning type', 'last x', 'last y', 'alone kills']
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
    #ID, Health, damage, kills, rifle, sniper, pistol, smg, grenade, preplant kill, 
    # postplant kill, fast_kill_rating (first_kill), time of kills, total kills, 
    #total deaths, avg kill time, assists, 'team', positioning type (att or vic), last x (vic/att), last y(vic/att), alone kills
    ct_player_1 = [ct_list[0], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0]
    ct_player_2 = [ct_list[1], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0]
    ct_player_3 = [ct_list[2], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0]
    ct_player_4 = [ct_list[3], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0]
    ct_player_5 = [ct_list[4], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "CounterTerrorist", "N/A", 0, 0, 0]
    
    t_player_1 = [t_list[0], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0]
    t_player_2 = [t_list[1], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0]
    t_player_3 = [t_list[2], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0]
    t_player_4 = [t_list[3], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0]
    t_player_5 = [t_list[4], 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, [], 0, 0, 0, 0, "Terrorist", "N/A", 0, 0, 0]
    
    
    
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
                        
                        #alone kill
                        alone_kill = True
                        distance_to_nearest_teammate = 99999
                        for player in all_players:
                            if ((player[17] == attacker[17]) and (player[1] > 0) and player[0] != attacker[0]):
                                result = distance_between_points([player[19], player[20]], [attacker[19], attacker[20]])
                                if result < distance_to_nearest_teammate:
                                    distance_to_nearest_teammate = result
                                if result < 400:
                                    alone_kill = False
                           
                                    
                        if alone_kill == True:
                            attacker[21] += 1

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
    if index == iterations:
        break
    round_df = all_roles_in_round(data, f)
    print('--------------------------------------')
    main_df = main_df.append(round_df, ignore_index = True)
    index += 1

main_df = main_df.drop(['time of kills', 'Health', 'team', 'positioning type', 'last x', 'last y'], axis=1)
pd.set_option("display.max_rows", None, "display.max_columns", None, 'expand_frame_repr', False)

print(main_df)
    
#save to csv
main_df.to_csv('players_df.csv', index = False, encoding='utf-8')
    



    
    
    





