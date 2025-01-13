import os
import pandas as pd
import charset_normalizer
import fnmatch
import os
import os.path
import platform
import logging
import sys
def autoetlm():
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
		path=r"c:%HOMEPATH%\Downloads"
		u=os.path.expandvars(path)
		v=[]
		w=[]
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
	######################################################
		class NomeTabela:
			def __init__(self,*args):
				self.nt='tabela'
		nometabela=NomeTabela()
	######################################################
		w.pop(0)
		if platform.system()=='Windows':
				os.chdir(u+'\x5c')
		else:
				os.chdir(u+'/')
		for x in v:
			with open(x,'rb') as f1:
				data=f1.read()
				x1=data.decode(charset_normalizer.detect(data)['encoding'])
				x2=x1.encode(encoding='utf-8')
			with open(f'{nometabela.nt}.csv','wb') as f2:
				f2.write(x2)
		df=pd.read_csv(f'{nometabela.nt}.csv')
		# print(df.info())
		y1=int(input('N° de cópias do DataFrame: '))
		y2=int(input('N° de linhas do DataFrame: '))
		for num in range(y1):
			subset_df=df.sample(n=y2)
			subset_df.to_csv(f'{nometabela.nt+str(num)}.csv',sep=';',index=False)
	except Exception as e:
		logging.error(f"Um erro ocorreu: {str(e)}")	
		try:
			df=pd.read_csv(f'{nometabela.nt}.csv',sep=';')
		# print(df.info())
			y1=int(input('N° de cópias do DataFrame: '))
			y2=int(input('N° de linhas do DataFrame: '))
			for num in range(y1):
				subset_df=df.sample(n=y2)
				subset_df.to_csv(f'{nometabela.nt+str(num)}.csv',sep=';',index=False)
		except Exception as e:
			logging.error(f"Um erro ocorreu: {str(e)}")
			try:
				for f in os.listdir():
					df = pd.read_excel(f,engine='openpyxl')
					df.to_csv('X.csv', index=False,sep=';')
					fcsv=pd.read_csv(f'{nometabela.nt}.csv',sep=';')
					# print(df.info())
					y1=int(input('N° de cópias do DataFrame: '))
					y2=int(input('N° de linhas do DataFrame: '))
					for num in range(y1):
						subset_df=fcsv.sample(n=y2)
						subset_df.to_csv(f'{nometabela.nt+str(num)}.csv',sep=';',index=False)
			except Exception as e:
				logging.error(f"Um erro ocorreu: {str(e)}")
	
    
