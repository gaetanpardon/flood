import pygame
from pygame.locals import *
# from images.troll import c #importe depuis le repertoire

pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((640, 480))

tex = 'blabla'  # c.lol()
font = pygame.font.Font(None, 45)

fond = pygame.image.load('magefonB.png').convert_alpha() #importe l'image et la converti pour usage
fenetre.blit(fond,(0,0)) # la colle en 0,0
pygame.key.set_repeat(400, 30)#delay avant de repete l'apuis de touche , fréquence de repétition (tuple de temps en mili s)

background = pygame.Surface((50,50)) # crée un rectagle
background = background.convert() #convertie en image
background.fill((0, 0, 0)) # change sa couleur

text = font.render(tex,1,(125,15,15)) # créer un texte (le texte , antaliasing , tuple couleur)
fenetre.blit(text,(200,200))
fenetre.blit(background,(100,100))
pygame.display.flip() # actualise la fenétre

perso_x = 0
perso_y = 0

flag = 1
position = fond.get_rect() # créer un tuple de position
#position.move('déplacement_x', 'déplacement_y') # modifie le tuple
while flag :

    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus

        if event.type == QUIT:     #Si un de ces événements est de type QUIT

            flag = 0      #On arrête la boucle
        if event.type == KEYDOWN: # KEYUP

            if event.key == K_SPACE:
                print("Espace")

            if event.key == K_RETURN:
                print("Entrée")

        if event.type == MOUSEMOTION:  # Si mouvement de souris
            # On change les coordonnées du perso
            perso_x = event.pos[0]
            perso_y = event.pos[1]


pygame.display. quit () #faire le display (automatique en cas de fin de script )