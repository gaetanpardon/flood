# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 15:22:11 2015

@author: pardon
"""
def fct(x,y):
    if (y-35)**2+(x-35)**2<400 :#or 70-x-y==0:
        return(0)
    else:
        return(1)
        
def ligne(numero, image):
    largeur , hauteur = image.size
    image_mod=Image.new('RGB',(largeur,hauteur))
    pixels = image.load()
    pixels2 = image_mod.load()
    for l in range (0,largeur) :
        if l != numero :
            for h in range(0, hauteur) :
                pixels2[l,h] = pixels[l,h]
        else:
             for h in range(0, hauteur) :
                 pixels2[l,h] = (0,0,0)
    return(image_mod)

largeur=70
hauteur=70

fichier = open ("image2.pbm" , "w" )

fichier.write("P1")

fichier.write("\n")

fichier.write(str(largeur)+" "+str(hauteur))

for h in range(hauteur) :
    fichier.write("\n")
    for l in range(largeur):
        if fct(h,l)==0:
            fichier.write("0")
        else:
            fichier.write("1")
fichier.close()


def miroir(numero, image):
    largeur , hauteur = image.size
    image_mod=Image.new('RGB',(largeur,hauteur))
    pixels = image.load()
    pixels2 = image_mod.load()
    for h in range (0,hauteur) :
        if h != numero :
            for l in range(0, largeur) :
                pixels2[largeur-l-1,h] = pixels[l,h]
        else:
             for l in range(0, largeur) :
                 pixels2[l,h] = (255,255,255)
    return(image_mod)
    
    
def NouB (image):
    largeur , hauteur = image.size
    image_mod=Image.new('RGB',(largeur,hauteur))
    pixels = image.load()
    pixels2 = image_mod.load()
    for h in range (0,hauteur) :
            for l in range(0, largeur) :
                R, G , B = pixels[l,h]
                N=0.299*R + 0.587*G + 0.114*B
                N= int(N)
                pixels2[l,h] = (N,N,N)
    return(image_mod)
    
def Nega (image):
    largeur , hauteur = image.size
    image_mod=Image.new('RGB',(largeur,hauteur))
    pixels = image.load()
    pixels2 = image_mod.load()
    for h in range (0,hauteur) :
            for l in range(0, largeur) :
                R, G , B = pixels[l,h]
                R ,G , B = 255-R , 255-G , 255-B 
                pixels2[l,h] = (R,G,B)
    return(image_mod)
    
def NBhis (image):
    largeur , hauteur = image.size

    pixels = image.load()
    liste=[]
    for i in range (0,256):
        liste=liste+[0]
    for h in range (0,hauteur) :
            for l in range(0, largeur) :
                R, G , B = pixels[l,h]
                N=0.299*R + 0.587*G + 0.114*B
                N= int(N)
                liste[N]=liste[N]+1 
    return(liste) 
    
def NouB2 (image):
    largeur , hauteur = image.size
    image_mod=Image.new('RGB',(largeur,hauteur))
    pixels = image.load()
    pixels2 = image_mod.load()
    for h in range (0,hauteur) :
            for l in range(0, largeur) :
                R, G , B = pixels[l,h]
                N=0.299*R + 0.587*G + 0.114*B
                if N<30:
                    M=0
                elif N<181:
                    M=N-30
                    M=M/151*255
                    M= int(M)
                else:
                    M=255
                #print(M)

                pixels2[l,h] = (M,M,M)
    return(image_mod)
from PIL import Image


def flitrepb (image):
    largeur , hauteur = image.size
    image_mod=Image.new('RGB',(largeur,hauteur))
    pixels = image.load()
    pixels2 = image_mod.load()
    for h in range (0,hauteur-2) :
            for l in range(0, largeur-2) :
                if l==0 or l==largeur or h==0 or h==hauteur :
                    R, G , B = pixels[l,h]
                    N=R              
                else:
                    N=0
                    for vl in range(3) :
                        for vh in range(3) :
                            R, G , B = pixels[l-1+vl,h-1+vh]
                            if vl==1 and vh==1 :
                                N=N+4*R
                            else:
                                N=N+R
                    N=N/12
                if N<0:
                    M=0
                elif N<255:
                    M=N#-20
                    #M=M/181*255
                    M= int(M)
                else:
                    M=255
                #print(M)
                pixels2[l,h] = (M,M,M)
    return(image_mod)

def flitreph (image):
    largeur , hauteur = image.size
    image_mod=Image.new('RGB',(largeur,hauteur))
    pixels = image.load()
    pixels2 = image_mod.load()
    for h in range (0,hauteur-2) :
            for l in range(0, largeur-2) :
                if l==0 or l==largeur or h==0 or h==hauteur :
                    R, G , B = pixels[l,h]
                    N=R              
                else:
                    N=0
                    for vl in range(3) :
                        for vh in range(3) :
                            R, G , B = pixels[l-1+vl,h-1+vh]
                            if vl==1 and vh==1 :
                                N=N+5*R
                            elif vl==1 or vh==1:
                                N=N-R
                N=N
                if N<0:
                    M=0
                elif N<255:
                    M=N#-20
                    #M=M/181*255
                    M= int(M)
                else:
                    M=255
                #if M!=0 :
                    #print(M)

                pixels2[l,h] = (M,M,M)
    return(image_mod)
    
def flitre33 (image,MATR):
    largeur , hauteur = image.size
    image_mod=Image.new('RGB',(largeur,hauteur))
    pixels = image.load()
    pixels2 = image_mod.load()
    TVM=0
    for vhi in range(3) :
        
        for vli in range(3) :
            TVM=TVM+ MATR[vhi][vli]        
    for h in range (0,hauteur) :
            for l in range(0, largeur) :
                if l<(1) or l>(largeur-2) or h<(1) or h>(hauteur-2 ) :
                    R, G , B = pixels[l,h]
                    N=R              
                else:
                    N=0
                    for vh in range(len(MATR)) :
                        
                        for vl in range(len(MATR[vh])) :
              
                            R, G , B = pixels[l+vl-1,h+vh-1]
                            N=N+R*MATR[vh][vl]
                    if TVN != 0 :
			N=N/TVM
                if N<0:
                    M=0
                elif N<255:
                    M=N#-20
                    #M=M/181*255
                    M= int(M)
                else:
                    M=255
                #if M!=0 :  #debug
                 #   print(M)  #debug

                pixels2[l,h] = (M,M,M)
    return(image_mod)

    
def flitre (image,MATR):
    largeur , hauteur = image.size
    image_mod=Image.new('RGB',(largeur,hauteur))
    pixels = image.load()
    pixels2 = image_mod.load()
    DHM=len(MATR)
    DLM=0
    TVM=0
    for vhi in range(len(MATR)) :
        
        DLMT=len(MATR[vhi])
        if DLMT>DLM :
            DLM=DLMT
        for vli in range(len(MATR[vhi])) :
            #print (MATR[vhi]) #debug
            #print (MATR[vhi][vli]) #debug
            TVM=TVM+ MATR[vhi][vli]
    print("l=",DLM,"l/2=",DLM//2)
    print("h=",DHM,"h/2=",DHM//2)        
    for h in range (0,hauteur) :
            for l in range(0, largeur) :
                if l<(DLM//2) or l>(largeur-DLM//2 -1) or h<(DHM//2) or h>(hauteur-DHM//2 -1) :
                    R, G , B = pixels[l,h]
                    N=R              
                else:
                    N=0
                    for vh in range(len(MATR)) :
                        
                        for vl in range(len(MATR[vh])) :
                            #if vl-DLM//2>-3 or vh-DHM//2>-3 : #debug
                                #print(l,vl,DLM//2,h,vh,DHM//2) #debug
                            R, G , B = pixels[l+vl-DLM//2,h+vh-DHM//2]
                            N=N+R*MATR[vh][vl]
                    if TVN != 0 :
			N=N/TVM
                if N<0:
                    M=0
                elif N<255:
                    M=N#-20
                    #M=M/181*255
                    M= int(M)
                else:
                    M=255
                #if M!=0 :  #debug
                 #   print(M)  #debug

                pixels2[l,h] = (M,M,M)
    return(image_mod)
im = Image.open("TP Image\londres.jpg")

im.show()

largeur , hauteur = im.size
print (largeur , hauteur )

image_mod=ligne(10,im)
image_mod.show()

image_mod4=miroir(im)
image_mod4.show()

image_mod2=NouB(im)
image_mod2.show()

image_mod3=Nega(im)
image_mod3.show()
    
imc = Image.open("TP Image\chat.jpg")

imcnb = NouB(imc)
imcnb.show()

import matplotlib.pyplot as plt

table = NBhis(imc)
plt.figure()
plt.plot(range(len(table)),table,'K')

plt.grid(True)
plt.show()

imcnb2 = NouB2(imc)
imcnb2.show()

imflipb = flitrepb(imcnb)
imflipb.show()

imfliph = flitreph(imcnb)
imfliph.show()

matrice= [[1,1,1]]+[[1,4,1]]+[[1,1,1,]]
imflipb2 = flitre33(imcnb,matrice)
imfli.show()

matrice= [[0,-1,0]]+[[-1,5,-1]]+[[0,-1,0,]]
imfli = flitre33(imcnb,matrice)
imfliph2.show()

#bas 3*5
matrice = [[1,1,1]]+[[1,1,1]]+[[1,4,1]]+[[1,1,1]]+[[1,1,1]]
imfli = flitre(imcnb,matrice)
imfli.show()
#bas renforcé 5*5
matrice = [[1,1,1,1,1]]+[[1,2,2,2,1]]+[[1,2,4,2,1]]+[[1,2,2,2,1]]+[[1,1,1,1,1]]
imfli2 = flitre(imcnb,matrice)
imfli2.show()
#hasard
matrice=[[11,12,37,15,745,147]]+[[144,15,15,87,54,87]]+[[15,48,36,14,84,23]]
imfli3 = flitre(imcnb,matrice)
imfli3.show()
#haut renforcé 5*5
matrice=[[-1,-1,-1,-1,-1]]+[[-1,-2,-2,-2,-1]]+[[0,-2,31,-2,0]]+[[-1,-2,-2,-2,-1]]+[[-1,-1,-1,-1,-1]]

imfli4 = flitre(imcnb,matrice)
imfli4.show()

matrice= [[-1,-1,-1,-1,-1]]+[[-1,4,4,4,-1]]+[[-1,4,0,4,-1]]+[[-1,4,4,4,-1]]+[[-1,-1,-1,-1,-1]]
imfli5 = flitre(imcnb,matrice)
imfli5.show()