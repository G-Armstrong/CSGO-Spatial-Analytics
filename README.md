# CSGO-Spatial-Analytics
## Input
* https://www.kaggle.com/skihikingkevin/csgo-matchmaking-damage

## Intro/Descriptions

## Folders & Files
* src.py: Brings in data, sorts data, and filters for non-eco rounds
* reader.py: Produces density map of pre and post A plant for entire data
* sim.py: simulates a round with attackers and victims color coded for each side (used for testing boxes)
* roles.py: main code for feature handling
* kmeans_final: code for determining clusters (AI stuff)

## 11/10/2020
* Intial coding start date

## 12/5/2020
* Finished Preplant heatmaps for offense and defense where they inflict damage and win the round 

## 12/7/2020
* End of First Semester Presentation (PPT)

## 12/22/2020
* Planned Spring 2021 goals and modified code to reflect the aggressors in engagements ('att_side' == ...)

## 12/28/2020
* Finished pre and postplant heatmaps where both sides are aggressors in engagements

## 12/29/2020
* Finished pre and postplant heatmaps where both sides are victims in engagements

## 1/5/2021
* Progress made on single round animation. Isolated 10 players in data for that single round

## 1/9/2021
* Created method to track individual attacking player on heat map
* Created method to find individual player ID
* Created method to find IDs of all players and assign them to their respective teams 

## 1/23/2021
* 64 lines of code changed
* Created new heat maps that take a single round and display unique colors for CTs players and wether or not they are the victims or attackers in their engagements

## 1/26/2021
* Finalized animation of single round, planning next steps

## 2/2/2021
* Created a list of 23 features to track to determine player roles

## 2/8/2021
* Began tracking player features and applied weights to each of these features to be used later for assigned player roles based on historical data 

## 2/27/2021
* Output visualization of sklearn clustering found on kmeans_final.py

## 3/6/2021
* Experimented with Weka to create a Classifier tree of 14 tracked attributes (ClassiferTree.PNG) and output mean and SD for k=5 clusters
* Created AlgorithmComparison.py to compare the accuracy of various algorithms on training and testing data

## 4/4/2021
* Added avg distance to A site for all players
* Tallied if a player got a kill in a mid box (see sim.py for mid boxes locations)
* Cleaned code in roles.py and sim.py.

## 4/6/2021
* Added A_site box checks
* Statistics are now collectable on where certain types of players (obtained from clustering) get kills 
* Since the focus will be on A-bombsite attacks, pre and post plant recommendations can be made to players based on statistical analysis
* of successful positions

## 4/10/2021
* Ran rough PCA and KMeans analysis in kmeans_final.py
* SHOTGUN_kill, MACHINEGUN_kill  These two features will be removed since these weapons are unlikely to appear in a NORMAL buy round 
* Planned out coding of remaining features. Do trade-kill last since it is time dependent and annoying to code  


## TODO
* <s>Pre and Postplants Heatmaps where both sides are victims in engagements</s>
* <s>Create simuation of single round </s> 
* <s> Add Avg distance to A bombsite </s>
* <s> Map boxes around vital areas of the map for A post plant </s>
* Interpret clustering output and find the best algorithm to group player behavior
* Apply statistics once clustering interpretion is finished
* Add columns for each box
* Continue to add features and clean code



