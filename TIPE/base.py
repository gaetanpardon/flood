from math import sin
from math import cos
from math import atan
from math import log
#import matplotlib.pyplot as plt
from int import intTFD as itg
#from PIL import Ima
Te = 4

def read (nom):
    f=open("./"+nom, "r")
    flag=0
    L=[]
    T=[]
    t=0
    for l in f:
        if flag==1 :
            L = L+[float(l.strip("\r"))]
            T = T+[t]
            t = t+Te
        flag=1
    f.close()
    return(L , T)

L, T = read("MCC.CSV")
print(L)
V ,VP= itg.FFT(L)


#print(V)
print(len(L))
t=input("graph:")
if t=="o" :
    itg.graph(V,"image/imaVp4")
    itg.graph(L,"image/imaLp4")
t=input("graph:")
if t=="o" :
    itg.graphpa(V,200,"image/imaV200pt")
    itg.graphpt(L,700,"image/imaL300pt")

AR=itg.harliste(V)
print(len(AR))
print(AR)
t=input("massif:")
if t=="o" :
    R3D=itg.FFT3dr(L,1,720,69)
    itg.imagecouleur(R3D,"imageglobFl")
"""
Vlog = []
J=[]
i=0
j=1
while i+j<len(V):
    k=0
    Vtemps=0
    while k<j :
        Vtemps=Vtemps+V[i]
        i+=1
        k+=1

    k=0
    Vlog=Vlog+[int(Vtemps/j)]
    J=J+[j]
    j=j*2
    print(j)

print(Vlog)
print(J)
#"""
"""
plt.figure()
plt.plot(range(len(V)),V,'K')

plt.grid(True)
plt.show()


plt.figure()
plt.plot(T,L,'K')

plt.grid(True)
plt.show()

#"""

Ltest=[]
for ig in range(1000) :
    Ltest= Ltest + [sin(3.141592654*ig/100)]



Rf , Rfph = itg.FFT(Ltest)
To , Toph = itg.FSO(Ltest,cos,3.141592654*2)

print(Rf,'/n/n/n/n/n',To)

print('dif:')
nd=0
e=0.0001
for i in range(len(Rf)) :
    if( Rf[i]*(1+e)< To[i]) or (Rf[i]*(1-e)> To[i]) :
        print (Rf[i],To[i])
        nd+=1
print(nd)

#"""