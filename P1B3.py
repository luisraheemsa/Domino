# Parte 1 Bloco 3

#P17

def mesap(q):
            return len(q)>=0 and len(q)<=4


#P18
def carroca_m_p((a, b, c, d)):
	y = (1==0)
	if y == (1==0):
		for i in (a, b, c, d):
			if ((len(i) == 2) and (i[0] == i[1])) : y = not(y)
	return y

#P19
def pontos_marcados(a):
	y = 0
	for i in a:
		if len (i) == 1 : y = y + i[0]
		elif len (i) == 2 : y = y + i[0] + i[1]
	if y%5 == 0 : return y
	else : return 0

#P20
def pode_jogar_p((a, b), (c, d, e, f)):
	y = (1==0)
	for i in (c, d, e, f):
		if y == (1==0):
			if i != [] : y = (i[0] == a or i[0] == b)
	return y



#P21
def marca_ponto_p((a, b), c):
	if maior_ponto((a, b), c) >= 0 : return (1==1)
	else : return (1==0)


		return (r[1], r[2])
	else : return None
	

