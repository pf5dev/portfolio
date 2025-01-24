import os
import unidecode
import re
from nltk.tokenize import word_tokenize, RegexpTokenizer
u1=0
#=========================================================

def w():
	a1=input("input string: ")
	global outstr
	outstr=unidecode.unidecode(a1)
	print(outstr)
	print("\n")

#=========================================================

def x(*args):
	p7=RegexpTokenizer(r'\w+')
	q7=p7.tokenize(s)
	p8=r'(\d+)'
	q8=[int(re.findall(p8, string)[0]) for string in q7 if re.findall(p8, string)]
	for l in range(len(q8)):
		print(q8[l],end='')

#=========================================================	
while u1 < 1:
	os.system("cls")
	a3=input('[1]-swapcase [2]-remover pontuação: ')
	if a3=='1':
		w()
		print(outstr.upper())
		print(outstr.lower())
	elif a3=='2':
		s=input('dígitos com pontuação: ')
		x()
		print('\n')
	a4=input('\ncontinuar [s]im ou [n]ao: \n')
	if a4=='s':
		continue
	elif a4=='n':
		break
	else:
		break

