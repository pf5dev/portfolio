import pandas as pd
import fnmatch
import os
import os.path
import re
import random
from nltk.tokenize import word_tokenize, RegexpTokenizer
from contextlib import redirect_stdout
#import matplotlib.pyplot as plt
#import seaborn 
#=================================================
os.system('cls')
path=r"c:%HOMEPATH%\Downloads"
u=os.path.expandvars(path)
for file in os.listdir(u):
	if fnmatch.fnmatch(file,'*.csv'):
		v=file
		w=u+"\x5c"+v
df=pd.read_csv(w,sep=";",encoding="latin_1")
#print(df.columns.values)
#print(set(df['Atividade (Ticket)'].tolist()))
#=================================================

def f1(*args):
	p1=RegexpTokenizer(r'\w+(?=\W)')
	q1=p1.tokenize(s1)
	return [print(n, end=" ") for n in q1]
	
#=================================================

def f2(*args):
	p2=RegexpTokenizer(r'\d{7}')
	q2=p2.tokenize(s3)
	return [print(rf, end=" ") for rf in q2]
	
#=================================================

def f3(*args):
	u=list(range(48,58))
	v=list(range(65,91))
	w=list(range(97,123))
	x=u+v+w
	y=list(random.choices(x,k=8))
	z=list(map(chr,y))
	z1=" ".join(z)
#	print(z1.replace(" ","",))
	z3=z1.replace(" ","",)
	return print(z3)

#=================================================

def f4(*args):
	p4=RegexpTokenizer(r'(\w+\.\w+@edu.sme.prefeitura.sp.gov.br)')
	q4=p4.tokenize(s3)
	return [print(s4, end=' ') for s4 in q4]
	
#=================================================

def f5(*args):
	p5=RegexpTokenizer(r'(\w+\.\w+@sme.prefeitura.sp.gov.br)')
	q5=p5.tokenize(s3)
	return [print(s5, end=' ') for s5 in q5]

#=================================================

def f6(*args):
	p6=RegexpTokenizer(r'(\w+@sme.prefeitura.sp.gov.br)')
	q6=p6.tokenize(s3)
	return [print(s6, end=' ') for s6 in q6]

#=================================================

def f7(*args):
	p7=RegexpTokenizer(r'\w+')
	q7=p7.tokenize(s3)
	p8=r'(\d+)'
	q8=[int(re.findall(p8, string)[0]) for string in q7 if re.findall(p8, string)]
	for l in range(len(q8)):
		print(q8[l],end='')
			
#=================================================

def f8(*args):
	p9_0=RegexpTokenizer(r'(wifi)',flags=re.I)
	q9_0=p9_0.tokenize(s3)
#	p9_1=RegexpTokenizer(r'(adm)')
#	q9_1=p9_1.tokenize(s3)	
	p9_2=RegexpTokenizer(r'(WI-FI)',flags=re.I)
	q9_2=p9_2.tokenize(s3)
	p9_3=RegexpTokenizer(r'(WI)\s*(FI)',flags=re.I)
	q9_3=p9_2.tokenize(s3)
	return q9_0+q9_2+q9_3

#=================================================
"""
for i in range(len(df)):
	a=df.loc[i,["Solicitante", "Atividade (Ticket)", "Descrição", "id Solicitacao Servico"]]
	s=a.tolist()
	s1,s2,s3,s4=s
	x=f8()
	if 'wifi' and 'adm' in x:
		print('wifi and adm')
	else:
		print('nok')
"""
with open('carimbo5.txt','w') as f:
	with redirect_stdout(f):
		print('#Cabeçalho=================================================\n')
		print('\nVerificado divergência entre a atividade prévia e a solicitação no campo descrição. Atividade alterada por esse motivo.\n')
		print('\nAtribuição de Licença Pacote Office 365\n\nPrezados,\n\nSegue para análise e Atribuição de Licença Pacote Office 365\n\nRF do beneficiário:\n\nNome Completo:\n\nE-mail (@sme):\n\nTipo de Licença (A3 ou A5):\n\nA3 - Servidores em exercício nas Unidades Educacionais (docentes, gestores, quadro de apoio e outros cargos com cadastro do EOL).\n\nA5 - Servidores em exercício nos Órgãos Administrativos (SME, DRE, COGEP, CODAE e outros de atendimento administrativo).\n')
		print('Caso continue com problemas para efetuar o login, será necessário procurar o responsável pelo SEI ADM. O TIC pode fornecer essa informação.\n')
		print('#Cabeçalho=================================================\n')
		for i in range(len(df)):
			a=df.loc[i,["Solicitante", "Atividade (Ticket)", "Descrição", "id Solicitacao Servico"]]
			s=a.tolist()
			s1,s2,s3,s4=s
			match s2:
				case "Criar Usuário do Domínio Educação" | "Alterar Senha - Domínio Educação":
					print('Ticket ',s4,'\n')
					print('Prezado(a)', end=" ")
					f1()
					print('a solicitação ',s2, 'foi realizada com sucesso, segue abaixo as informações para acesso:\n')
					print('Usuário: ', end=' ')
					f2()
					print('',end=' ')
					f7()
					print('\n\nSenha: ', end=' ')
					f3()
					print('\n\nAtenciosamente,\nN3Spassu/SMESP.\n')
				case "Recuperar Conta - E-mail @SME" | "Criar Conta - E-mail @SME" | "Alterar Senha - E-mail @SME":
					print('Ticket ',s4,'\n')
					print('Prezado(a)', end=" ")
					f1()
					print('a solicitação ',s2, 'foi realizada com sucesso, segue abaixo as informações para acesso:\n')
					print('Usuário: ', end=' ')
					f5()
					print('',end=' ')
					f6()
					print('\n\nSenha: ', end=' ')
					f3()
					print('\n\nAtenciosamente,\nN3Spassu/SMESP.\n')
				case "Alterar Senha - E-mail @edu" | "Criar Conta - E-mail @edu":
					print('Ticket ',s4,'\n')
					print('Prezado(a)', end=" ")
					f1()
					print('a solicitação ',s2, 'foi realizada com sucesso, segue abaixo as informações para acesso:\n')
					print('Usuário: ', end=' ')
					f4()
					print('\n\nSenha: 12345678', end=' ')
					print('\n\nAtenciosamente,\nN3Spassu/SMESP.\n')
				case "Permissão de Acesso a Caixa de Correio Compartilhada @SME" | "Remoção de Acesso a Caixa de Correio Compartilhada @SME":
					if s2=="Permissão de Acesso a Caixa de Correio Compartilhada @SME":
						print('Ticket ',s4,'\n')
						print('Prezado (a)', end=' ')
						f1()
						print(' permissão de acesso a caixa de correio compartilhada da UE',end=' ')
						print(' concedida com sucesso.\n\nImportante: pode demorar até 60 minutos para que a alteração seja efetivada no Outlook e no OWA.\n\nAtenciosamente,\nN3Spassu/SMESP.\n')
					elif s2=="Remoção de Acesso a Caixa de Correio Compartilhada @SME":
						print('Ticket ',s4,'\n')
						print('Prezado (a)', end=' ')
						f1()
						print(' remoção de acesso a caixa de correio compartilhada da UE',end=' ')
						print(' efetuada com sucesso.\n\nImportante: pode demorar até 60 minutos para que a alteração seja efetivada no Outlook e no OWA.\n\nAtenciosamente,\nN3Spassu/SMESP.\n')
				case "Licença Pacote Office 365":
					print('Ticket ',s4,'\n')
					print('Prezado (a)', end=' ')
					f1()			
					print(' solicitado atribuição de',s2,'pela Prodam conforme evidência anexa.',end=' ')
					print('\n\nAtenciosamente,\nN3Spassu/SMESP.\n')
				case "Listar Usuários com Permissão - Caixa Compartilhada @SME":
					print('Ticket ',s4,'\n')
					print('Prezado (a)', end=' ')
					f1()
					print(' para a solicitação',s2,'anexado evidência para comprovação.\n\nAtenciosamente,\nN3Spassu/SMESP.\n')
				case "Configurar Permissões de Pasta ou Arquivo de Rede":
					print('Ticket ',s4,'\n')
					print('Prezado (a)', end=' ')
					f1()
					print(' Concedido o acesso a pasta, conforme solicitado.\n\nPasta:\n\nNome do usuário:\n\nRF:', end=' ')	
					f2()
					print('',end=' ')
					f7()
					print('\n\nAtenciosamente,\nN3Spassu/SMESP.\n')
				case "Criar Usuário SEI" | "Alterar Senha SEI - Domínio Educação ":
					x=f8()
					if x!=[]:
						print('Ticket ',s4,'\n')
						print('Prezado(a)', end=" ")
						f1()
						print('a solicitação, foi realizada com sucesso, segue abaixo as informações para acesso:\n')
						print('Usuário: ', end=' ')
						f2()
						print('',end=' ')
						f7()
						print('\n\nSenha: ', end=' ')
						f3()
						print('\n\nAtenciosamente,\nN3Spassu/SMESP.\n')
					else:
						print('Ticket ',s4,'\n')
						print('Prezado(a)', end=" ")
						f1()
						print('a solicitação ',s2, 'foi realizada com sucesso, segue abaixo as informações para acesso:\n')
						print('Usuário: ', end=' ')
						f2()
						print('',end=' ')
						f7()
						print('\n\nSenha: ', end=' ')
						f3()
						print('\nCaso continue com problemas para efetuar o login, será necessário procurar o responsável pelo SEI ADM. O TIC pode fornecer essa informação. \n\nAtenciosamente,\nN3Spassu/SMESP.\n')
				case _:
					print('Ticket ',s4,'\n')
					print('Prezado(a)', end=" ")
					f1()
					print('a solicitação, foi realizada com sucesso, segue abaixo as informações para acesso:\n')
					print('Usuário: ', end=' ')
					f2()
					print('',end=' ')
					f7()
					print('\n\nSenha: ', end=' ')
					f3()
					print('\n\nAtenciosamente,\nN3Spassu/SMESP.\n')




	
	
	

