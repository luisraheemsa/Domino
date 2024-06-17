# Parte 1 Bloco 2

#P6
def pontos(m):
    soma=[x[0]+x[1] for x in m]
    return sum(soma)

#P7
def garagem(m):
    soma=[x[0]+x[1] for x in m]
    x=sum(soma)
    r=x%5
    return x-r

#P8
def pedra_igual_p(x,y):
    return((x[0]==y[0] or x[0]==y[1]) and (x[1]==y[0] or x[1]==y[1]))

#P9
def ocorre_pedra_p(pedra, mao):
    return pedra in mao

#P10   
def ocorre_valor_p(v, mao):
    x=[True for x in mao if (v==x[0] or v==x[1])]
    if len(x)>0:
        return True
    else:
        return False

#P11
def ocorre_pedra(pedra, mao):
    lis=[x for x in mao if pedra in mao]
    if len(lis)>0:
        return lis
    else:
        return False

#P12
def pedra_maior(mao):
    soma=[x[0]+x[1] for x in mao]
    i = soma.index(max(soma))
    return mao[i]

#P13    
def ocorre_valor_q(v,mao):
   x=[True for x in mao if (v==x[0] or v==x[1])]
   return len(x)

#P14
def ocorre_carroca_q(mao):
    x = [x for x in mao if x[0]==x[1]]
    return len(x)

#P15
def tira_maior(mao):
    soma=[x[0]+x[1] for x in mao]
    i = soma.index(max(soma))
    del mao[i]
    return mao

#P16
def tira_maior_v(v,mao):
    lis_m=[x for x in mao if (v==x[0] or v==x[1])]
    soma=[x[0]+x[1] for x in lis_m]
    i = soma.index(max(soma))
    del mao[i]
    return mao
    return mao

