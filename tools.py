import os
import sys
import copy
from termcolor import colored, cprint
from define import *


#def convert_list_to_tuple(ar):
#	return tuple(ar)

#def convert_tuple_to_list(ar):
#	return list(ar)

#def cp_arena(ar):
#	ab = convert_tuple_to_list(ar)
#	mn = ab.copy()
#	mm = convert_list_to_tuple(mn)
#	return mm

def cp_arena(ar):
	mn = copy.deepcopy(ar)
	return mn

def init_arena(nx, ny):
	ar = []
	for i in range(nx):
		ar.append(getlist(ny, '   '))
#	arena_tuple = convert_list_to_tuple(ar)
#	return arena_tuple
	return ar

def turn_to_x_y(ar, x, y, player):
	ar[x][y] = player 

def turn(ar, y, player):
	for x in range(TX-1, -1, -1):
		if is_pos_blank(ar, x, y) == True:
			turn_to_x_y(ar, x, y, player)
			return (x, y)
	return ()

def cp_int(n):
	m = n
	return m

def clear():
   os.system('clear')

def print_c(n, c):
	s = c * n
	print('\n' + s)

def getlist(n, c):
	lst = []
	for i in range(n):
		lst.append(c)
	return lst

def getlist2(n):
	lst = []
	for i in range(n):
		lst.append(' '+str(i)+' ')
	return lst

def print_arena(ar):
	print(COLORED_TITLE)
	print_c(29, BT)
	for i in ar:
		print(CT, end='')
		for j in i:
			cj = colored(j, 'white','on_white')
			print(cj + CT, end='')
		print_c(29, BT)
	tmp = getlist2(TY)
	print(CT, end='')
	for j in tmp:
		cj = colored(j, 'blue','on_white', attrs=['bold'])
		print(cj + CT, end='')
	print_c(29, BT)

def is_pos_blank(ar, x, y):
	return (ar[x][y] == '   ')

def lst_pos_y_playable(ar, player):
	mn = cp_arena(ar)
	lst_y = []
	for y in range(TY):
		new_mn = cp_arena(mn)
		if turn(new_mn, y, player) != ():
			lst_y.append(y)
	return lst_y


def idm(a, b, c, d):
	if (a == '   ' or b == '   ' or c == '   ' or d == '   '):
		return False
	if (a == b and b == c and c == d):
		return True
	return False

def check_range(n, a, z):
	if (n >= a and n <= z):
		return True
	return False