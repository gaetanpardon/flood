
import random
import time
liste=[]
import fonct as f

for i in range(10) :
    a=random.randint(0,1000)
    liste+= [a]

def maxi(L):
    m=L[0]
    for v in L :
        if m<v :
            m=v

    return(m)

def moy(L):
    m=L[0]
    for v in L :

        m+=v

    return(m/len(L))
def var (L) :
    mo= moy(L)
    va=0
    for v in L :
        va+=(v-mo)**2
    return (va/len(L))

t=time.time()
print(maxi(liste),moy(liste),var(liste))
print(t,time.time()-t)

def tri(L) :
    Lt=[]
    for i in range(len(L)):
        if Lt==[]:
            Lt=[L[i]]
        else :
            Lt=Lt+[L[i]]
            for j in range(i) :
                if Lt[j + 1] >= L[i] and L[j] < L[i]:
                    Lt.insert(j, L[i])
                if Lt[i - 1] < L[i]:
                    Lt.append(L[i])
    return(Lt)

print(liste)
input()
t=time.time()
R=f.tri(liste)
print(R)
print(time.time()-t)

input()
t=time.time()
R=f.tribulle(liste)
print(R)
print(time.time()-t)

print(f.heron(5,0.001))