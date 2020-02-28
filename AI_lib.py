from define import *
from ft_lib import *
from random import randrange

def idm2(player, a, b, c, d):
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
		score += 90

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

def minimax(ar,player,org_player,NB_PLAYED,depth,result,calc_func,a,b):
	if result == 1:
		return (1000000, None)
	elif result == 0:
		return (0, None)
	elif result == -1:
		return (-1000000, None)
	if (depth == 0):
		m = score_ar(ar, calc_func, player,org_player)
		return (m[0], m[1])
	coord = ()
	if player == org_player: # Maximal Player
		max_v, py = NEG_INF, None
		for y in range(TY):
			cp_ar = cp_arena(ar)
			coord = turn(cp_ar, y, PLAYER[player])
			if coord == ():
				continue
			if is_winning_pos(cp_ar, coord[0], coord[1]):
				result = 1
			elif NB_PLAYED == TX*TY:
				result = 0
			score = minimax(cp_ar,1-player,org_player,NB_PLAYED+1,depth-1,result,calc_func,a,b)
			if score[0] > max_v:
				max_v = score[0]
				py = coord[1]
			if a < max_v:
				a = max_v
			if a >= b:
				break
		return (max_v, py)
	else: # Minimal Player
		min_v, py = INF, None
		for y in range(TY):
			cp_ar = cp_arena(ar)
			coord = turn(cp_ar, y, PLAYER[player])
			if coord == ():
				continue
			if is_winning_pos(cp_ar, coord[0], coord[1]):
				result = -1
			elif NB_PLAYED == TX*TY:
				result = 0
			score = minimax(cp_ar,1-player,org_player,NB_PLAYED+1,depth-1,result,calc_func,a,b)
			if score[0] < min_v:
				min_v = score[0]
				py = coord[1]
			if b > min_v:
				b = min_v
			if a >= b:
				break
		return (min_v, py)

#######################################

def AI_Mode(mode=2, depth=3):
	NB_PLAYED = 0
	arena = init_arena(TX, TY)
	print_arena(arena)
	while True:
		try:
			y = int(input(CHOOSE_TURN))
			if (y < 0 or y > 1):
				print(WARN_NUMBER)
				continue
			break
		except ValueError:
			print(WARN_TYPE)
			continue
	t = 1 - y
	while (NB_PLAYED < TX*TY):
		coord = ()
		s = "Chon vi tri tu 0-6\n  [ PLAYER "+str(t+1)+"] ("+PLAYER[t]+") : "
		s = colored(s, 'white', 'on_red', attrs=["bold"])
		if (t == 0):
			try:
				y = int(input(s))
				if (y < 0 or y > 6):
					print(WARN_NUMBER)
					continue
			except ValueError:
				print(WARN_TYPE)
				continue
		else:
			if mode == 1:
				y = randrange(TY)
			elif mode == 2:
				y = score_ar(arena,idm2,t,t)[1]
			elif mode == 3:
				y = minimax(arena,t,t,NB_PLAYED,depth,2,idm3,NEG_INF,INF)[1]

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
			y = minimax(arena,t,t,NB_PLAYED,depth2,2,idm3,NEG_INF,INF)[1]
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
