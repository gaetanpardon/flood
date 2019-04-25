"""
perm
addu
fond
char
toit
plaf
cloi
plom
elec
plat


constrution = dict()

constrution["perm"]=set()
constrution["addu"]=set()
constrution["fond"]=set()
constrution["char"]=set()
constrution["toit"]=set()
constrution["plaf"]=set()
constrution["cloi"]=set()
constrution["plom"]=set()
constrution["elec"]=set()
constrution["plat"]=set()


constrution["perm"].add("contenu",[6])
constrution["addu"]=set("contenu",[3])
constrution["fond"]=set("contenu",[5,"perm","addu"])
constrution["char"]=set("contenu",[2,"fond"])
constrution["toit"]=set("contenu",[2,"char"])
constrution["plaf"]=set("contenu",[2,"char"])
constrution["cloi"]=set("contenu",[3,"plaf"])
constrution["plom"]=set("contenu",[3,"plaf","cloi"])
constrution["elec"]=set("contenu",[2,"plaf","cloi"])
constrution["plat"]=set("contenu",[3,"toit","plaf","cloi","plom","elec"])

#""
Lgraph=[[],[[0,0]],[[0,0]],[[6,1],[3,2]],[[5,3]],[[2,4]],[[2,4]],[[2,6]],[[2,6],[3,7]],[[2,6],[3,7]],[[2,5],[2,6],[3,7],[3,8],[2,9]],[[3,10]]]
#""
def graphLvM(L):
    M=[]
    for i in range(len(L)) :
        M.append([])
        for j in range(len(L)):
            M[i].append("v")
    for i in range(len(L)):
        for elt in L[i] :
            M[i][elt[1]]=elt[0]
    return(M)
#Mgraph=graphLvM(Lgraph)
#print(Mgraph)


def pluslongM(M) :
    R=M[:]
    i=0
    j=0
    for m in range(len(R)) :
     for i in range(len(R)):
        for j in range(len(R)):
            if R[i][j]!='v' :
                for k in range(len(R)) :
                    if R[j][k]!='v' :
                       if R[i][k]=='v' :
                           R[i][k]=R[i][j]+R[j][k]
                       else :
                            R[i][k]=max(R[i][k],R[i][j]+R[j][k])

    return(R)

#tM=pluslongM(Mgraph)
#print(tM)

def checrit (Ml) :
    L=[]
    for i in range(len(Ml)) :
        if Ml[-1][i]!='v' and Ml[i][0]!='v' :
            if Ml[-1][0]==Ml[-1][i]+Ml[i][0] :
                L.append(i)
    return(L)
#criM=checrit(tM)
#print(criM)

def plutard(Ml) :
    L=[]
    for i in range(len(Ml)) :
        if Ml[-1][i]!='v' and Ml[i][0]!='v' :
            L.append(Ml[-1][0]-Ml[-1][i])
    return(L)

""
var=plutard(tM)
print(var)
Ltemp=[]
for elt in tM[1:-1] :
    Ltemp.append(elt[0])

print(Ltemp)
#"""

CLEOPATRE = "Cleopatre"
IPHIGENIE = "Iphigenie"
JULIETTE = "Juliette"
FANNY = "Fanny"
CHIMENE = "Chimene"

ACHILLE = "Achille"
CESAR = "Cesar"
RODRIGUE = "Rodrigue"
ROMEO = "Romeo"
MARIUS = "Marius"

LES_COUPLES = [("start",CLEOPATRE),("start",IPHIGENIE),("start",JULIETTE),("start",FANNY),("start",CHIMENE),(CLEOPATRE, ACHILLE), (CLEOPATRE, CESAR), (CLEOPATRE, ROMEO),
               (IPHIGENIE, ACHILLE), (JULIETTE, CESAR), (JULIETTE, RODRIGUE), (JULIETTE, ROMEO),
               (FANNY, CESAR), (FANNY, MARIUS), (CHIMENE, RODRIGUE), (CHIMENE, ROMEO),("end",ACHILLE),("end",CESAR),("end",RODRIGUE),("end",ROMEO),("end",MARIUS)]
Cl=["start",CLEOPATRE,IPHIGENIE,JULIETTE,FANNY,CHIMENE,ACHILLE,CESAR,RODRIGUE,ROMEO,MARIUS,"end"]

Gmar=[]
for i in range(len(Cl)) :
    Gmar.append([])
    for elt in LES_COUPLES :
        #print(elt)
        if elt[0]==Cl[i] :
            j=0
        """
            flag=True
            while j<len(Cl) and flag:
                if Cl[j]==elt[1] :
                    Gmar[i].append(j)
                    flag=False
                j+=1
        """
        if elt[1]==Cl[i] :
            j=0
            flag=True
            while j<len(Cl) and flag:
                if Cl[j]==elt[0] :
                    Gmar[i].append(j)
                    flag = False
                j+=1
        #"""
print(Gmar)

def LvM(L) :
    M=[]
    for i in range(len(L)):
        M.append([])
        for j in range(len(L)):
            M[i].append(0)
    for i in range(len(L)):
        for elt in L[i]:
            M[i][elt]=1
    return(M)
Mmar=LvM(Gmar)
print(Mmar)

def chemin(M,d,s) :
    ch=[d]
    b=[[],[d]]
    flag=True
    while flag:
        m=0
        mj=-1
        if len(ch)<len(M) :
            for j in range(len(M[ch[-1]])) :
                if M[ch[-1]][j]>=m :
                    if not j in b[-1] :
                        m=M[ch[-1]][j]
                        mj=j
        if mj==-1 or m==0 :
            b=b[:-1]
            b[-1].append(ch[-1])
            ch=ch[:-1]
        else :
            b.append([d])
            ch.append(mj)
        if ch == [] :
            flag=False
        else:
            if ch[-1]==s :
                flag=False
    return(ch)

def copy(Mo) :
    M=[]
    for i in range(len(Mo)) :
        M.append([])
        for elt in Mo[i] :
            M[-1].append(elt)
    return(M)
def flotmax(Mo) :
    M = Mo[:][:]
    ch=chemin(M,0,11)
    m=0
    while ch!=[] :
        #print(type(M))
        #print(ch)
        m=M[ch[0]][ch[1]]

        #m=I[int(ch[1])]

        for i in range(len(ch)-1) :
            if M[ch[i]][ch[i+1]]<m :
                m=M[ch[i]][ch[i+1]]
        for i in range(len(ch)-1):
            M[ch[i]][ch[i + 1]]=-m
            M[ch[i+1]][ch[i]]=+m
        if m==0 :
            print("inf")
        chemin(M,0,11)
    return(M)

def extra(M,Mo) :
    Mf=[]
    for i in range(len(M)) :
        Mf.append([])
        for j in range(len(M)) :
            Mf[-1].append(Mo[i][j]-M[i][j])
    return(Mf)
I=flotmax(Mmar)
R=extra(I,Mmar)

print("\n\n\n",R)