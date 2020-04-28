###############################
## Author: TRAN Quang Toan   ##
## Project Game Puissance 4  ##
## Version 1                 ##
## 10 Feb 2020               ##
###############################

from define import *
from ft_lib import *
from eval_func import *
from random import randrange, shuffle
from copy import deepcopy

def is_game_over(ar, player, org_player, eval_func, NB_PLAYED, depth, last_moved):
	x, y = last_moved[0], last_moved[1]
	if 1-player == org_player and is_winning_pos(ar, x, y):
		return (1000000-TIME_PENALTY*(NB_PLAYED), None)	
	elif 1-player != org_player and is_winning_pos(ar, x, y):
		return (-1000000+TIME_PENALTY*(NB_PLAYED), None)
	elif NB_PLAYED == TX*TY:
		return (0, None)
	if (depth == 0):
		return score_ar_z(ar, eval_func, player,org_player)
	return ()

def minimax(ar,player,org_player,NB_PLAYED,depth,last_moved,eval_func,a,b):
	result = is_game_over(ar, player, org_player, eval_func, NB_PLAYED, depth, last_moved)
	if result != ():
		return result
	max_v, min_v, py = NEG_INF, INF, None
	if player == org_player: # Maximal Player
		lst_y = lst_applicable(ar, TY, player)
		shuffle(lst_y) ## Melanger lst_y
		for y in lst_y:
			cp_ar = deepcopy(ar)
			coord = turn(cp_ar, y, player)
			score = minimax(cp_ar,1-player,org_player,NB_PLAYED+1,depth-1,coord,eval_func,a,b)
			# ar[coord[0]][coord[1]] = BLK
			if score[0] > max_v:
				max_v = score[0]
				py = coord[1]
			if a < max_v: ## Alpha-Beta
				a = max_v
			if a >= b:
				break
		return (max_v, py)
	else: # Minimal Player
		lst_y = lst_applicable(ar, TY, player)
		shuffle(lst_y) ## Melanger lst_y
		for y in lst_y:
			cp_ar = deepcopy(ar)
			coord = turn(cp_ar, y, player)
			score = minimax(cp_ar,1-player,org_player,NB_PLAYED+1,depth-1,coord,eval_func,a,b)
			# ar[coord[0]][coord[1]] = BLK
			if score[0] < min_v:
				min_v = score[0]
				py = coord[1]
			if b > min_v: ## Alpha-Beta 
				b = min_v
			if a >= b:
				break
		return (min_v, py)

##
#######################################
## mode = 1 => 'AI' joue random mouvement entre 0 et 6
## mode = 2 => AI_Normal
## mode = 3 => AI_Minimax
## depth = 3 par default
def AI_Mode(mode=2, depth=3): 
	NB_PLAYED = 0
	arena = init_arena(TX, TY)
	print_arena(arena)
	y = choose_number(CHOOSE_TURN, 0, 1, WARN_NUMBER_TURN)
	t = 1 - y ## Si y = 0 => Joueur choisit Non => t = 1 => AI va commencer le premier mouvement
	          ## Si y = 1 => Joueur choisit Oui => t = 0 => L'homme va commencer le premier mouvement
	while (NB_PLAYED < TX*TY):
		coord = ()
		s = "Choose your Move from 0 -> 6 \n  [ PLAYER "+str(t+1)+"] ("+PLAYER_COLORED[t]+") : "
		s = colored(s, 'white', 'on_red', attrs=["bold"])
		if (t == 0):
			y = choose_number(s, 0, 6, WARN_NUMBER)
		else:
			if mode == 1:
				y = randrange(TY)
			elif mode == 2:
				y = score_ar(arena,idm2,t,t)[1]
			elif mode == 3:
				y = minimax(arena,t,t,NB_PLAYED,depth,(0,0),idm5,NEG_INF,INF)[1]

		fclear()
		coord = turn(arena, y, t)
		if (coord == ()):
			print_arena(arena)
			print(WARN_ILLEGALMOVE)
			continue
		print_arena(arena)
		if (is_winning_pos(arena, coord[0], coord[1])):
			print("\nFelicitation!! [ PLAYER", t+1, PLAYER_COLORED[t], "] WON!!\n")
			break
		t ,NB_PLAYED = 1 - t, NB_PLAYED + 1
		if (NB_PLAYED == TX*TY):
			print(TIE)
			break
##
####################################################
## mode = True => AI_Normal vs AI_Minimax
## mode = False => AI_Minimax vs AI_Minimax
## Le but pout comparer entre les AIs et entre les fonctions evaluations
## Et c'est pour tester des erreurs rapidemment
def AI_vs_AI(mode,eval_func1,depth1,eval_func2,depth2):
	t, NB_PLAYED = 0, 0
	arena = init_arena(TX, TY)
	print_arena(arena)
	while (NB_PLAYED < TX*TY):
		if (t == 0):
			if mode:
				y = score_ar(arena, eval_func1, t, t)[1]
			else:
				y = minimax(arena,t,t,NB_PLAYED,depth1,(0,0),eval_func1,NEG_INF,INF)[1]
		else:
			y = minimax(arena,t,t,NB_PLAYED,depth2,(0,0),eval_func2,NEG_INF,INF)[1]
		fclear()

		coord = turn(arena, y, t)		
		print_arena(arena)
		if (is_winning_pos(arena, coord[0], coord[1])):
			print("\nFelicitation!! [ PLAYER", t+1, PLAYER_COLORED[t], "] WON!!\n")
			break
		t ,NB_PLAYED = 1 - t, NB_PLAYED + 1
		if (NB_PLAYED == TX*TY):
			print(TIE)
			break
##
####################################################