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
	## NB_PLAYED: nombre de mouvements on a deja joue (0 <= NB_PLAYED <= 6*7=42)
	t, NB_PLAYED = 0, 0  ## t = 0 | 1 (player 0 | 1)
	arena = init_arena(TX, TY)
	print_arena(arena)
	##
	while (NB_PLAYED < TX*TY): ## Si NB_PLAYED < TX*TY (42): On continuera a jouer
		coord = ()
		s = "Choose your Move from 0 -> 6 \n  [ PLAYER "+str(t+1)+"] ("+PLAYER[t]+") : "
		s = colored(s, 'white', 'on_red', attrs=["bold"])
		y = choose_number(s, 0, 6, WARN_NUMBER) ## On saisit 0->6
		clear()
		coord = turn(arena, y, PLAYER[t]) ## On place la balle a la position y(0-6)
		
		if (coord == ()): ## Si la position y n'est pas valide => Il faut re-saisir y
			print_arena(arena)
			print(WARN_ILLEGALMOVE)
			continue
		
		print_arena(arena) ## Si la position y est valide
		                   ## On verifie si player t(0|1) a gagne et quitte la boucle
		if (is_winning_pos(arena, coord[0], coord[1])):
			print("\nFelicitation!! [ PLAYER", t+1, PLAYER[t], "] WON!!\n")
			break
		## Sinon, l'adversaire va jouer et le nombre mouvements +1
		t ,NB_PLAYED = 1 - t, NB_PLAYED + 1
		if (NB_PLAYED == TX*TY): ## Si NB_PLAYED == 42 et personne a gagne=> C'est Draw
			print(TIE)
			break

def Menu():
	print(COLORED_TITLE)
	n = choose_number(COLORDED_OPT, 1, 5, WARN_NUMBER_MENU)
	clear()
	if (n == 1):
		Normal_Game()         ## 2 Players
	elif (n == 2):
		AI_Mode(1)            ## StupidAI fait des randoms mouvements
	elif (n == 3):
		AI_Mode(2)            ## NormalAI cherche le meilleur mouvement avec evaluation function
	elif (n == 4):
		AI_Mode(3, 6)         ## MinimaxAI 
	elif (n == 5):
		AI_vs_AI(False, 6, 6) ##True:  NormalAI vs MinimaxAI
                              ##False: MinimaxAI vs MinimaxAI
                              ## Le but pout comparer entre les AIs et les fonctions evaluations
                              ## Et c'est pour tester des erreurs rapidement

######
# Le programme va commencer ici, par appeller la fonction Menu()
#
Menu()
#
#
##########