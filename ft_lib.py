###############################
## Author: TRAN Quang Toan   ##
## Project Game Puissance 4  ##
## Version 1                 ##
## 10 Feb 2020               ##
###############################

import os
from termcolor import colored
from define import *

def getlist(n, c): ## creer une liste qui contient n fois charectere c
	lst = []
	for i in range(n):
		lst.append(c)
	return lst

def init_arena(nx, ny): ## creer une liste qui contient nx fois une liste 
	ar = []             ##  qui contient n fois la chaine de charactere BLK
	for i in range(nx): ## la boucle pour faire nx fois
		ar.append(getlist(ny, BLK))
	return ar

def turn(ar, y, player): ## On cherche l'axe x jusqu'a la position disponible
	for x in range(TX-1, -1, -1): 
		if ar[x][y] == BLK:
			ar[x][y] = player
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
		## Si il y a un x disponible, on l'ajoute dans la liste lst_y 
		for x in range(TX-1, -1, -1): 
			if ar[x][i] == BLK:
				lst_y.append(i)
				break
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
			if j != BLK:
				cj = colored(PLAYER_COLORED[j], 'white','on_white')
			else:
				cj = colored(BLK2, 'white','on_white')
			print(cj + CT, end='')
		print_c(29, BT)
	tmp = getlist2(TY)
	print(CT, end='')
	for j in tmp:
		cj = colored(j, 'blue','on_white', attrs=['bold'])
		print(cj + CT, end='')
	print_c(29, BT)
	
	# print("\n")
	# for i in ar:
	# 	for j in i:
	# 		print('[',j,']', end="")
	# 	print("\n")

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

def count(lst, c):
	ct = 0
	for i in lst:
		if i == c:
			ct += 1
	return ct

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
##
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
