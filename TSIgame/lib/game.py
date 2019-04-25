
import pygame
from pygame.locals import *
#from lib import start as st



def game (fenetre , background ) :
    fenetre.blit(background, (0, 0))
    font = pygame.font.Font(None, 45)
    p_tableau = pygame.image.load('./image/Dtableau.png').convert_alpha()  # importe l'image et la converti pour usage

    p_table = pygame.image.load('./image/Dtable.png').convert_alpha()  # importe l'image et la converti pour usage
    p_voisin = pygame.image.load('./image/Dvoisin.png').convert_alpha()
    p_postax =[0,0,0]
    p_postay = [0,0,0]
    p_vue = 0
    fenetre.blit(p_table, (p_postax[p_vue],p_postay[p_vue] ))  # la colle en 0,0
    p_objet = [p_table,p_tableau,p_voisin]
    p_cursory = 200
    p_cursorx = 200
    flag = 1
    while flag:

        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus

            if event.type == pygame.locals.QUIT:  # Si un de ces événements est de type QUIT

                flag = 0  # On arrête la boucle
            if event.type == pygame.locals.KEYDOWN:  # KEYUP

                if event.key == pygame.locals.K_ESCAPE:
                    flag = 0

                if event.key == 273 :
                    print("arrow")
                    p_vue=1
                    print(p_vue)

                if event.key == 275:
                    print("arrow")
                    p_vue = 2
                    print(p_vue)

            if event.type == pygame.locals.KEYUP:  # KEYUP

                if event.key == 273:
                    print("arrow")
                    p_vue = 0
                    print(p_vue)

                if event.key == 275:
                    print("arrow")
                    p_vue = 0
                    print(p_vue)


            if event.type == pygame.locals.MOUSEMOTION:  # Si mouvement de souris
                # On change les coordonnées du perso
                p_cursorx = event.pos[0]
                p_cursory = event.pos[1]
                # print('ok')

        if p_cursory > 500 and p_postay[p_vue] > -360  :
            p_postay[p_vue] = p_postay[p_vue] -3
            # print('upy')
        if p_cursory < 100 and  0> p_postay[p_vue] :
            p_postay[p_vue] = p_postay[p_vue] + 3
            # print('downy')
        if p_cursorx > 900 and p_postax[p_vue] > -540  :
            p_postax[p_vue] = p_postax[p_vue] -3
            # print('upx')
        if p_cursorx < 100 and 0> p_postax[p_vue]  :
            p_postax[p_vue] = p_postax[p_vue] + 3
            # print("downx")

        # print(p_position)
        fenetre.blit(background, (0, 0))
        fenetre.blit(p_objet[p_vue], (p_postax[p_vue],p_postay[p_vue] ))

        pygame.display.flip()
        pygame.time.wait(30)