import sys 
from termcolor import colored, cprint

TITLE = '\n                             \n     [---PUISSANCE 4---]     \n                             '
COLORED_TITLE = colored(TITLE, 'red', 'on_white', attrs=['bold'])
TX = 6
TY = 7

CT = colored('|', 'cyan','on_white')
BT = colored('=', 'cyan','on_white')
PLAYER = [colored('-O-', 'red','on_yellow', attrs=['bold'])
	, colored('-X-', 'red','on_blue', attrs=['bold'])]
#NB_PLAYED = 0