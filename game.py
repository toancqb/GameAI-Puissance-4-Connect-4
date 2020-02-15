from define import *
from tools import *
from AI_lib import *
from random import randrange
import sys 
from termcolor import colored, cprint

def is_winning_pos(ar, x, y):
	for i in range(-3, 1):
		if (y+i >= 0 and y+i+3 < TY):
			if (idm(ar[x][y+i], ar[x][y+i+1], ar[x][y+i+2], ar[x][y+i+3])):
				return True
		if (x+i >= 0 and x+i+3 < TX):
			if (idm(ar[x+i][y], ar[x+i+1][y], ar[x+i+2][y], ar[x+i+3][y])):
				return True
		if (x+i >= 0 and x+i+3 < TX and y+i >= 0 and y+i+3 < TY):
			if (idm(ar[x+i][y+i], ar[x+i+1][y+i+1], ar[x+i+2][y+i+2], ar[x+i+3][y+i+3])):
				return True
	ch = [[3,-3],[2,-2],[1,-1],[0,0]]
	for i in ch:
		if (check_range(x+i[0],0,TX-1) and check_range(y+i[1],0,TY-1)
			and check_range(x+i[0]-3, 0, TX-1) and check_range(y+i[1]+3, 0, TY-1)):
			if (idm(ar[x+i[0]][y+i[1]], ar[x+i[0]-1][y+i[1]+1]
				, ar[x+i[0]-2][y+i[1]+2], ar[x+i[0]-3][y+i[1]+3])):
				return True
	return False

def game():
	t = 0
	NB_PLAYED = 0
	arena = init_arena(TX, TY)
	print_arena(arena)
	while (NB_PLAYED < TX*TY):
		coord = ()
		s = "Chon vi tri tu 0-6\n  [ PLAYER "+str(t+1)+"] ("+PLAYER[t]+") : "
		s = colored(s, 'white', 'on_red', attrs=["bold"])
		try:
			y = int(input(s))
			if (y < 0 or y > 6):
				print(WARN_NUMBER)
				continue
		except ValueError:
			print(WARN_TYPE)
			continue
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

def idm2(player, a, b, c, d):
	odd_player = 0
	if (player == 0):
		odd_player = 1
	score, blank, piece = 0, 0, 0
	lst = [a,b,c,d]
	for i in lst:
		if (i == '   '):
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
	and (c == PLAYER[odd_player] and d == '   ')):
		score += 500
	
	return score


def score_pos(ar, coord, p):
	x = coord[0]
	y = coord[1]
	if (y == 3):
		score = 3
	else:
		score = 0
	for i in range(-3, 1):
		if (y+i >= 0 and y+i+3 < TY):
			score += idm2(p, ar[x][y+i], ar[x][y+i+1], ar[x][y+i+2], ar[x][y+i+3])
		
		if (x+i >= 0 and x+i+3 < TX):
			score += idm2(p, ar[x+i][y], ar[x+i+1][y], ar[x+i+2][y], ar[x+i+3][y])
		
		if (x+i >= 0 and x+i+3 < TX and y+i >= 0 and y+i+3 < TY):
			score += idm2(p, ar[x+i][y+i], ar[x+i+1][y+i+1], ar[x+i+2][y+i+2], ar[x+i+3][y+i+3])
	
	ch = [[3,-3],[2,-2],[1,-1],[0,0]]
	
	for i in ch:
		if (check_range(x+i[0],0,TX-1) and check_range(y+i[1],0,TY-1)
			and check_range(x+i[0]-3, 0, TX-1) and check_range(y+i[1]+3, 0, TY-1)):
			score += idm2(p, ar[x+i[0]][y+i[1]], ar[x+i[0]-1][y+i[1]+1]
				, ar[x+i[0]-2][y+i[1]+2], ar[x+i[0]-3][y+i[1]+3])

	return score

def score_ar(ar, player, sign):
	mn = cp_arena(ar)
	max_point = -100000000
	tmp, px, py = 0, None, None
	for y in range(TY):
		new_mn = cp_arena(mn)
		coord = turn(new_mn, y, PLAYER[player])
		if coord == ():
			continue
		tmp = score_pos(new_mn, coord, player)
		if (tmp > max_point):
			max_point = tmp
			px = coord[0]
			py = coord[1]
	return (sign * max_point, px, py)

def AI_Normal():
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
			mn = cp_arena(arena)
			m = score_ar(mn, 1, 1)
			y = m[2]

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

def max_eval(mn, result, cp_NB_PLAYED, alpha, beta, depth, prev_coord):
	if (depth == 0):
		return (score_pos(mn, prev_coord, 1), prev_coord[0], prev_coord[1])
	px, py, coord, m, max_v = None, None, (), (), -100000000
	if result == 1:
		return (1000000, prev_coord[0], prev_coord[1])
	elif result == 0:
		return (0, prev_coord[0], prev_coord[1])
	elif result == -1:
		return (-1000000, prev_coord[0], prev_coord[1])
	for y in range(TY):
		new_mn = cp_arena(mn)
		coord = turn(new_mn, y, PLAYER[1])
		if coord == ():
			continue
		px, py = coord[0], coord[1]
		if is_winning_pos(new_mn, coord[0], coord[1]):
			result = 1
		elif cp_NB_PLAYED + 1 == TX*TY:
			result = 0
		m = min_eval(new_mn, result, cp_NB_PLAYED + 1, alpha, beta, depth-1, coord)
		if (m[0] > max_v):
			max_v, px, py = m[0], m[1], m[2]
		if (alpha < max_v):
			alpha = max_v
		if (alpha >= beta):
			break
	return (max_v, px, py)

def min_eval(mn, result, cp_NB_PLAYED, alpha, beta, depth, prev_coord):
	if (depth == 0):
		sign = -1
		return (sign * score_pos(mn, prev_coord, 0), prev_coord[0], prev_coord[1])
	px, py, coord, m, min_v = None, None, (), (), 100000000
	if result == 1:
		return (1000000, prev_coord[0], prev_coord[1])
	elif result == 0:
		return (0, prev_coord[0], prev_coord[1])
	elif result == -1:
		return (-1000000, prev_coord[0], prev_coord[1])
	for y in range(TY):
		new_mn = cp_arena(mn)
		coord = turn(new_mn, y, PLAYER[0])
		if coord == ():
			continue
		px, py = coord[0], coord[1]
		if is_winning_pos(new_mn, coord[0], coord[1]):
			result = 1
		elif cp_NB_PLAYED + 1 == TX*TY:
			result = 0
		m = max_eval(new_mn, result, cp_NB_PLAYED + 1, alpha, beta, depth-1, coord)
		if (m[0] < min_v):
			min_v, px, py = m[0], m[1], m[2]
		if (beta > min_v):
			beta = min_v
		if (alpha >= beta):
			break
	return (min_v, px, py)

def minimax_AI(ar, NB_PLAYED, depth):
	mn = cp_arena(ar)
	cp_NB_PLAYED = cp_int(NB_PLAYED)
	(m, max_i, max_j) = max_eval(mn, 2, cp_NB_PLAYED, -100000000, 100000000, depth, ())
	return (m, max_j)

def AI_Minimax(depth):
	t = 0
	NB_PLAYED = 0
	arena = init_arena(TX, TY)
	print_arena(arena)
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
			m = minimax_AI(arena, NB_PLAYED, depth)
			y = m[1]
		#clear()
		if (t == 1):
			print(y, m[0])
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

def AI_Puissance4(AI_function):
	t = 0
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
			y = AI_function()
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

def menu():
	print(COLORED_TITLE)
	control = True
	while control:
		try:
			n = (int)(input(COLORDED_OPT))
			if (n < 1 or n > 4):
				print(WARN_NUMBER_MENU)
				continue
			control = False
		except ValueError:
			print(WARN_TYPE)
			continue

	if (n == 1):
		game()
	elif (n == 2):
		AI_Puissance4(stupid_AI)
	elif (n == 3):
		AI_Normal()		
	elif (n == 4):
		AI_Minimax(3)		

menu()