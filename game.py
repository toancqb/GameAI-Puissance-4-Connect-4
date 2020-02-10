from define import *
from tools import *
from AI_lib import *
from random import randrange
import sys 
from termcolor import colored, cprint

def init_arena(nx, ny):
	ar = []
	for i in range(nx):
		ar.append(getlist(ny, '   '))
	return ar

def turn_to_x_y(ar, x, y, player):
	ar[x][y] = player 

def turn(ar, y, player):
	for i in range(TX-1, -1, -1):
		if is_pos_blank(ar, i, y) == True:
			turn_to_x_y(ar, i, y, player)
			return (i, y)
	return ()

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
		s = "Chon vi tri tu 0-6\n[ PLAYER "+str(t+1)+"] ("+PLAYER[t]+") : "
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
			print("Hoa roi")
			break

def stupid_AI():
	n = randrange(7)
	return n

#def minimax_AI(ar):
#	mn = cp_arena(ar)


def AI_Puissance4(AI_function):
	t = 0
	NB_PLAYED = 0
	arena = init_arena(TX, TY)
	print_arena(arena)
	while (NB_PLAYED < TX*TY):
		coord = ()
		s = "Chon vi tri tu 0-6\n[ PLAYER "+str(t+1)+"] ("+PLAYER[t]+") : "
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
			print("Hoa roi")
			break

def menu():
	print(COLORED_TITLE)
	control = True
	while control:
		try:
			n = (int)(input(COLORDED_OPT))
			if (n < 1 or n > 2):
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

#game()
menu()