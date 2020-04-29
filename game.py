###############################
## Author: TRAN Quang Toan   ##
## Project Game Puissance 4  ##
## Version 1                 ##
## 10 Feb 2020               ##
###############################

from define import *
from ft_lib import *
from AI_lib import *
from termcolor import colored

def Normal_Game():
	## NB_PLAYED: nombre de mouvements on a deja joue (0 <= NB_PLAYED <= 6*7=42)
	t, NB_PLAYED = 0, 0  ## t = 0 | 1 (player 0 | 1)
	arena = init_arena(TX, TY)
	print_arena(arena)
	##
	while (NB_PLAYED < TX*TY): ## Si NB_PLAYED < TX*TY (42): On continuera a jouer
		coord = ()
		s = "Choose your Move from 0 -> 6 \n  [ PLAYER "+str(t+1)+"] ("+PLAYER_COLORED[t]+") : "
		s = colored(s, 'white', 'on_red', attrs=["bold"])
		y = choose_number(s, 0, 6, WARN_NUMBER) ## On saisit 0->6
		fclear()
		coord = turn(arena, y, t) ## On place la balle a la position y(0-6)
		
		if (coord == ()): ## Si la position y n'est pas valide => Il faut re-saisir y
			print_arena(arena)
			print(WARN_ILLEGALMOVE)
			continue
		
		print_arena(arena) ## Si la position y est valide
		                   ## On verifie si player t(0|1) a gagne et quitte la boucle
		if (is_winning_pos(arena, coord[0], coord[1])):
			print("\nFelicitation!! [ PLAYER", t+1, PLAYER_COLORED[t], "] WON!!\n")
			break
		## Sinon, l'adversaire va jouer et le nombre mouvements +1
		t ,NB_PLAYED = 1 - t, NB_PLAYED + 1
		if (NB_PLAYED == TX*TY): ## Si NB_PLAYED == 42 et personne a gagne=> C'est Draw
			print(TIE)
			break

def Menu():
	fclear()
	print(COLORED_TITLE)
	n = choose_number(COLORDED_OPT, 1, 5, WARN_NUMBER_MENU)
	fclear()
	if (n == 1):
		Normal_Game()         ## 2 Players
	elif (n == 2):
		AI_Mode(1)            ## StupidAI fait des randoms mouvements
	elif (n == 3):
		AI_Mode(2)            ## NormalAI cherche le meilleur mouvement avec evaluation function
	elif (n == 4):
		AI_Mode(3, 6)         ## MinimaxAI 
	elif (n == 5):
		AI_vs_AI(False,idm5,6,idm3,4)  ## True:  NormalAI vs MinimaxAI
                              ## False: MinimaxAI vs MinimaxAI
                              ## Le but est pour comparer entre les AIs et entre les fonctions evaluations
                              ## Et c'est pour tester des erreurs rapidemment

######
# Le programme va commencer ici, par appeller la fonction Menu()
#
Menu()
#
#
##########

# best_agent = [10000,33,10,5000] 
# curr_agent = [1,1,1,1]

# def ef_best(player,a,b,c,d):
# 	odd_player = 0
# 	if (player == 0):
# 		odd_player = 1
# 	score, blank, piece = 0, 0, 0
# 	lst = [a,b,c,d]
# 	for i in lst:
# 		if (i == BLK):
# 			blank += 1
# 		if (i == player):
# 			piece += 1
# 	if (piece == 4 and blank == 0):
# 		score += best_agent[0]
# 	elif (piece == 3 and blank == 1):
# 		score += best_agent[1]
# 	elif (piece == 2 and blank == 2):
# 		score += best_agent[2]

# 	blank, piece = 0, 0
# 	for i in lst:
# 		if (i == player):
# 			blank += 1
# 		if (i == odd_player):
# 			piece += 1
# 	if (piece == 3 and blank == 1):
# 		score += best_agent[3]

# 	if ((a == player or d == player)
# 	and (b == odd_player and c == odd_player)):
# 		score += best_agent[1]*3
# 	if ((a == odd_player and b == player)
# 	and (c == odd_player and d == BLK)):
# 		score += best_agent[2]

# 	return score

# def ef_curr(player,a,b,c,d):
# 	odd_player = 0
# 	if (player == 0):
# 		odd_player = 1
# 	score, blank, piece = 0, 0, 0
# 	lst = [a,b,c,d]
# 	for i in lst:
# 		if (i == BLK):
# 			blank += 1
# 		if (i == player):
# 			piece += 1
# 	if (piece == 4 and blank == 0):
# 		score += curr_agent[0]
# 	elif (piece == 3 and blank == 1):
# 		score += curr_agent[1]
# 	elif (piece == 2 and blank == 2):
# 		score += curr_agent[2]

# 	blank, piece = 0, 0
# 	for i in lst:
# 		if (i == player):
# 			blank += 1
# 		if (i == odd_player):
# 			piece += 1
# 	if (piece == 3 and blank == 1):
# 		score += curr_agent[3]

# 	if ((a == player or d == player)
# 	and (b == odd_player and c == odd_player)):
# 		score += best_agent[1]*3
# 	if ((a == odd_player and b == player)
# 	and (c == odd_player and d == BLK)):
# 		score += best_agent[2]

# 	# print(curr_agent)
# 	return score

# def deep_learning():
# 	global best_agent
# 	global curr_agent
# 	for i1 in range(24,34,3):
# 		for i2 in range(2,15,2):
# 			# for i3 in range(1,3,1):
	
# 			curr_agent = [10000,i1,i2,5000]
# 			res1, res2 = [], []
# 			for game in range(5): ## best vs current
# 				res1.append(AI_vs_AI(False,ef_best,4,ef_curr,4))
# 			for game in range(5): ## current vs best
# 				res2.append(AI_vs_AI(False,ef_curr,4,ef_best,4))
# 			r_curr = count(res1,1)+count(res2,0)
# 			r_best = count(res1,0)+count(res2,1)
# 			print(best_agent,"vs",curr_agent,":",r_best,"-",r_curr)
# 			if r_curr > r_best:
# 				print(best_agent, "-->", curr_agent)
# 				best_agent = curr_agent
	
# 	print(best_agent)


# def test():
# 	global best_agent
# 	global curr_agent
# 	curr_agent = [1,1,1,1,1]
# 	res1, res2 = [], []
# 	for game in range(5): ## best vs current
# 		res1.append(AI_vs_AI(False,ef_best,4,ef_curr,4))
# 	for game in range(5): ## current vs best
# 		res2.append(AI_vs_AI(False,ef_curr,4,ef_best,4))
# 	if count(res1,1)+count(res2,0) > count(res1,0)+count(res2,1):
# 		best_agent = curr_agent
# 	print(res1, res2)
# 	print(best_agent)

# deep_learning()
# test()
# AI_vs_AI(True,idm3,4,idm5,4)