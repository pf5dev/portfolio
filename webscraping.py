import os
import re
from bs4 import BeautifulSoup
import subprocess
from datetime import datetime
os.system('cls')
def ping(host):
    response=subprocess.run(['ping','-n','1',host],stdout=subprocess.DEVNULL)
    return response
l1=[]
with open(r'C:\Users\268903258\Downloads\Zabbix Escolas_ Hosts.html','r',encoding='utf-8') as f:
    soup=BeautifulSoup(f,'html.parser')
for x in soup.find_all('td',class_='nowrap'):
    for y in x.contents:
        z=str(y.string)
        i=re.search(r'(\d*.\d*.\d*.\d*)',z)
        l1.append(i.group(0))
l1.pop(0)
l2=[]
with open(r'C:\Users\268903258\Downloads\Zabbix Escolas_ Hosts.html','r',encoding='utf-8') as f:
    soup=BeautifulSoup(f,'html.parser')
for m in soup.find_all('a',class_='link-action'):
    for n in m.contents:
        o=str(n.string)
        l2.append(o)
l3=[]
for ping_host in l1:
    str(l3.append([ping(ping_host),datetime.now().strftime('%d/%m/%Y %H:%M')]))
res=[]
for g in range(len(l2)):
    res.append(l2[g]+' '+str(l3[g]))
#print(res)
with open('teste.txt','w') as f:
    for txt in res:
        f.write(f'{txt};\n')
os.rename(r'C:\Users\268903258\Documents\scripts_py\webscraping\teste.txt',r'C:\Users\268903258\Documents\scripts_py\webscraping\teste.csv')
    
