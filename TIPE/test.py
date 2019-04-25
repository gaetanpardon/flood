from int import intTFD as itg
"""

fichier = open ("test" +".pbm" , "w" )

fichier.write("P3")

fichier.write("\n")
long =5

fichier.write(str(long)+" "+str(long))


for h in range(long) :
    fichier.write("\n")
    for l in range(long):

        if True  :
            fichier.write("2")
        else:
            fichier.write("0")
fichier.close()
#"""
"""
def ipar(fa,fb) :
    L=[]
    flag=True
    i=0
    s=0
    d=0
    if len(fa)>len(fb) :
        li=len(fb)
    else :
        li=len(fa)
    while flag :
        if fa[i]==fb[i] :
            s=s+1
        else :
            if s!=0 :
                L.append("S"+str(s))
                s=0
            L.append(fb[i])
        if (i+2)>li :
            flag=False
        else :
            i+=1
    return(L)




fichier = open ("image/"+"RGB.tif" , "rb" )


for l in fichier :
    print(l)
    for v in l :
        print(v)


fichier.close()

f=open ("image/"+"5x30.tif" , "rb" )
for l in f :
    print(l)
f.close()

f=open ("image/"+"5x30n.tif" , "rb" )
for l in f :
    print(l)
f.close()

f=open ("image/"+"10x3.tif" , "rb" )
for l in f :
    print(l)
f.close()

f=open ("image/"+"10x3n.tif" , "rb" )
a=f.read()
print("\r","\r","\r","\r")
print(a[2])

f.close()


"""#"""
"""#"""
"""#"""
"""#"""
"""
f1=open ("image/"+"5x30n.tif" , "rb" )

f2a=open ("image/"+"10x3.tif" , "rb" )

f2b=open ("image/"+"10x3n.tif" , "rb" )

fa=f1.read()
fb=f2a.read()
fc=f2b.read()

f1.close()
f2a.close()
f2b.close()

L1=ipar(fa,fb)
L2=ipar(fa,fc)
print(L1)
print(L2)

L3 = []
for e in fa :
    L3 = [e] + L3
L1a = []
for e in L1 :
    L1a = [e] + L1a
L2a = []
for e in L2 :
    L2a = [e] + L2a

L4=ipar(L3,L1a)
L5=ipar(L3,L2a)
print(L4)
print(L5)
"""
#4965

print(18//16)

l= itg.chnom(35456565)
print(l)

l=itg.chduo([5,2],5)
print(l)

Lx=itg.expL(20)
print(Lx)

L=[0,1,2,1,0,1,2,1,0]
print("\r", "\r", "calcul:")
R=itg.FFT3d(L)
print(R)

itg.imagecouleur([[[5,2]]],"image")
itg.imagecouleur(R,"image2")
#"""