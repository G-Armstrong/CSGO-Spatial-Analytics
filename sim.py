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
first_game = ""

#['Unnamed: 0','file','map','date','round','tick','seconds','att_team','vic_team','att_side','vic_side','hp_dmg','arm_dmg','is_bomb_planted',
#                                                                 'bomb_site','hitbox','wp','wp_type','award','winner_team','winner_side','att_id','att_rank','vic_id','vic_rank','att_pos_x','att_pos_y','vic_pos_x',
#                                                                 'vic_pos_y','round_type','ct_eq_val','t_eq_val','avg_match_rank']

for k,v in file_to_rounds.items(): #taking a single round at a time and splitting by pre and post plant

    if k == "003218553373129179487_1555113029.dem":
        first_game = k
        
    #for rnd in v:
        # print("att_id:", data['att_id'])
        # print("vic_id:", data['vic_id'])
        # print()
        #first round of first game on mirage in data
        #sim_round_one.append(data[(data['round'] == 4) & (data['file'] == first_game) & (data['att_id'] == 76561198152153688)].values.tolist())
    sim_round_one = (data[(data['round'] == 4) & (data['file'] == first_game)].values.tolist())

#make sure there are <= 10 att_id's
#attid = 21, vic_id = 23
att_id_list = []
vic_id_list = []

for aids in sim_round_one:
    att_id_list.append(aids[21])
    vic_id_list.append(aids[23])

filtered_att_id_list = list(set(att_id_list))
filtered_vic_id_list = list(set(vic_id_list))

print(filtered_att_id_list)
print(filtered_vic_id_list)

#track 1 player through round
#track atts through round
#track vics
#track att/vic pairs


