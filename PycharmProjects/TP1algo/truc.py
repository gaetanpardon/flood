"""
L=[[1,2,3,6],[],[4],[5],[5,8],[],[7,8],[9],[9],[]]
c=["montre1","caleçon2","chaussette3","pantalon4","chaussure5","chemise6","cravate7","ceinture8","veste9"]

def tritoporecu(s, gra , Lsor, Lsmar):
    Lsmar.append(s) #placer s dans la liste des sommets marqués
    for elt in gra[s] :#pour chaque voisin x de s:
        if not elt in Lsmar :#si x n’a pas été marqué:
            tritoporecu(elt, gra, Lsor, Lsmar)
    Lsor.append(s) #placer s au début de la_liste_des_sommets_ordonnées

R=[]
Lmar=[]
tritoporecu(0,L,R,Lmar)
print(R)

for elt in R :
    if elt != 0 :
        print(c[elt-1]) """


"""
f=open("graph")
C=f.read()
print(C)
L=C.split("\n")
print(L)
f.close()
for i in range(len(L)) :
    L[i]=L[i].split(",")
print("chiffre")
for i in range(len(L)) :
  if L[i] != [''] :
    for j in range(len(L[i])) :
        print(L[i][j])
        L[i][j]=int(L[i][j])
  else :
      L[i]=[]
print(L)
#"""
import TP1

L=TP1.recugraph("graph")
c=TP1.recucor("cores")

print(L,c)
R=[]
TP1.tritoporecu(0,L,R)
print(R)
R.reverse()
TP1.saveresu(R,c,"resu.txt")

test = TP1.randolist([1,2,3,4,5,6])
print(test)
R=[]

print("aa")
TP1.tritoporecu2(0,L,R)
#print(R)
R.reverse()
TP1.saveresu(R,c,"resu2.txt")

L2=TP1.recugraph("graph2")
c2=TP1.recucor("cores2")
print(L2,c2)


R=[]
TP1.tritoporecu2(0,L2,R)
R.reverse()
print(R)
TP1.saveresu(R,c2,"resu3.txt")