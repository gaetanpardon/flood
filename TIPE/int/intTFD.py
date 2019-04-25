from math import sin
from math import cos
from math import atan
from math import sqrt


def intarmo(A,ar):#intégration d'un armonique
    n=len(A)
    pas=2*3.141592654/n
    an=0.0
    bn=0.0
    for i in range(n) :
       an= an + A[i]* cos(ar*(i*pas))
       bn = bn + A[i] * sin(ar*(i * pas))
    if an==0 :
        ph=3.141592654
    else :
        ph = atan (bn/an)
        if an<0 :
            if ph < 0:
                ph = ph + 3.141592654
            else:
                ph = ph - 3.141592654
    cn= sqrt(an**2 + bn**2)
    return (cn,ph)

def FFT (A) :#transphorme de fourirer
    CN=[]
    PH=[]
    for j in range(len (A)) :
        cn , ph = intarmo (A,j)
        if j!=0 :
            cn = 2*cn
        CN=CN + [cn]
        PH = PH + [ph]

    return(CN,PH)

def FSO (A,f,perf) :#trasformer via fonction
    n=len(A)
    pas=perf/n
    CN = []
    Dph = []
    for j in range(len(A)):
        an = 0.0
        bn = 0.0
        for i in range(n):
            an = an + A[i] * f(j * (i * pas))
            bn = bn + A[i] * f(j * (i * pas)+( perf/4) )
        ph = atan(an / bn)
        if an < 0:
            ph = ph - 3.141592654
        cn = sqrt(an ** 2 + bn ** 2)

        CN = CN + [cn]
        Dph = Dph + [ph]

    return (CN,Dph)

def graph(Lv,nom) :#transphorme valeur-->raie
    fichier = open (nom+".pbm" , "w" )

    fichier.write("P1")

    fichier.write("\n")
    long=int(len(Lv)/8)-5

    fichier.write(str(long)+" "+str(long))
    m=2*max(Lv)/((long))

    for h in range(long) :
        fichier.write("\n")
        for l in range(long):
            vt=(Lv[l*4]+Lv[l*4+1]+Lv[l*4+2]+Lv[l*4+3])/m
            if vt>(long-h-4) and vt<(long-h+4)  :
                fichier.write("1")
            else:
                fichier.write("0")
    fichier.close()

def graphpa(Lv,long,nom) :
    fichier = open (nom+".pbm" , "w" )

    fichier.write("P1")

    fichier.write("\n")


    fichier.write(str(long)+" "+str(long))
    m=max(Lv)/((long)*2)

    for h in range(long) :
        fichier.write("\n")
        for l in range(long):
            vt=(Lv[l])/m
            if vt>(long-h)  :
                fichier.write("1")
            else:
                fichier.write("0")
    fichier.close()

def graphpt(Lv,long,nom) :
    fichier = open (nom+".pbm" , "w" )

    fichier.write("P1")

    fichier.write("\n")


    fichier.write(str(long)+" "+str(long))
    m=max(Lv)/((long))

    for h in range(long) :
        fichier.write("\n")
        for l in range(long):
            vt=(Lv[l])/m
            if vt>(long-h-4) and vt<(long-h+4)  :
                fichier.write("1")
            else:
                fichier.write("0")
    fichier.close()


def harliste (L) : #cherche les armonique prinsipaux
    AR=[]
    ar=0
    for i in range(len(L)-3) :
        if L[i+3]>L[i+2] and L[i+3]>L[i+1] and L[i+3]>L[i+0]:
            if (ar+5)<(i+3) :
                AR.append(ar)
                ar=i+3

            if L[i+3]> L[ar] :
                ar=i+3
    return(AR)


def expL(Long):
    Lx=[]
    for i in range(Long):
        
        if i> Long -i :
           Lx.append(0.3678794412**((Long-i)**2) )
        else:
            Lx.append( 0.3678794412 ** ((i) ** 2) )
    return(Lx)

def FFT3d (L) :
    Long=len(L)
    pas = 2 * 3.141592654 / Long
    Lx = expL(Long)
    R = []
    for j in range(Long) :
        Rf = []
        for ar in range(int(Long)) :
            an = 0.0
            bn = 0.0
            for i in range(Long) :
                if (i+j-Long)<0 :
                    ix=i+j
                else :
                    ix=(i+j-Long)

                an += L[i] * cos(ar * (i * pas)) * Lx[ix]
                bn += L[i] * sin(ar * (i * pas)) * Lx[ix]
            cn=sqrt(an**2 + bn**2 )
            if ar != 0 :
                cn= 2 * cn
            if an == 0:
                ph = 3.141592654
            else:
                ph = atan(bn / an)
                if an < 0:
                    if ph< 0 :
                        ph = ph + 3.141592654
                    else :
                        ph = ph - 3.141592654
            Rf.append([cn,ph])
        R.append(Rf)
    return(R)

def chnom(vint,l=4) :
    if vint<(256**l) :
        A=[]
        r=vint
        for i in range(l) :
            a=r//(256**(l-1-i))
            r=r-a*(256**(l-1-i))
            A = [a]+ A
        return A
    else :
        return False

def chduop (ph2,sup) :
    pi = 3.141592654
    if ph2 > 0:
        av = 0
        pa = int(sup * sin(ph2 / (2 / 3)))
    else:
        pa = 0
        av = int(sup * sin(ph2 / (2 / 3)) * (-1))
    return(av,pa)

def chduo(duo,m) :
    pi = 3.141592654
    sup=int((duo[0]/m)*255)
    r,g,b= 255,255,255
    if (pi)>= duo[1] and duo[1] > (pi/3) :
        b=sup
        ph2=duo[1]-2*(pi/3)
        (g,r)=chduop(ph2,sup)
    if (pi/3) >= duo[1] and duo[1] > (-pi / 3):
        g = sup
        ph2 = duo[1]
        (r,b) = chduop(ph2, sup)
    if (-pi / 3) >= duo[1] and duo[1] >= (-pi):
        r = sup
        ph2 = duo[1] + 2 * (pi / 3)
        (b, g) = chduop(ph2, sup)
    if (r,g,b) == (255,255,255) :
        print(duo)


    return([b,g,r,255])


def imagecouleur(M,nom) :
    lar=len(M)
    lon=len(M[0])
    sizepx=lar*lon*4
    hlarpx=chnom(lar)
    hlonpx=chnom(lon)
    size=3*16+6+sizepx
    hsize=chnom(size) #[3*16+6+4,0,0,0]
    hsizepx=chnom(sizepx)#[4,0,0,0]
    entetef=[[4*16+2,4*16+13],hsize,[0,0,0,0],[3*16+6,0,0,0]]
    entetebit = [[2*16+8,0,0,0],hlarpx,hlonpx,[1,0],[32,0],[0,0,0,0],hsizepx,[1,1,0,0],[1,1,0,0],[0,0,0,0],[0,0,0,0]]
    entete = entetef + entetebit
    fichier = open(nom + ".BMP", "wb")
    for e in entete :
        fichier.write(bytearray(e))

    m =0
    for im in range(lar):
        for jm in range(lon):
            v=M[im][jm][0]
            if v>m :
                m=v
    for il in range(lar) :
        for jl in range(lon) :
            hpx=chduo(M[il][jl],m)
            fichier.write(bytearray(hpx))
    fichier.close()
    return(True)

def FFT3dr (L,armin=0,armax=0,sf=0) :
    Long=len(L)
    pas = 2 * 3.141592654 / Long
    if armax==0:
        armax=Long
    Lx = expL(Long)
    R = []
    j=0
    Mtour=0 #debug
    flag=True
    while j < Long and flag:
        Rf = []
        ar=armin
        while ar < armax :
            an = 0.0
            bn = 0.0
            for i in range(Long) :
                if (i+j-Long)<0 :
                    ix=i+j
                else :
                    ix=(i+j-Long)

                an += L[i] * cos(ar * (i * pas)) * Lx[ix]
                bn += L[i] * sin(ar * (i * pas)) * Lx[ix]
            cn=sqrt(an**2 + bn**2 )
            if ar != 0 :
                cn= 2 * cn
            if an == 0:
                ph = 3.141592654
            else:
                ph = atan(bn / an)
                if an < 0:
                    if ph< 0 :
                        ph = ph + 3.141592654
                    else :
                        ph = ph - 3.141592654
            Rf.append([cn,ph])
            ar+=1
        j+= (sf+1)
        R.append(Rf)
        Mtour+=1
        if Mtour>10 :
            Mtour=0
            conti=input("stop:")
            if conti == "o":
                flag=False


    return(R)

def FFT3dn (L,armin=0,armax=0,sf=0) :
    Long=len(L)
    pas = 2 * 3.141592654 / Long
    if armax==0:
        armax=Long
    Lx = expL(Long)
    R = []
    j=0
    Mtour=0 #debug
    flag=True
    while j < Long and flag:
        Rf = []
        ar=armin
        while ar < armax :
            an = 0.0
            bn = 0.0
            for i in range(Long) :
                if (i+j-Long)<0 :
                    ix=i+j
                else :
                    ix=(i+j-Long)

                an += L[i] * cos(ar * (i * pas)) * Lx[ix]
                bn += L[i] * sin(ar * (i * pas)) * Lx[ix]
            cn=sqrt(an**2 + bn**2 )
            if ar != 0 :
                cn= 2 * cn
            if an == 0:
                ph = 3.141592654
            else:
                ph = atan(bn / an)
                if an < 0:
                    if ph< 0 :
                        ph = ph + 3.141592654
                    else :
                        ph = ph - 3.141592654
            Rf.append([cn,ph])
            ar+=1
        j+= (sf+1)
        R.append(Rf)
        Mtour+=1
        if Mtour>10 :
            Mtour=0
            conti=input("stop:")
            if conti == "o":
                flag=False


    return(R)

def vals(b):
    v=int(b)
    if v>127 :
        v=254-v
    return(v)