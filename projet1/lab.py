
import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))

fond = pygame.image.load('magefonB.png').convert_alpha() #importe l'image et la converti pour usage
fenetre.blit(fond,(0,0)) # la colle en 0,0
pygame.display.flip() # actualise la fenétre
pygame.key.set_repeat(400, 30)#delay avant de repete l'apuis de touche , fréquence de repétition (tuple de temps en mili s)


son = pygame.mixer.Sound("son.wav") #créer un objet son (de préferance utilisé des wav et ogg)

son.fadeout(300) #Fondu à 300ms de la fin de l'objet "son"
son.play()
son.stop()
pygame.mixer.pause()
pygame.mixer.unpause()

pygame.mixer.music.load("musique.wav") #créer une playliste et y ajoute musique
pygame.mixer.music.queue("instruments.wav") # ajout instu à la fin de la play liste

volume = pygame.mixer.music.get_volume() #Retourne la valeur du volume, entre 0 et 1
pygame.mixer.music.set_volume(0.5) #Met le volume à 0.5 (moitié)

nb_joysticks = pygame.joystick.get_count()#rend le nombre de joystique braché

mon_joystick = pygame.joystick.Joystick(0) #créer un objet joystick
mon_joystick.init() #Initialisation

pygame.time.get_ticks () # rend le temps en mili s
pygame.time. wait (500) #attend 500 mili s

pygame.transform.scale (Surface, (largeur, hauteur), DestSurface = None) -> Surface #redimention l'image
pygame.display. set_caption(titre, icontitle = None) #donne un tire à la fenétre
pygame.display. set_icon(Surface) # change l'icone de la fenétre
pygame.display. set_gamma (rouge, vert = None, bleu = None) #régle le gamma de base 1.0 # rend true si fonctione
pygame.display. set_gamma_ramp (rouge, vert, bleu) #régle le gamma à l'aide de table de 256 valeur de 0 à 0xffff rend true si fonctione

flag = 1
position = fond.get_rect() # créer un tuple de position
position.move('déplacement_x', 'déplacement_y') # modifie le tuple
while flag :

    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus

        if event.type == QUIT:     #Si un de ces événements est de type QUIT

            flag = 0      #On arrête la boucle
        if event.type == KEYDOWN: # KEYUP

            if event.key == K_SPACE:
                print("Espace")

            if event.key == K_RETURN:
                print("Entrée")


pygame.display. quit () #faire le display (automatique en cas de fin de script )