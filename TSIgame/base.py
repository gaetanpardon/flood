
import pygame
from pygame.locals import *
from lib import start as st
from lib import game as g

pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((1080, 720))

p_fond = pygame.image.load('fonddebug.png').convert_alpha() #importe l'image et la converti pour usage
p_position = p_fond.get_rect() # créer un tuple de position
fenetre.blit(p_fond,p_position) # la colle en 0,0
pygame.display.flip() # actualise la fenétre

background = pygame.Surface((1080,720)) # crée un rectagle
background = background.convert() #convertie en image
background.fill((0, 0, 0)) # change sa couleur
p_Sback = pygame.Surface((180,20)) # crée un rectagle
p_Sback = p_Sback.convert() #convertie en image
p_Sback.fill((0, 0, 0)) # change sa couleur

p_Cback = pygame.Surface((20,180)) # crée un rectagle
p_Cback = p_Cback.convert() #convertie en image
p_Cback.fill((0, 0, 0)) # change sa couleur
st.menu(fenetre,background)
p_cursory=2000
p_cursorx=2000
flag=0
while flag :

    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus

        if event.type == pygame.locals.QUIT:     #Si un de ces événements est de type QUIT

            flag = 0      #On arrête la boucle
        if event.type == pygame.locals.KEYDOWN: # KEYUP

            if event.key == pygame.locals.K_ESCAPE:
                flag=0

            if event.key == pygame.locals.K_RETURN:
                print("Entrée")

        if event.type == pygame.locals.MOUSEMOTION:  # Si mouvement de souris
            # On change les coordonnées du perso
            p_cursorx = event.pos[0]
            p_cursory = event.pos[1]
            #print('ok')
    if p_cursory > 500:
        p_position=p_position.move(0,-10)
        #print('upy')
    if p_cursory < 100 :
        p_position=p_position.move(0,10)
        #print('downy')
    if p_cursorx > 900 :
        p_position=p_position.move(-10, 0)
        #print('upx')
    if p_cursorx < 100 :
        p_position=p_position.move(10,0)
        #print("downx")



    #print(p_position)
    fenetre.blit(background,(0,0))
    fenetre.blit(p_fond, p_position)  # la colle en ppos

    fenetre.blit(p_Sback,(800,10))
    fenetre.blit(p_Sback, (800, 50))
    fenetre.blit(p_Sback, (10, 10))
    fenetre.blit(p_Sback, (10, 50))
    fenetre.blit(p_Cback, (20, 500))
    fenetre.blit(p_Cback, (1050, 500))

    pygame.display.flip()  # actualise la fenétre

    pygame.time.wait(30)  # attend 500 mili s

pygame.display. quit () #faire le display (automatique en cas de fin de script )