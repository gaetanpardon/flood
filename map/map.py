import math

import objetm2

A =objetm2.Forme(0,0,5)
B=objetm2.Forme(0,0,0)

print(B.contact(A))
print(A.laser(0,4,math.pi/2))

import objetm

A2 =objetm.forme(0,0,5)
B2=objetm.forme(3,4,5)

print(B2.contact(A))
print(math.pi/2)
print(A2.laser(4,0,math.pi/2))

"""
def gardeparti(Bm,Ln) :
    c = objetm2.Carte(500, 7)
    for N in Ln :
        c.car.RAZ()
        parti(Bm,N,c)
    """
class fakeno :
    def __init__(self,d,g):
        self.d=d
        self.g=g
    def work(self,a1,a2,a3,p1,p2,p3,e1,e2):
        return (0,0,self.d,self.g)



def parti(Bm,Rneuro,c): #affichage(liste)
    livetimeusefornotation=0
    life=True
    #c=objetm2.Carte(500,7)#carte
    ax,ay,aa=c.car.getcoor()
    fx,fy=c.arri.getcoor()
    while livetimeusefornotation < Bm and life :
        livetimeusefornotation+=1
        Ld=c.laserma()
        cax,cay,crd,crg=Rneuro.work(Ld[0],Ld[1],Ld[2],ax,ay,aa,fx,fy)
        c.car.moveC(crd,crg)
        ax, ay, aa = c.car.getcoor()
        life=c.life()
        ax=cax
        ay=cay

    return (life)

