import pandas as pd
import fnmatch
import os
import os.path
import unidecode
import csv
import platform
from sqlalchemy import create_engine, text
import charset_normalizer
if platform.system()=='Windows':
	os.system('cls')
else:
	os.system('clear')
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
		self.a4='text'
		self.a5='db'
	def nomecoluna(self,*args):
		return i
c1=C1()
########################################################
def f0():
	l1=[]
	for x in v:
		with open(x,'rb') as f1:
			data=f1.read()
			x1=charset_normalizer.detect(data)
			l1.append(data.decode(x1['encoding']))
			for y in l1:
				if ';' in y:
					return ';'
				else:
					return ','
########################################################
if platform.system()=='Windows':
	os.chdir(u+'\x5c')
else:
	os.chdir(u+'/')
arqdir=list(enumerate(v))
print(arqdir)
p0=input('Arquivo *csv: ')
p1=input('Datatype [o]riginal ou [p]adrão(texto): ')
match p1:
	case 'o':
		df=pd.read_csv(c1.a3[int(p0)],sep=f'{f0()}')
		engine=create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/postgres')
		with engine.connect() as conn:
			df.to_sql(f'{c1.a1+p0}',engine,if_exists='replace',index=False)
	case 'p':
		for k in range(len(v)):
			num_str=str(k)
			with open(c1.a3[k],newline='',encoding='utf-8') as csvfile:
				A=csv.reader(csvfile,delimiter=f'{f0()}')
				for row in A:
					pass
					break						
			with open(f'{c1.a0+num_str}.sql','w') as f:
				f.write(f'CREATE DATABASE {c1.a5+num_str};\n')
				f.write(f'\c {c1.a5+num_str}\n')
				f.write(f'CREATE TABLE {c1.a1+num_str}(')
				for j,i in enumerate(row):
					i=unidecode.unidecode(i)
					if j == len(row)-1:
						f.write(f'"{c1.nomecoluna(i)}" {c1.a4});\n')
					else:								
						f.write(f'"{c1.nomecoluna(i)}" {c1.a4},\n')
				f.write(f'\d+ {c1.a1+num_str}\n')
				f.write(f"COPY {c1.a1+num_str} FROM '/docker-entrypoint-initdb.d/{c1.a3[k]}' DELIMITER \'{f0()}\' CSV HEADER;\n")

					









	




			
			
	
