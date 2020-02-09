import os
import sys 
from termcolor import colored, cprint
from define import *

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
	tmp = getlist2(7)
	print(CT, end='')
	for j in tmp:
		cj = colored(j, 'blue','on_white', attrs=['bold'])
		print(cj + CT, end='')
	#print('')
	print_c(29, BT)