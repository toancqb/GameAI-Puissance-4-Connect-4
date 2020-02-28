###############################
## Author: TRAN Quang Toan   ##
## Project Game Connect 4    ##
## Version 1 		    	 ##
## 10 Feb 2020		     	 ##
###############################

from os import system
from copy import deepcopy
from termcolor import colored
from define import *

def cp_arena(ar):
	mn = deepcopy(ar)
	return mn

def init_arena(nx, ny):
	ar = []
	for i in range(nx):
		ar.append(getlist(ny, BLK))
	return ar

def turn_to_x_y(ar, x, y, player):
	ar[x][y] = player

def turn(ar, y, player):
	for x in range(TX-1, -1, -1):
		if is_pos_blank(ar, x, y) == True:
			turn_to_x_y(ar, x, y, player)
			return (x, y)
	return ()

def clear():
   system('clear')

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
	return (ar[x][y] == BLK)

def idm(a, b, c, d):
	if (a == BLK or b == BLK or c == BLK or d == BLK):
		return False
	if (a == b and b == c and c == d):
		return True
	return False

def check_range(n, a, z):
	if (n >= a and n <= z):
		return True
	return False

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
