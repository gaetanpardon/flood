import random
R=[]
L=[]
i = 0
print("ok")
for i in range(100) :
    L.append(i)
i=0
j=0
print("ok")
for i in range(100) :
    j=random.randint(0 , 100-(i+1))
    R.append(L[j])
    L=L[:j]+L[j+1:]
print("ok")
fichier = open ("melange.txt" , "w" )
for i in range(len(R)) :
    fichier.write(str(i)+") "+str(R[i])+"\n")
fichier.close()
print(R)