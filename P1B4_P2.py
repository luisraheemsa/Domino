# Parte 1 Bloco 4

#P27

def lista_de_jogadas(xs):
	xs = [xs[i] for i in range(0,len(xs)-1) if (xs[i][1]==xs[i+1][0]) == False]
	return xs == []

#P28	
def mesa2p(m1,m2):
	chk = [True for i in range(0,len(m2[1:])) if m1[i][0]==m2[i+1][0][0]]
	return chk != []

#P29
def marca_ponto_2(xs):
	chk == sum([x[0][0] for x in xs[1:]])
	if chk%5==0:
		return chk
	else:
		return 0

#P30		
def faz_jogada_2(a,xs,c):
	r = [a] + xs[c+1]
	xs[c+1] = r
	return xs
	

#P31	
def pedras_de_ponto(m1):
    return [d[i] for i in range(0,len(d)) if marca_ponto_p(d[i],m[1]) == True]

def junta(a,b):
	return a+b

#P34
def pedras_fora_p(m2):
	return [x for x in d if x not in reduce(junta,m2)]

# Parte 2 - Tuplas e Listas em Geral

 #P35                                             
def somavet(a,b):
    return (a[0]+b[0],a[1]+b[1])
#P36    
def sumdo(n):
	return [(a,b) for a in range(0,n) for b in range(a,n) if a+b==n]
#P37
def alterna(l):
    
    return l.sort()

#P38
def intersec(l,lk):
    return [x for x in l if l in lk]

#P39
def uni(l,lk):
    a = l + lk
    return list(set(a))
