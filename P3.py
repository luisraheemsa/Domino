# Parte 3 - Processamento de Cadeia de Caracteres

#40
def e_palav(l):
	return l.isalpha()
#41	
def e_int(l):
	return l.isdigit()

#42
def conjuga(v,t):
	if v[len(v)-2]=='a' and t=='presente':
		c=v.split('ar')
		k=c[0]
		conj=['o'.join(k),'as'.join(k),'a'.join(k),'amos'.join(k),'ais'.join(k),'am'.join(k)]
		y=[pe[i]+conj[i] for i in range(6)]
		return(y)
	elif v[len(v)-2]=='a' and t=='passado':
		c=v.split('ar')
		k=c[0]
		conj=['ava'.join(k),'avas'.join(k),'ava'.join(k),'avamos'.join(k),'avais'.join(k),'avam'.join(k)]
		y=[pe[i]+conj[i] for i in range(6)]
		return(y)	
	elif v[len(v)-2]=='a' and t=='futuro':
		c=v.split('ar')
		k=c[0]
		conj=['arei'.join(k),'ara'.join(k),'ara'.join(k),'aremos'.join(k),'arais'.join(k),'arao'.join(k)]
		y=[pe[i]+conj[i] for i in range(6)]
		return(y)
	elif v[len(v)-2]=='e' and t=='presente':
		c=v.split('er')
		k=c[0]
		conj=['o'.join(k),'es'.join(k),'e'.join(k),'emos'.join(k),'eis'.join(k),'em'.join(k)]
		y=[pe[i]+conj[i] for i in range(6)]
		return(y)
	elif v[len(v)-2]=='e' and t=='passado':
		c=v.split('er')
		k=c[0]
		conj=['ia'.join(k),'ias'.join(k),'ia'.join(k),'iamos'.join(k),'ieis'.join(k),'iam'.join(k)]
		y=[pe[i]+conj[i] for i in range(6)]
		return(y)
	elif v[len(v)-2]=='e' and t=='futuro':
		c=v.split('er')
		k=c[0]
		conj=['erei'.join(k),'erais'.join(k),'era'.join(k),'eremos'.join(k),'erais'.join(k),'erao'.join(k)]
		y=[pe[i]+conj[i] for i in range(6)]
		return(y)
	elif v[len(v)-2]=='i' and t=='presente':
		c=v.split('ir')
		k=c[0]
		conj=['o'.join(k),'es'.join(k),'e'.join(k),'imos'.join(k),'ies'.join(k),'em'.join(k)]
		y=[pe[i]+conj[i] for i in range(6)]
		return(y)
	elif v[len(v)-2]=='i' and t=='passado':
		c=v.split('ir')
		k=c[0]
		conj=['i'.join(k),'ies'.join(k),'iu'.join(k),'imos'.join(k),'ies'.join(k),'iram'.join(k)]
		y=[pe[i]+conj[i] for i in range(6)]
		return(y)
	else v[len(v)-2]=='i' and t=='futuro':
		c=v.split('ir')
		k=c[0]
		conj=['irei'.join(k),'iras'.join(k),'ira'.join(k),'iremos'.join(k),'irais'.join(k),'irao'.join(k)]
		y=[pe[i]+conj[i] for i in range(6)]
		return(y)
#43		
def e_float(l):
	 if '.' in l:
		t=''.join(l.split('.'))
		return (t.isdigit())
#44	 
def int_frac(l):
	a=l.isdigit()
	if a==True:
		v=(l+','+'0')
		return (con)
	else:
		if e_float(l)==True
			w= l.split('.')
			return (w)
#45		
def traduz(l):
	u=['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
	d=['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'oitenta', 'noventa']
	if l[0]==0:
		x=[u[l[1]-1]]
		return (x)
	elif l[0]==1:
		if l[1]==1:return ('onze')
		elif l[1]==2: return ('doze')
		elif l[1]==3: return ('treze')
		elif l[1]==4: return ('quatorze')
		elif l[1]==5: return ('quinze')
		elif l[1]==6: return ('dezesseis')
		elif l[1]==7: return ('dezessete')
		elif l[1]==8: return ('dezoito')
		elif l[1]==9: return ('dezenove')
	else:
		x=[d[l[0]-1]+'e'+u[p[1]-1]]
		return (x)
		
