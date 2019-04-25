import random

def expoS(x,y) :
    r=x
    for i in range(int(y)-1) :
        r=r*x
    return(r)

def expo(x,y) :
    i = int(y)
    m=x
    r=0
    while i>0 :
        if i%2==0 :
            i=i/2
        else :
            r+=m
            i=(i-1)/2
        m = m * m
    return(r)

def tritoporecu(s, gra , Lsor, Lsmar=[]):
    Lsmar.append(s) #placer s dans la liste des sommets marqués
    for elt in gra[s] :#pour chaque voisin x de s:
        if not elt in Lsmar :#si x n’a pas été marqué:
            tritoporecu(elt, gra, Lsor, Lsmar)
    Lsor.append(s) #placer s au début de la_liste_des_sommets_ordonnées

def tritoporecu2(s, gra , Lsor, Lsmar=[]):
    Lsmar.append(s) #placer s dans la liste des sommets marqués
    t=randolist(gra[s])
    #print(t)#debug
    for elt in t :#pour chaque voisin x de s:
        if not elt in Lsmar :#si x n’a pas été marqué:
            tritoporecu(elt, gra, Lsor, Lsmar)
    Lsor.append(s) #placer s au début de la_liste_des_sommets_ordonnées

def recugraph (graph) :
    f=open(graph)
    C=f.read()
    #print(C)#débug
    L=C.split("\n")
    #print(L)#débug
    f.close()
    for i in range(len(L)) :
        L[i]=L[i].split(",")
    #print("chiffre")#débug
    for i in range(len(L)) :
        if L[i] != [''] :
            for j in range(len(L[i])) :
                #print(L[i][j])#débug
                L[i][j]=int(L[i][j])
        else :
            L[i]=[]
    return(L)

def recucor (cor) :
    f=open(cor)
    C=f.read()
    #print(C)#débug
    L=C.split("\n")
    #print(L)#débug
    f.close()
    return (L)

def saveresu (R,C,cible) :
    f=open(cible,"w")
    for elt in R:
        if elt != 0:
            f.write(C[elt-1])
            f.write("\n")
    f.close()
    return(0)

def randolist (L) :
    Lc=L[:]
    A=[]
    for i in range(len(L)) :
        a= random.randint(0,len(Lc)-1)
        A.append(Lc.pop(a))
    return(A)