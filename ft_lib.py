###############################
## Author: TRAN Quang Toan   ##
## Project Game Puissance 4  ##
## Version 1                 ##
## 10 Feb 2020               ##
###############################

import os
from copy import deepcopy
from termcolor import colored
from define import BLK, TX, TY, WARN_TYPE, BT, CT, PLAYER, COLORED_TITLE

def cp_arena(ar): 
	mn = deepcopy(ar) ## Utilisation deepcopy pour faire la copie completement
	return mn

def getlist(n, c): ## creer une liste qui contient n fois charectere c
	lst = []
	for i in range(n):
		lst.append(c)
	return lst

def init_arena(nx, ny): ## creer une liste qui contient nx fois une liste 
	ar = []             ##  qui contient n fois la chaine de charactere BLK
	for i in range(nx):
		ar.append(getlist(ny, BLK))
	return ar

def turn_to_x_y(ar, x, y, player): ## PLacer la balle a la position (x, y)
	ar[x][y] = player

def turn(ar, y, player): ## On cherche l'axe x jusqu'a la position disponible
	for x in range(TX-1, -1, -1):
		if is_pos_blank(ar, x, y) == True:
			turn_to_x_y(ar, x, y, player)
			return (x, y)
	return ()

def clear(): ## On efface l'ecran terminal sur Linux
	os.system('clear')

def fclear(): ## J'ai trouve la solution sur internet pour effacer terminal 
    os.system('cls' if os.name=='nt' else 'clear') ## sur Windows ou Linux

def print_c(n, c): ## Print n fois charactere c
	s = c * n
	print('\n' + s)

def lst_applicable(ar, n, p): ## On cherche des positions disponibles pour jouer
	lst_y = []
	for i in range(n): ## Pour chaque position l'axe y, on cherche position l'axe x
		mn = cp_arena(ar) ## Si il y a un x disponible, on l'ajoute dans la liste lst_y 
		coord = turn(mn, i, PLAYER[p])
		if coord == ():
			continue
		lst_y.append(i)
	return lst_y

def lst_applicable2(ar, n, p): ## Simplifier la fonction de lst_applicable
	lst_y = []
	for y in range(n):
		for x in range(TX-1, -1, -1):
			if is_pos_blank(ar, x, y) == True:
				lst_y.append(y)
	return lst_y

def getlist2(n): ## Creer une liste qui contien ' 0 ',' 1 ',' 2 '...
	lst = []
	for i in range(n):
		lst.append(' '+str(i)+' ')
	return lst

def print_arena(ar): ## Imprimer Arena Puissance 4
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

def idm(a, b, c, d): ## Verifier Si a,b,c,d ont le meme valeur sauf que BLK
	if (a == BLK or b == BLK or c == BLK or d == BLK):
		return False
	if (a == b and b == c and c == d):
		return True
	return False

def check_range(n, a, z): ## Verifier si le numero n est entre a et z
	if (n >= a and n <= z):
		return True
	return False

###################################################
# Pour chaque position (x, y)
# On verifie:
# [  ][--][  ][==][  ][--][  ] 
# [  ][  ][--][==][--][  ][  ]
# [==][==][==][xy][==][==][==]
# [  ][  ][--][==][--][  ][  ]
# [  ][--][  ][==][  ][--][  ]
# [--][  ][  ][==][  ][  ][--]
##
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
##
######################################################

def choose_number(str, i_min, i_max, warning): ## Saisir le numero
	while True:
		try:
			y = int(input(str))
			if (y < i_min or y > i_max): ## Le numero doit etre entre i_min et i_max
				print(warning)
				continue
			break
		except ValueError: ## Si le numero saisi n'est pas integer, il faut refaire
			print(WARN_TYPE)
			continue
	return y
