from random import randrange
from define import *

lst = [1, 2, 3]

def cp_arena(ar):
	mn = ar.copy()
	return mn

def test(lst):
	mn = cp_arena(lst)
	mn[1] = 'one'
	return mn

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
		if (i == '   '):
			blank += 1
		if (i == PLAYER[odd_player]):
			piece += 1
	if (piece == 3 and blank == 1):
		score -= 50
	blank, piece = 0, 0
	for i in lst:
		if (i == PLAYER[player]):
			blank += 1
		if (i == PLAYER[odd_player]):
			piece += 1
	if (piece == 3 and blank == 1):
		score += 10000

	return score



player = 1
odd_player = 0
score = idm2(player, PLAYER[odd_player], PLAYER[player], PLAYER[odd_player], PLAYER[odd_player])
print(score)