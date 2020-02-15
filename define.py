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
WARN_NUMBER = colored("0 -> 6 Only, Please!", 'red', 'on_white', attrs=['bold'])
WARN_NUMBER_MENU = colored("1 -> 2 Only, Please!", 'red', 'on_white', attrs=['bold'])
WARN_TYPE = colored("Integer Only, Please type again!", 'red', 'on_white', attrs=['bold'])
WARN_ILLEGALMOVE = colored("Out of Range, Please try again!", 'red', 'on_white', attrs=['bold'])

COLORDED_OPT = colored("\n                             \n1. 2 Players                 \n2. vs Computer(StupidAI)     \n3. vs Computer(NormalAI)     \n4. vs Computer(MinimaxAI)    \n                             \n"
	, 'red', 'on_white', attrs=['bold'])
TIE = colored("It's a tie", 'red', 'on_white', attrs=["bold"])
CHOOSE_TURN = colored("\n Do you want to play first? \n Press 1 for YES \n Press 0 for NO\n", 'white', 'on_red', attrs=["bold"])