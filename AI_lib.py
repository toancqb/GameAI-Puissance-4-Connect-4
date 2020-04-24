###############################
## Author: TRAN Quang Toan   ##
## Project Game Puissance 4  ##
## Version 1                 ##
## 10 Feb 2020               ##
###############################

from define import *
from ft_lib import *
from random import randrange, shuffle

######################################
## 2eme version de fonction evaluation
## [O][O][O][O] += 1000000
## [O][ ][O][O] += 5 (avoir 1 BLK)
## [O][ ][ ][O] += 2 (avoir 2 BLK)
## [X][O][X][X] += 10000 (Eviter le pire, l'adversaire va gagner si on ne l'emperche pas)
## [O][X][X][O] += 500
## [X][O][X][ ] += 500
def idm2(player, a, b, c, d):
	odd_player = 0
	if player == 0:
		odd_player = 1
	score, blank, piece = 0, 0, 0
	lst = [a,b,c,d]
	for i in lst:
		if (i == BLK):
			blank += 1
		if (i == PLAYER[player]):
			piece += 1
	if (piece == 4 and blank == 0):
		score += 1000000
	if (piece == 3 and blank == 1):
		score += 5
	elif (piece == 2 and blank == 2):
		score += 2

	blank, piece = 0, 0
	for i in lst:
		if (i == PLAYER[player]):
			blank += 1
		if (i == PLAYER[odd_player]):
			piece += 1
	if (piece == 3 and blank == 1):
		score += 10000

	if ((a == PLAYER[player] or d == PLAYER[player])
	and (b == PLAYER[odd_player] and c == PLAYER[odd_player])):
		score += 500
	if ((a == PLAYER[odd_player] and b == PLAYER[player])
	and (c == PLAYER[odd_player] and d == BLK)):
		score += 500

	return score


#######################################
## 3eme version de fonction evaluation
## [O][O][O][O] += 100
## [O][ ][O][O] += 9 (avoir 1 BLK)
## [O][ ][ ][O] += 4 (avoir 2 BLK)
## [O][ ][ ][ ] += 1 (avoir 3 BLK)
## [X][O][X][X] += 100 (Eviter le pire, l'adversaire va gagner si on ne l'emperche pas)
def idm3(player, a, b, c, d):
	odd_player = 0
	if (player == 0):
		odd_player = 1
	score, blank, piece = 0, 0, 0
	lst = [a,b,c,d]
	for i in lst:
		if (i == BLK):
			blank += 1
		if (i == PLAYER[player]):
			piece += 1
	if (piece == 4 and blank == 0):
		score += 100
	elif (piece == 3 and blank == 1):
		score += 9
	elif (piece == 2 and blank == 2):
		score += 4
	elif piece == 1 and blank == 3:
		score += 1

	blank, piece = 0, 0
	for i in lst:
		if (i == PLAYER[player]):
			blank += 1
		if (i == PLAYER[odd_player]):
			piece += 1
	if (piece == 3 and blank == 1):
		score += 100

	return score

#######################################
## 4eme version de fonction evaluation
## [O][O][O][O] += 100000
## [O][ ][O][O] += 5 (avoir 1 BLK)
## [O][ ][ ][O] += 2 (avoir 2 BLK)
## [X][O][X][X] += 100000 (Eviter le pire, l'adversaire va gagner si on ne l'emperche pas)
def idm4(player, a, b, c, d):
	odd_player = 0
	if (player == 0):
		odd_player = 1
	score, blank, piece = 0, 0, 0
	lst = [a,b,c,d]
	for i in lst:
		if (i == BLK):
			blank += 1
		if (i == PLAYER[player]):
			piece += 1
	if (piece == 4 and blank == 0):
		score += 100000
	if (piece == 3 and blank == 1):
		score += 5
	elif (piece == 2 and blank == 2):
		score += 2

	odd_piece, piece = 0, 0
	for i in lst:
		if (i == PLAYER[player]):
			odd_piece += 1
		if (i == PLAYER[odd_player]):
			piece += 1
	if (piece == 3 and odd_piece == 1):
		score += 100000

	return score

def score_pos(ar, coord, calc_func, p):
	x = coord[0]
	y = coord[1]
	if (y == 3):
		count = 1
		for x in range(TX-1,-1,-1):
			if ar[x][y] == p:
				count += 1
		score = 3*count
	else:
		score = 0
	for i in range(-3, 1):
		if (y+i >= 0 and y+i+3 < TY):
			score += calc_func(p, ar[x][y+i], ar[x][y+i+1], ar[x][y+i+2], ar[x][y+i+3])

		if (x+i >= 0 and x+i+3 < TX):
			score += calc_func(p, ar[x+i][y], ar[x+i+1][y], ar[x+i+2][y], ar[x+i+3][y])

		if (x+i >= 0 and x+i+3 < TX and y+i >= 0 and y+i+3 < TY):
			score += calc_func(p, ar[x+i][y+i], ar[x+i+1][y+i+1], ar[x+i+2][y+i+2], ar[x+i+3][y+i+3])

	ch = [[3,-3],[2,-2],[1,-1],[0,0]]

	for i in ch:
		if (check_range(x+i[0],0,TX-1) and check_range(y+i[1],0,TY-1)
			and check_range(x+i[0]-3, 0, TX-1) and check_range(y+i[1]+3, 0, TY-1)):
			score += calc_func(p, ar[x+i[0]][y+i[1]], ar[x+i[0]-1][y+i[1]+1]
				, ar[x+i[0]-2][y+i[1]+2], ar[x+i[0]-3][y+i[1]+3])

	return score

def score_ar(ar, calc_func, player, org_player):
	mn = cp_arena(ar)
	max_point = NEG_INF
	tmp, px, py, sign = 0, None, None, 1
	if player != org_player:
		sign = -1
	for y in range(TY):
		new_mn = cp_arena(mn)
		coord = turn(new_mn, y, PLAYER[player])
		if coord == ():
			continue
		tmp = score_pos(new_mn, coord, calc_func, player)
		if (tmp > max_point):
			max_point = tmp
			px = coord[0]
			py = coord[1]
	return (sign*max_point, py)

def score_ar_z(ar, calc_func, player, org_player):
	tmp, px, py, sign = 0, None, None, 1
	score = 0
	if player != org_player:
		sign = -1
	for x in range(TX):
		for y in range(TY):
			if ar[x][y] != BLK:
				score += score_pos(ar, (x,y), calc_func, player)
				if y == 3:
					score += 3
	return (sign*score, None)

def minimax(ar,player,org_player,NB_PLAYED,depth,result,calc_func,a,b):
	if result == 1:
		return (1000000, None)
	elif result == 0 or NB_PLAYED == TX*TY:
		return (0, None)
	elif result == -1:
		return (-1000000, None)
	if (depth == 0):
		m = score_ar_z(ar, calc_func, player,org_player)
		return (m[0], m[1])
	coord = ()
	if player == org_player: # Maximal Player
		#lst_y = lst_applicable(ar, TY, player)
		lst_y = [i for i in range(TY) if turn(deepcopy(ar), i, PLAYER[player]) != ()]
		shuffle(lst_y)
		max_v, py = NEG_INF, None
		for y in lst_y:
			cp_ar = cp_arena(ar)
			coord = turn(cp_ar, y, PLAYER[player])
			if is_winning_pos(cp_ar, coord[0], coord[1]):
				result = 1
			elif NB_PLAYED == TX*TY:
				result = 0
			score = minimax(cp_ar,1-player,org_player,NB_PLAYED+1,depth-1,result,calc_func,a,b)
			if score[0] - TIME_PENALTY*(NB_PLAYED+1) > max_v:
				max_v = score[0] - TIME_PENALTY*(NB_PLAYED+1)
				py = coord[1]
			if a < max_v:
				a = max_v
			if a >= b:
				break
		if py == None:
			py = lst_applicable2(ar, TY, player)[0]
		return (max_v, py)
	else: # Minimal Player
		#lst_y = lst_applicable(ar, TY, player)
		lst_y = [i for i in range(TY) if turn(deepcopy(ar), i, PLAYER[player]) != ()]
		shuffle(lst_y)
		min_v, py = INF, None
		for y in lst_y:
			cp_ar = cp_arena(ar)
			coord = turn(cp_ar, y, PLAYER[player])
			if is_winning_pos(cp_ar, coord[0], coord[1]):
				result = -1
			elif NB_PLAYED == TX*TY:
				result = 0
			score = minimax(cp_ar,1-player,org_player,NB_PLAYED+1,depth-1,result,calc_func,a,b)
			if score[0] + TIME_PENALTY*(NB_PLAYED+1) < min_v:
				min_v = score[0] + TIME_PENALTY*(NB_PLAYED+1)
				py = coord[1]
			if b > min_v:
				b = min_v
			if a >= b:
				break
		if py == None:
			py = lst_applicable2(ar, TY, player)[0]
		return (min_v, py)

#######################################

def minimax2(ar,player,org_player,NB_PLAYED,depth,result,calc_func,a,b):
	if result == 1:
		return (1000000, None)
	elif result == 0 or NB_PLAYED == TX*TY:
		return (0, None)
	elif result == -1:
		return (-1000000, None)
	if (depth == 0):
		m = score_ar(ar, calc_func, player,org_player)
		return (m[0], m[1])
	coord = ()
	if player == org_player: # Maximal Player
		#lst_y = lst_applicable(ar, TY, player)
		lst_y = [i for i in range(TY) if turn(deepcopy(ar), i, PLAYER[player]) != ()]
		shuffle(lst_y)
		max_v, py = NEG_INF, None
		for y in lst_y:
			cp_ar = cp_arena(ar)
			coord = turn(cp_ar, y, PLAYER[player])
			if is_winning_pos(cp_ar, coord[0], coord[1]):
				result = 1
			elif NB_PLAYED == TX*TY:
				result = 0
			score = minimax(cp_ar,1-player,org_player,NB_PLAYED+1,depth-1,result,calc_func,a,b)
			if score[0] - TIME_PENALTY*(NB_PLAYED+1) > max_v:
				max_v = score[0] - TIME_PENALTY*(NB_PLAYED+1)
				py = coord[1]
			if a < max_v:
				a = max_v
			if a >= b:
				break
		if py == None:
			py = lst_applicable2(ar, TY, player)[0]
		return (max_v, py)
	else: # Minimal Player
		#lst_y = lst_applicable(ar, TY, player)
		lst_y = [i for i in range(TY) if turn(deepcopy(ar), i, PLAYER[player]) != ()]
		shuffle(lst_y)
		min_v, py = INF, None
		for y in lst_y:
			cp_ar = cp_arena(ar)
			coord = turn(cp_ar, y, PLAYER[player])
			if is_winning_pos(cp_ar, coord[0], coord[1]):
				result = -1
			elif NB_PLAYED == TX*TY:
				result = 0
			score = minimax(cp_ar,1-player,org_player,NB_PLAYED+1,depth-1,result,calc_func,a,b)
			if score[0] + TIME_PENALTY*(NB_PLAYED+1) < min_v:
				min_v = score[0] + TIME_PENALTY*(NB_PLAYED+1)
				py = coord[1]
			if b > min_v:
				b = min_v
			if a >= b:
				break
		if py == None:
			py = lst_applicable2(ar, TY, player)[0]
		return (min_v, py)

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
	zz = (0, 0)
	while (NB_PLAYED < TX*TY):
		coord = ()
		s = "Choose your Move from 0 -> 6 \n  [ PLAYER "+str(t+1)+"] ("+PLAYER[t]+") : "
		s = colored(s, 'white', 'on_red', attrs=["bold"])
		if (t == 0):
			y = choose_number(s, 0, 6, WARN_NUMBER)
		else:
			if mode == 1:
				y = randrange(TY)
			elif mode == 2:
				y = score_ar(arena,idm2,t,t)[1]
			elif mode == 3:
				zz = minimax(arena,t,t,NB_PLAYED,depth,2,idm3,NEG_INF,INF)
				y = zz[1]

		clear()
		coord = turn(arena, y, PLAYER[t])
		if (coord == ()):
			print_arena(arena)
			print(WARN_ILLEGALMOVE)
			continue
		print_arena(arena)
		print(zz[1],":",zz[0],"\n")
		if (is_winning_pos(arena, coord[0], coord[1])):
			print("\nFelicitation!! [ PLAYER", t+1, PLAYER[t], "] WON!!\n")
			break
		t ,NB_PLAYED = 1 - t, NB_PLAYED + 1
		if (NB_PLAYED == TX*TY):
			print(TIE)
			break
##
####################################################
## mode = True => AI_Normal vs AI_Minimax
## mode = False => AI_Minimax vs AI_Minimax
## Le but pout comparer entre les AIs et les fonctions evaluations
## Et c'est pour tester des erreurs rapidement
def AI_vs_AI(mode, depth1, depth2):
	t, NB_PLAYED = 0, 0
	arena = init_arena(TX, TY)
	print_arena(arena)
	while (NB_PLAYED < TX*TY):
		if (t == 0):
			if mode:
				y = score_ar(arena, idm2, t, t)[1]
			else:
				y = minimax(arena,t,t,NB_PLAYED,depth1,2,idm3,NEG_INF,INF)[1]
		else:
			y = minimax2(arena,t,t,NB_PLAYED,depth2,2,idm4,NEG_INF,INF)[1]
		clear()

		coord = turn(arena, y, PLAYER[t])
		if (coord == ()):
			print_arena(arena)
			print(WARN_ILLEGALMOVE)
			continue
		print_arena(arena)
		if (is_winning_pos(arena, coord[0], coord[1])):
			print("\nFelicitation!! [ PLAYER", t+1, PLAYER[t], "] WON!!\n")
			break
		t ,NB_PLAYED = 1 - t, NB_PLAYED + 1
		if (NB_PLAYED == TX*TY):
			print(TIE)
			break
