###############################
## Author: TRAN Quang Toan   ##
## Project Game Puissance 4  ##
## Version 1                 ##
## 10 Feb 2020               ##
###############################

from define import *
from ft_lib import *
from AI_lib import *
from termcolor import colored

def Normal_Game():
	t, NB_PLAYED = 0, 0
	arena = init_arena(TX, TY)
	print_arena(arena)
	while (NB_PLAYED < TX*TY):
		coord = ()
		s = "Choose your Move from 0 -> 6 \n  [ PLAYER "+str(t+1)+"] ("+PLAYER[t]+") : "
		s = colored(s, 'white', 'on_red', attrs=["bold"])
		y = choose_number(s, 0, 6, WARN_NUMBER)
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

def Menu():
	print(COLORED_TITLE)
	n = choose_number(COLORDED_OPT, 1, 5, WARN_NUMBER_MENU)
	clear()
	if (n == 1):
		Normal_Game()         ## 2 Players
	elif (n == 2):
		AI_Mode(1)            ## StupidAI
	elif (n == 3):
		AI_Mode(2)            ## NormalAI
	elif (n == 4):
		AI_Mode(3, 6)         ## MinimaxAI
	elif (n == 5):
		AI_vs_AI(False, 6, 6) ##True:  NormalAI vs MinimaxAI
                              ##False: MinimaxAI vs MinimaxAI

Menu()
