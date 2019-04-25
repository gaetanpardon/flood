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
    for il in range(lar) :
        for jl in range(lon) :
            hpx=M[il][jl] #[r,g,b 255]
            fichier.write(bytearray(hpx))
    fichier.close()
    return(True)

def nuancier ():
    M=[]
    for i in range(512) :
        M.append([])
        for j in range (512) :
            ia=i//64
            ja=j//64
            r=(i-ia*64)*4+3
            g=(ia*8+ja)*4+3
            b=(j-ja*64)*4+3
            if r>255 or g>255 or b>255 :
                print(i,j,r,g,b,ia,ja)

            M[i].append([r,g,b,255])
    return (M)
