import pandas as pd
import fnmatch
import os
import os.path
import unidecode
import csv
import platform
import logging
import sys
import autoetlm
if platform.system()=='Windows':
	os.system('cls')
else:
	os.system('clear')
logging.basicConfig(level=logging.DEBUG)
file_handler = logging.FileHandler('erro.log')
file_handler.setLevel(logging.ERROR)
logging.getLogger().addHandler(file_handler)
sys.stderr = open('erro.log', 'w')
try:
	autoetlm.autoetlm()
	if platform.system()=='Windows':
		path=r"c:%HOMEPATH%\Downloads"
		u=os.path.expandvars(path)
	else:
		path=r"$HOME/Downloads"
		u=os.path.expandvars(path)
	v=[]
	w=[]
	for file in os.listdir(u):
		if fnmatch.fnmatch(file,'*.csv'):
				v.append(file)
				for m in range(len(v)):
					if platform.system()=='Windows':
						w.append(u+"\x5c"+v[m])
					w.append(u+"/"+v[m])
	if len(w)>1:
		w.pop(0)	
#######################################################
	class C1:
		def __init__(self,*args):
			self.a0='script'
			self.a1='tabela'
			self.a3=v
			self.a4='tabelasmod'
			self.a5='text'
		def nomecoluna(self,*args):
				return i
	c1=C1()
# #######################################################
	def myf0(*args):
		b1=list(enumerate(row))
		print(b1)
		print()		
		labeldt=input('INFORMAR DIGITO DA COLUNA E O TIPO DE DADO CORRESPONDENTE COMO \"0,text\" ou \"1,integer\", etc: ')
		b2=labeldt.split(',')
		return b2[1]
# #######################################################
	x=[]
	y=[]
	if platform.system()=='Windows':
		os.chdir(u+'\x5c')
	else:
		os.chdir(u+'/')
	# print(v)
	v.sort()
	os.rename(v[0],f'{v[0]}.txt')
	os.rename(v[1],f'{v[1]}.txt')
	p0=input('TIPO DE DADO PARA CADA COLUNA [m]anual ou [a]utomático: ')
	for k in range(2,len(v),1):
		num_str=str(k)
		with open(c1.a3[k],newline='',encoding='utf-8') as csvfile:
					A=csv.reader(csvfile,delimiter=';')
					for row in A:
						pass
						break						
					with open(f'{c1.a0+num_str}.sql','w') as f:
						x.append(f'{c1.a0+num_str}.sql')
						f.write(f'CREATE TABLE {c1.a1+num_str}(')
						for j,i in enumerate(row):
							i=unidecode.unidecode(i)
							if p0=='a':
								if j == len(row)-1:
									f.write(f'"{c1.nomecoluna(i)}" {c1.a5});\n')
								else:								
									f.write(f'"{c1.nomecoluna(i)}" {c1.a5},\n')
							elif p0=='m':
								if j == len(row)-1:
									f.write(f'"{c1.nomecoluna(i)}" {myf0()});\n')
								else:								
									f.write(f'"{c1.nomecoluna(i)}" {myf0()},\n')
						y.append(c1.a1+num_str)
						f.write(f"COPY {c1.a1+num_str} FROM '/docker-entrypoint-initdb.d/{c1.a3[k]}' DELIMITER ';' CSV HEADER;\n")																		
	if len(v)>1:
	# if len(w)>1:
		d=list(enumerate(v))
		print(d)
		num=int(input('Nº DO ARQUIVO *CSV QUE TERÁ COLUNA \"PRIMARY KEY\" NA TABELA CRIADA NO REPOSITÓRIO DE DADOS: '))	
		print()
		pfk_label=input('NOME(label) DA PRIMARY KEY: ')
		print()
		p,q=zip(*d)
		if q[num]==c1.a3[num]:
			arq=open(x[num],'a')
			arq.write(f'ALTER TABLE {y[num]} ADD COLUMN {pfk_label} SERIAL PRIMARY KEY;\n')
			arq.close()	
		x.pop(num)
		z=y[num]
		y.pop(num)
		with open(f'{c1.a4}.sql','w') as f:
				for e in range(len(x)):
					f.write(f'ALTER TABLE {y[e]} ADD COLUMN {pfk_label} SERIAL;\n')
					f.write(f'ALTER TABLE {y[e]} ADD CONSTRAINT fk FOREIGN KEY ({pfk_label}) REFERENCES {z} ({pfk_label});\n')
except Exception as e:
    logging.error(f"Um erro ocorreu: {str(e)}")
					









	




			
			
	
