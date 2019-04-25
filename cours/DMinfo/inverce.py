f=open("./MCC.CSV", "r")
flag=0
L=""
T=[]
t=0
for l in f:
    if flag==1 :
        L=l+L
        T=T+[t]
        t=t+0.1
    else:
        v=l
    flag=1
L=v+L

f.close()

c=open("./MCCF.CSV", "w")
c.write(L)
c.close