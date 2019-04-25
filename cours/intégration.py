# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:39:54 2016

@author: pardon
"""
import matplotlib.pyplot as plt
def integre(f,a,b,n,p):
    pa=(a+b)/n
    Tot=0
    for i in range(n):
        fu= f(a + pa * ( i + p) )
        Tot = Tot + ( fu * pa )
    return(Tot)
    
def f(x) :
    return(1/(1+x**2))
    
test=integre (f , 0, 1 , 2000 ,0)
print (test)    

def rect_g(f,a,b,n):
    T=integre(f,a,b,n,0)
    return(T)
def rect_d(f,a,b,n):
    T=integre(f,a,b,n,1)
    return(T)
def rect_m(f,a,b,n):
    T=integre(f,a,b,n,0.5)
    return(T)
def trap(f,a,b,n):
    T=(integre(f,a,b,n,0)+integre(f,a,b,n,1))/2
    return(T)
    

def trapd(f,a,b,n):
    pa=(a+b)/n
    Tot=0
    fd=( f(a) )
    for i in range(n):
        #print("i=",i)
        fg = fd
        fd=( f(a + pa * ( i + 1 )) )
        #print (fd)
        Tot = Tot +( (fg +fd) /2 )*pa
    return(Tot)

rg=rect_g(f , 0, 1 , 200)
rd=rect_d(f , 0, 1 , 200)
rm=rect_m(f , 0, 1 , 200)
print("\r \r \r \r \r" )
trd=trapd (f , 0, 1 , 200)
tr=trap (f , 0, 1 , 200)
print(rg,"\r",rd,"\r",rm,"\r",tr,"\r",trd)

print("\r \r \r \r \r" )

print (rect_g(f , 0, 1 , 10) , rect_g(f , 0, 1 , 100) , rect_g(f , 0, 1 , 10000))
print (rect_d(f , 0, 1 , 10) , rect_d(f , 0, 1 , 100) , rect_d(f , 0, 1 , 10000))
print (rect_m(f , 0, 1 , 10) , rect_m(f , 0, 1 , 100) , rect_m(f , 0, 1 , 10000))
print (trap(f , 0, 1 , 10) , trap(f , 0, 1 , 100) , trap(f , 0, 1 , 10000))

print ("\r \r \r \r \r \r \r \r \r")
print("à partir de la ligne 2 on des valeur en v tout les 0.1 ms ")

def read (nom):
    f=open("./"+nom, "r")
    flag=0
    L=[]
    T=[]
    t=0
    for l in f:
        if flag==1 :
            L=L+[float(l.strip("\r"))]
            T=T+[t]
            t=t+0.1
        flag=1
    f.close()
    return(L , T)
    
L, T = read("MCC.CSV")
plt.figure()
plt.plot(T,L,'K')

plt.grid(True)
plt.show()

def moyenne(N,liste):
    assert len(liste)>N
    T=0
    for i in range(N):
        T=T+liste[i]
    return(T/N)
def moy(liste):
    T=0
    for i in range(len(liste)):
        T=T+liste[i]
    return(T/len(liste))
    
    
m=moy(L)    
print("la valeur moyenne est", m,"V")
M=[]
for i in range(len(L)):
    M=M+[m]
plt.plot(T,L,'K')
plt.plot(T,M,'K')
plt.show()
def periode (liste,m,e): #m étant une marge de valeur atteinte autour de la valeur de moy :
    assert e<m and 0<m and 0<e    
    vmoy = moy(liste)
    i=0
    nv=0
    vl=[]
    for i in range(len(liste)):

        return("256")
            
p=periode(L,1,0.7)
print ("periode en echantillon:", p)
print ("vérification de la valeur de la periode sur 3 exemple: \r",L[1],"\r",L[1+int(p)],"\r",L[1+2*int(p)],"\r coucou")
print ("la periode est de :", p/10 ,"ms")

def moyenne_glissante(liste,N):
    u=int(N)
    vmoy = moy(liste)
    if u%2==1 :
        u=u+1
    #print(u)#debug 
    MG=[]
    for i in range(len(liste)):
        if u/2<i and i<len(liste)-u/2 :
            T=0.0
            # print("ok") #debug
            for j in range(u+1):
                T=T+liste[i+j-int(u/2)]
            MG=MG+[2*vmoy-T/u+1]
        else:
            MG=MG+[2*vmoy-liste[i]]
    return(MG)

mg=moyenne_glissante(L,p)

plt.plot(T,L,'K')
plt.plot(T,M,'K')
plt.plot(T,mg,'K')
plt.show()

print("le chariot de golf a accéléré ")