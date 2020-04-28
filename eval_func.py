###############################
## Author: TRAN Quang Toan   ##
## Project Game Puissance 4  ##
## Version 1                 ##
## 10 Feb 2020               ##
###############################

from define import *
from ft_lib import *
from copy import deepcopy

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
		if (i == player):
			piece += 1
	if (piece == 4 and blank == 0):
		score += 1000000
	if (piece == 3 and blank == 1):
		score += 5
	elif (piece == 2 and blank == 2):
		score += 2

	blank, piece = 0, 0
	for i in lst:
		if (i == player):
			blank += 1
		if (i == odd_player):
			piece += 1
	if (piece == 3 and blank == 1):
		score += 10000

	if ((a == player or d == player)
	and (b == odd_player and c == odd_player)):
		score += 500
	if ((a == odd_player and b == player)
	and (c == odd_player and d == BLK)):
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
		if (i == player):
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
		if (i == player):
			blank += 1
		if (i == odd_player):
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
		if (i == player):
			piece += 1
	if (piece == 4 and blank == 0):
		score += 100000
	if (piece == 3 and blank == 1):
		score += 5
	elif (piece == 2 and blank == 2):
		score += 2

	odd_piece, piece = 0, 0
	for i in lst:
		if (i == player):
			odd_piece += 1
		if (i == odd_player):
			piece += 1
	if (piece == 3 and odd_piece == 1):
		score += 100000

	return score

#######################################
## 5eme version de fonction evaluation
## [O][O][O][O] += 100
## [O][ ][O][O] += 24 (avoir 1 BLK)
## [O][ ][ ][O] += 16 (avoir 2 BLK)
## [O][ ][ ][ ] += 1 (avoir 3 BLK)
## [X][O][X][X] += 100 (Eviter le pire, l'adversaire va gagner si on ne l'emperche pas)
def idm5(player, a, b, c, d):
	odd_player = 0
	if (player == 0):
		odd_player = 1
	score, blank, piece = 0, 0, 0
	lst = [a,b,c,d]
	for i in lst:
		if (i == BLK):
			blank += 1
		if (i == player):
			piece += 1
	if (piece == 4 and blank == 0):
		score += 100
	elif (piece == 3 and blank == 1):
		score += 24
	elif (piece == 2 and blank == 2):
		score += 16
	elif piece == 1 and blank == 3:
		score += 1

	blank, piece = 0, 0
	for i in lst:
		if (i == player):
			blank += 1
		if (i == odd_player):
			piece += 1
	if (piece == 3 and blank == 1):
		score += 100

	return score

def score_pos(ar, coord, calc_func, p):
	x = coord[0]
	y = coord[1]
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

# def score_ar2(ar, eval_func, player, org_player):
# 	max_point = NEG_INF
# 	tmp, px, py, sign = 0, None, None, 1
# 	if player != org_player:
# 		sign = -1
# 	for y in range(TY):
# 		coord = turn(ar, y, player)
# 		if coord == ():
# 			continue
# 		tmp = score_pos(ar, coord, eval_func, player)
# 		if (tmp > max_point):
# 			max_point = tmp
# 			px = coord[0]
# 			py = coord[1]
# 		ar[coord[0]][coord[1]] = BLK
# 	return (sign*max_point, py)

def score_ar_z(ar, eval_func, player, org_player):
	sign = 1
	score = 0
	if player != org_player:
		sign = -1
	for x in range(TX):
		for y in range(TY):
			if ar[x][y] != BLK:
				score += score_pos(ar, (x,y), eval_func, player)
				if y == 3:
					score += 3
	return (sign*score, None)

def score_ar(ar, eval_func, player, org_player):
	max_point = NEG_INF
	tmp, px, py, sign = 0, None, None, 1
	if player != org_player:
		sign = -1
	for y in range(TY):
		cp_ar = deepcopy(ar)
		coord = turn(cp_ar, y, player)
		if coord == ():
			continue
		tmp = score_ar_z(cp_ar, eval_func, player, org_player)[0]
		if (tmp > max_point):
			max_point = tmp
			px = coord[0]
			py = coord[1]
		# ar[coord[0]][coord[1]] = BLK
	return (sign*max_point, py)