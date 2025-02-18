import pygame
import random
import sys
import time

#initialisation de pygame
pygame.init()

#definition des constantes
LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
TAILLE_CASE = 20
FPS = 10

#definition des couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
VERT = (0, 255, 0)

#definition du serpent
serpent = [(200, 200), (220, 200), (240, 200)]

#definition de la pomme
pomme = (random.randint(0, LARGEUR_ECRAN - TAILLE_CASE), random.randint(0, HAUTEUR_ECRAN - TAILLE_CASE))

#definition de la direction du serpent
direction = "droite"

#boucle principale du jeu
while True:
    #gestion des evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "bas":
                direction = "haut"
            elif event.key == pygame.K_DOWN and direction != "haut":
                definition = "bas"
            elif event.key == pygame.K_LEFT and direction != "droite":
                direction = "gauche"
            elif event.key == pygame.K_RIGHT and direction != "gauche":
                direction = "droite"

    #deplacement du serpent
    if direction == "haut":
        serpent.insert(0, (serpent[0][0], serpent[0][1] - TAILLE_CASE))
    elif direction == "bas":
        serpent.insert(0, (serpent[0][0], serpent[0][1] + TAILLE_CASE))
    elif direction == "gauche":
        serpent.insert(0, (serpent[0][0] - TAILLE_CASE, serpent[0][1]))
    elif direction == "droite":
        serpent.insert(0, (serpent[0][0] + TAILLE_CASE, serpent[0][1]))

    #gestion de la sortie dun serpent de l'ecran
    if serpent[0][0] < 0 or serpent[0][0] >= LARGEUR_ECRAN or serpent[0][1] < 0 or serpent[0][1] >= HAUTEUR_ECRAN:
        pygame.quit()
        sys.exit()

    #gestion de la collision du serpent avec lui-meme
    if serpent[0] in serpent[1:]:
        pygame.quit()
        sys.exit()

    #gestion de la collision avec la pomme
    if serpent[0] == pomme:
        pomme = (random.randint(0, LARGEUR_ECRAN - TAILLE_CASE), random.randint(0, HAUTEUR_ECRAN - TAILLE_CASE))
        serpent.append((serpent[-1][0], serpent[-1][1]))

    #affichage de l'ecran
    pygame.display.set_caption("jeu du serpent")
    ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
    ecran.fill(NOIR)

    #affichage du serpent
    for case in serpent:
        pygame.draw.rect(ecran, VERT, (case[0], case[1], TAILLE_CASE, TAILLE_CASE))

    #affichage de pomme
    pygame.draw.rect(ecran, 'red', (pomme[0], pomme[1], TAILLE_CASE, TAILLE_CASE))

    #rafraichissement de l'ecran
    pygame.display.update()

    #controle de la vitesse du jeu
    time.sleep(1 / FPS)
