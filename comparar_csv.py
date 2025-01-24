import pandas as pd
import fnmatch
import os
import os.path
from contextlib import redirect_stdout
import re
os.system('cls')
global v
w=[]
path=r"c:%HOMEPATH%\Downloads"
u=os.path.expandvars(path)
for file in os.listdir(u):
    if fnmatch.fnmatch(file,'*.csv'):
         v=file
         w.append(v)
os.chdir(u)
x=[]
for i in w:
    x.append(pd.read_csv(i,sep=';',encoding='utf-8'))
x[0].compare(x[1]).to_csv('X.csv',sep=';',encoding='utf-8')














    





