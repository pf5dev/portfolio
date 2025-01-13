import random
from contextlib import redirect_stdout
import os
os.system('cls')
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
	while z3.isalpha()==True:
			s1=random.choice(z3)
			s2=random.choice(['0','1','2','3','4','5','6','7','8','9'])
			z4=z3.replace(s1,s2)
			return z4
	return z3
a1=input("N° vezes pwdgen: ")
a2=int(a1)
i1=1
with open('pwdgen2.txt','w') as f:
	f.write('Caso continue com problemas para efetuar o login, será necessário procurar o responsável pelo SEI ADM. O TIC pode fornecer essa informação.')
	f.write('\n\n')
	with redirect_stdout(f):
		while i1 <= a2:
			print(f'{f3()},',end='')
			i1+=1
	

