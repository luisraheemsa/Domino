# Parte 1 Bloco 1

m = [(6,2),(5,5),(2,2),(3,4),(5,6),(4,2),(3,3)]

#P01

def pedrap(x,y):
    return [(x>=0 and x<=6) and (y>=0 and y<=6)]

#P02

def maop(m):
    if len(m)<=7:
        t = [True for x in m if pedrap(x[0],x[1])==True]
        if len(t)==len(m):
            return True
        else:
            return False

#P03

def carrocap(x,y):
    return((x>=0 and x<=6) and (y>=0 and y<=6) and (x==y))

#P4

def tem_carroca_p(m):
    t = [True for x in m if carrocap(x[0],x[1])]
    if len(t)>0:
        return True
    else:
        return False

#P5

def tem_carrocas(m):
    return [x for x in m if carrocap(x[0],x[1])]
