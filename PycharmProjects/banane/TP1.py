try:
    f = open('ventes.csv','r')
except IOError:
    print("Erreur d'ouverture!")

s = f.readline()
attr=s.split(',')
m=len(attr)
print(attr)
M=[]
for i in range(m) :
    M.append([])


s = f.readline()
while s!="" :
    val=s.split(',')
    s = f.readline()
    for i in range(m) :
        M[i].append(val[i])
f.close()


MONTANT=3
NOM_CONTACT=20
PAYS=18
QUANTITE=1
PRIX_UNITAIRE=2
MONTANT =3
#print(M)
#print(M[NOM_CONTACT],"\n",M[MONTANT])


f = open('ventes.csv','r')
liste_lignes = f.readlines()

try :
    print(liste_lignes[7])
except :
    print("tp de M")

f.close()


import csv

flux_de_tuples = csv.reader(open("ventes.csv","r"))



Ltup=[]
for e in flux_de_tuples :
    Ltup.append([])
    for elt in e :
        Ltup[-1].append(elt)
liste_pays=[]
for e in Ltup :
    p=e[PAYS]
    if not p in liste_pays:
        liste_pays.append(p)
print(liste_pays)


def Pv (ft,pays) :
    t=0
    #print('ok')
    for e in ft :
        #print(e[PAYS])
        if e[PAYS]==pays :
            t+=1
    return (t)
vf=Pv(Ltup,liste_pays[2])
print(vf)

def Pvm (ft,pays) :
    t=0
    #print('ok')
    for e in ft :
        #print(e[PAYS])
        if e[PAYS]==pays :
            t+=e[MONTANT]
    return (t)

def lvP (ft,Lpays) :
    Lr=[]
    a=0
    for p in Lpays:
        a=Pv(ft,p)
        Lr.append([p,a])
    return Lr

def lvPm (ft,Lpays) :
    Lr=[]
    a=0
    for p in Lpays:
        a=Pvm(ft,p)
        Lr.append([p,a])
    return Lr

Lr=lvP(Ltup,liste_pays)

print(Lr)



for e in Ltup :
    if e[PAYS] == 'United States' :
        e[PAYS]='USA'

l=0
for e in Ltup :
    if l!=0 :
        #print([e[QUANTITE]],e[PRIX_UNITAIRE])
        e[MONTANT] = int(e[QUANTITE]) * float(e[PRIX_UNITAIRE])
    else:
        l+=1
    #e[MONTANT]=int(e[QUANTITE])*float(e[PRIX_UNITAIRE])


liste_pays=[]
for e in Ltup :
    p=e[PAYS]
    if not p in liste_pays:
        liste_pays.append(p)

Lr=lvP(Ltup,liste_pays)
print(Lr)
Lrm=lvPm(Ltup,liste_pays[1:])
print(Lrm)

g = open('ventes_corrige.csv','w')
flux_de_sortie = csv.writer(g, delimiter = ",")
for lelt in Ltup :
    flux_de_sortie.writerow(lelt)

flux_de_sortie.writerow(e)
g.close()
"""
d = liste_dict[i]
e = [d[attr[j]] for j in range(m)]
flux_de_sortie.writerow(e)
"""

import json

h = open("ventes_corrige.json", "w")

json.dump(Ltup, h, sort_keys=True, indent=4)
h.close()

fh = open("ventes_corrige.json", "r")
liste_dict_new = json.load(fh)
fh.close()
