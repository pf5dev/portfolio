import os
import charset_normalizer
import fnmatch
import os
import os.path
import platform
import logging
import sys
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
######################################################
	w.pop(0)
	if platform.system()=='Windows':
			os.chdir(u+'\x5c')
	else:
		os.chdir(u+'/')
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
except Exception as e:
	logging.error(f"Um erro ocorreu: {str(e)}")	
		