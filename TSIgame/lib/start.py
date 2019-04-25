import pygame
from pygame.locals import *
from lib import game as g

pygame.init()
pygame.font.init()


def menu (fenetre , background ) :
    fenetre.blit(background, (0, 0))
    font = pygame.font.Font(None, 45)
    p_bar = pygame.Surface((750, 50))  # crée un rectagle
    p_bar = p_bar.convert()  # convertie en image
    p_bar.fill((255, 255, 255))  # change sa couleur
    p_text_nouv = font.render("nouvelle", 1, (125, 15, 15))
    p_text_char = font.render("charger", 1, (125, 15, 15))
    p_text_opti = font.render("option", 1, (125, 15, 15))
    p_text_crédi = font.render("crédit", 1, (125, 15, 15))
    p_text_quit = font.render("quitter", 1, (125, 15, 15))
    flag=1
    while flag:

        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus

            if event.type == pygame.locals.QUIT:  # Si un de ces événements est de type QUIT

                flag = 0  # On arrête la boucle
            if event.type == pygame.locals.KEYDOWN:  # KEYUP
                print(event.key)
                #print(pygame.locals.K_m)
                if event.key == pygame.locals.K_TAB:
                    flag = 0
            if event.type == pygame.locals.MOUSEBUTTONDOWN :
                print("clic")
                print (event.pos[0])
                print(event.pos[1])
                if 50 < event.pos[0] and event.pos[0] < 800 and 50 < event.pos[1] and event.pos[1] < 100:
                    print("game")
                    g.game(fenetre, background)
                if  50<event.pos[0]  and event.pos[0]<800 and 150<event.pos[1] and event.pos[1]<200 :
                    print("chargé")
                    charger(fenetre , background)
                if 50 < event.pos[0] and event.pos[0] < 800 and 250 < event.pos[1] and event.pos[1] < 300:
                    print("option")
                    optionL()


        fenetre.blit(background, (0, 0))

        fenetre.blit(p_bar, (50, 50))
        fenetre.blit(p_text_nouv, (50, 50))
        fenetre.blit(p_bar, (50, 150))
        fenetre.blit(p_text_char, (50, 150))
        fenetre.blit(p_bar, (50, 250))
        fenetre.blit(p_text_opti, (50, 250))
        fenetre.blit(p_bar, (50, 350))
        fenetre.blit(p_text_crédi, (50, 350))
        fenetre.blit(p_bar, (50, 450))
        fenetre.blit(p_text_quit, (50, 450))


        pygame.display.flip()
        pygame.time.wait(30)
    print("menu ok")
    return(None)


def charger(fenetre , background) :
    d_sl=open("./save/savelist.txt","r")
    p_save_sl =[]
    p_save_slp = []
    p_save_name =[]
    p_case = pygame.Surface((350, 450))  # crée un rectagle
    p_case = p_case.convert()  # convertie en image
    p_case.fill((255, 255, 255))  # change sa couleur
    p_persoD=pygame.image.load('./image/Dperso.png').convert_alpha()
    for elt in d_sl :
        #print ([elt.strip("\n")])
        #print ([elt])
        fenetre.blit(background, (0, 0))
        font = pygame.font.Font(None, 45)

        p_save_tuple = (elt.strip("\n")).split(";")

        print("tuple :",p_save_tuple)
        p_text_save = font.render(( p_save_tuple[0] ), 1, (125, 15, 15))#texte visible
        p_save_sl = p_save_sl +[ p_text_save ]
        p_save_slp = p_save_slp + [p_save_tuple[1]]
        p_save_name = p_save_name + [p_save_tuple[0]]

    print(p_save_sl)
    print(p_save_slp)
    d_sl.close()
    p_save_perso_sl=[]
    for i in range (len(p_save_slp)) :
        try :
             p_nomperso = "./image/perso"+p_save_slp[i] +".png"
             p_perso=pygame.image.load(p_nomperso).convert_alpha()
        except :
            p_perso=p_persoD
            print("l'image du le perso " + p_save_slp[i] + " est corompu")
        p_save_perso_sl = p_save_perso_sl + [p_perso]



    flag = 1
    p_sc =0
    while flag :
        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus

            if event.type == pygame.locals.QUIT:  # Si un de ces événements est de type QUIT

                flag = 0  # On arrête la boucle
            if event.type == pygame.locals.KEYDOWN:  # KEYUP
                #print(event.key)
                # print(pygame.locals.K_m)
                if event.key == 114:
                    flag = 0
                if event.key == 275 and p_sc+2< len(p_save_sl) :
                    p_sc += 1
                if event.key == 276 and p_sc > 0:
                    p_sc -= 1


            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                print("clic")
                print(event.pos[0])
                print(event.pos[1])
                if 50 < event.pos[0] and event.pos[0] < 400 and 50 < event.pos[1] and event.pos[1] < 500:
                    print("chargé")
                    load(fenetre, background)
                if 450 < event.pos[0] and event.pos[0] < 800 and 50 < event.pos[1] and event.pos[1] < 500:
                    print("chargé2")
                    load(fenetre, background)

        fenetre.blit(background, (0, 0))
        fenetre.blit(p_case, (50, 50))
        fenetre.blit(p_save_perso_sl[p_sc], (50, 50))
        fenetre.blit(p_save_sl[p_sc], (50, 500))
        fenetre.blit(p_case, (450, 50))
        fenetre.blit(p_save_perso_sl[p_sc+1], (450, 50))
        fenetre.blit(p_save_sl[p_sc+1], (450, 500))

        pygame.display.flip()
        pygame.time.wait(30)
    return (None)

def optionL () :
    try :
        d_opg=open("./option/optionG.txt","r")
        lp_optg = []
        for elt in d_opg :
            lp_optg= lp_optg+[int(elt.strip("\n"))]
        print(lp_optg)
    except :
        print("optiongE")
    try:
        d_opc = open("./option/optionC.txt", "r")
        lp_optc = []
        for elt in d_opc:
            lp_optc = lp_optc + [int(elt.strip("\n"))]
        print(lp_optc)
        if lp_optc != 5 :
            print("optionCc")
    except:
        print("optionCE")
    return(None)

def load(fenetre , background) :
    return()