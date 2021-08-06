#!/usr/bin/env python3

import sys
import pygame,random

def affiche(etat):
    i = 0
    while i < len(etat) :
        j = 0
        while j < len(etat[i]) :
            print(etat[i][j], end="")
            j += 1
        print()
        i += 1
    print()

def coupHumain(etat, typeJeu) :
    dim = len(etat)    
    while True :
        abs = input("Ligne (entre 0 et "+str(dim-1)+") ? ")
        ord = input("Colonne (entre 0 et "+str(dim-1)+") ? ")
        if abs.isdigit() and int(abs) >= 0 and int(abs) < dim and ord.isdigit() and int(ord) >= 0 and int(ord) < dim and etat[int(abs)][int(ord)] == 0  :
            if typeJeu == "p4" :
                if gravite(etat, int(abs), int(ord)) :
                    etat[int(abs)][int(ord)] = 2                    
                    return (int(abs), int(ord))
                else :
                    print("Coup impossible (gravité) !")
            else :
                etat[int(abs)][int(ord)] = 2
                return (int(abs), int(ord))
        print("Coup impossible (position) !")


def estGagnant(etat, nbPions, joueur, dernierCoup):
    ligne = dernierCoup[0]
    colonne = dernierCoup[1]
    dim = len(etat)
    pion = 1
    if joueur == "H" : 
        pion = 2
    # Vérification de la ligne où le dernier coup a été joué
    nbPionsAlignes = 0
    j = 0
    while j < dim :
        if etat[ligne][j] == pion :
            nbPionsAlignes += 1
            if nbPionsAlignes == nbPions : 
                return True
        else : 
            nbPionsAlignes = 0 
        j += 1
    # Vérification de la colonne où le dernier coup a été joué
    nbPionsAlignes = 0
    i = 0
    while i < dim :
        if etat[i][colonne] == pion :
            nbPionsAlignes += 1
            if nbPionsAlignes == nbPions : 
                return True
        else : 
            nbPionsAlignes = 0 
        i += 1
        
    # Vérification des diagonales où le dernier coup a été joué
    # Attention : la ligne du haut de la grille est la ligne 0
    nbPionsAlignes = 0
    lignetest = ligne
    colonnetest = colonne
    # On recule vers le bas pour trouver le point de départ d'une diagonale ascendante    
    while lignetest < dim-1 and colonnetest > 0 :
        lignetest += 1
        colonnetest -= 1
    # On repart du bas vers le haut
    while lignetest >= 0 and colonnetest < dim :
        if etat[lignetest][colonnetest] == pion :
            nbPionsAlignes += 1
            if nbPionsAlignes == nbPions : 
                return True
        else : 
            nbPionsAlignes = 0 
        lignetest -= 1
        colonnetest += 1

    nbPionsAlignes = 0
    lignetest = ligne
    colonnetest = colonne
    # On recule vers le haut pour trouver le point de départ d'une diagonale descendante
    while lignetest > 0 and colonnetest > 0 :
        lignetest -= 1
        colonnetest -= 1
    # On repart du haut vers le bas
    while lignetest < dim and colonnetest < dim :
        if etat[lignetest][colonnetest] == pion :
            nbPionsAlignes += 1
            if nbPionsAlignes == nbPions : 
                return True
        else : 
            nbPionsAlignes = 0 
        lignetest += 1
        colonnetest += 1
    # Aucun alignement n'a été trouvé
    return False


def gravite(etat, i, j) :
    if i == len(etat)-1 :
        return True
    if etat[i+1][j] != 0 :    
        return True 
    return False
   
def possibles(etat):
    dim = len(etat)
    possibles = []
    i = 0
    while i < dim :
        j = 0
        while j < len(etat[i]) :
            if etat[i][j] == 0 :
                if typeJeu == "p4" :
                    if gravite(etat, i, j) :
                        possibles.append([i,j])
                else :
                    possibles.append([i,j])
            j += 1
        i += 1
    return possibles

def min(scores) :
    scoreMin = scores[0]
    numCoupMin = 0
    numCoup = 1
    while numCoup < len(scores) :
        if scores[numCoup] < scoreMin :
            scoreMin = scores[numCoup]
            numCoupMin = numCoup
        numCoup += 1
    return numCoupMin

def max(scores) :
    scoreMax = scores[0]
    numCoupMax = 0
    numCoup = 1
    while numCoup < len(scores) :
        if scores[numCoup] > scoreMax :
            scoreMax = scores[numCoup]
            numCoupMax = numCoup
        numCoup += 1
    return numCoupMax

def explore(etat, nbPions, profondeur, joueur) :
    coupsPossibles = possibles(etat)
    nbCoupsPossibles = len(coupsPossibles)
    autreJoueur = "H"
    if joueur == "H" : autreJoueur = "IA"
    scores = []
    numCoup = 0
    for coup in coupsPossibles :
        if joueur == "IA" : 
            etat[coup[0]][coup[1]] = 1
        else : 
            etat[coup[0]][coup[1]] = 2
        if estGagnant(etat, nbPions, joueur, coup) == True :
            if joueur == "IA" :
                scores.append(1)
                etat[coup[0]][coup[1]] = 0
                break                    # car on n'a pas besoin d'envisager les coups suivants
            else :
                scores.append(-1)
                etat[coup[0]][coup[1]] = 0
                break                    # ...
        else :
            if nbCoupsPossibles == 1 :
                scores.append(0)  # Partie bloquée
            else :
                scores.append(explore(etat, nbPions, profondeur+1, autreJoueur))
        etat[coup[0]][coup[1]] = 0
        numCoup += 1
    if joueur == "H" :
        numCoup = min(scores)
        if profondeur == 0 :  # Pour renvoyer les coordonnées du coup à jouer à la boucle de jeu
            return coupsPossibles[numCoup]
        return scores[numCoup]
    if joueur == "IA" :
        numCoup = max(scores)
        if profondeur == 0 :  # Pour renvoyer les coordonnées du coup à jouer à la boucle de jeu
            return coupsPossibles[numCoup]
        return scores[numCoup]

if len(sys.argv) != 4 :
    print("Usage : ttt_ou_p4.py <ttt ou p4> <dimension> <nb pions à aligner>")
    exit()
if sys.argv[1] != "ttt" and sys.argv[1] != "p4" :
    print("Le premier paramètre doit être ttt (tic-tact-toe) ou p4 (puissance4)")
    exit()    
if not sys.argv[2].isdigit() or not sys.argv[3].isdigit() : 
    print("La dimension et le nombre des pions doivent être des entiers")
    exit()

typeJeu = "ttt"
if sys.argv[1] == "p4" :    
    typeJeu = "p4"
dimension = int(sys.argv[2])
nbPions = int(sys.argv[3])
etat = [[] for i in range(0, dimension)]
for i in range(0, dimension) :
    for j in range(0, dimension) :
        etat[i].append(0)
print(typeJeu)
print(etat)


####################  INTERFACE GRAPHIQUE  #####################

# taille_case = 100                     ## Taille en pixels d'une case de la grille de jeu
# rayon_cercle = int(taille_case/2 - 4) ## Rayon du cercle 
# cadre = (0, 0, 255)                   ## Cadre bleue de la grille de jeu
# blanc = (255, 255, 255)               ## Case initialement non remplie
# jeton_rouge = (255, 0, 0)             ## Jeton utilisé par l'utilisateur
# jeton_jaune = (255, 255, 0)           ## Jeton utilisé par l'IABoucle de jeu

# pion_joueur = 2                       ## pion utilisé par l'utilisateur
# pion_IA = 1                           ## pion utilisé par l'IA

# humain = 0                            ## Variables 'humain' et 'IA' utilisées pour définir les tours de jeu
# IA = 1


# largeur = len(etat[0]) * taille_case         ## Dimensions de la grille de jeu
# hauteur = (len(etat) + 1) * taille_case


# pygame.init()



# def inserer_jeton(etat,i,j,pion):          ## Fonction permettant l'insertion d'un jeton de joueur (Utilisateur / IA)
#     if i < len(etat) and j < len(etat[0]): ## etat : grille de jeu , i : abscisse du jeton inséré
#         etat[i][j] = pion                  ## j : ordonnée du jeton inséré , pion : 1 ou 2

# def emplacementValide(etat,colonne):     ## Fonction vérifiant  si une case de la grille de jeu est inoccupée avant l'inserion d'un jeton de joueur
#     if etat[len(etat)-1][colonne] == 0:  ## Le jeton inséré doit occuper la position la plus basse sur une colonne (gravité)
#         return True                      ## colonne : ordonnée de la case donnée
#     else:
#         return False


# def rangeeSuivante(etat, colonne):   ## Fonction recherchant une ligne non occupée de la grille de jeu
#     for ligne in range(len(etat)):   
#         if etat[ligne][colonne] == 0:
#             return ligne


# grille = pygame.display.set_mode((largeur, hauteur)) # Définition de la grille de jeu
# def grilleApparition(etat):
#     for colonne in range(len(etat[0])):
#         for ligne in range(len(etat)):
#             ## Construction des emplacements pour l'insertion des jetons
#             pygame.draw.rect(grille, cadre, (colonne*taille_case, (ligne+1)* taille_case, taille_case, taille_case))
#             pygame.draw.circle(grille, blanc, (int(colonne*taille_case + taille_case/2), int((ligne+1)*taille_case + taille_case/2)), rayon_cercle)
    
#     for colonne in range(len(etat[0])):
#         for ligne in range(len(etat)):
#             # Si c'est au tour de l'humain d'insérer un jeton, création d'un jeton rouge à insérer dans la case souhaitée
#             if etat[ligne][colonne] == pion_joueur:
#                 pygame.draw.circle(grille, jeton_rouge, (int(colonne*taille_case + taille_case/2), hauteur-int((ligne)*taille_case + taille_case/2)), rayon_cercle)
#             # Si c'est au tour de l'IA d'insérer un jeton, création d'un jeton jaune à insérer dans la case souhaitée
#             elif etat[ligne][colonne] == pion_IA:
#                 pygame.draw.circle(grille, jeton_jaune, (int(colonne*taille_case + taille_case/2), hauteur-int((ligne)*taille_case + taille_case/2)), rayon_cercle)
#     # Mise à jour de la grille de jeu
#     pygame.display.update()




# def jeu(etat):
#     fin_partie = False
#     myfont = pygame.font.SysFont("comicsansms", 40) ## Police d'écriture utilisée pour l'affichage du gagnant de la partie / égalité
#     tour = random.randint(humain,IA)    ## Gestion des tours de jeu 

#     while not fin_partie and len(possibles(etat)) != 0:  
#         for event in pygame.event.get():
#             ## Si clic sur la croix de la fenêtre d'affichage, celle-ci se ferme
#             if event.type == pygame.QUIT: 
#                 sys.exit()

#             if event.type == pygame.MOUSEMOTION: ## Mouvement du curseur
#                 pygame.draw.rect(grille, blanc, (0,0, largeur, taille_case)) ## Bande horizontale blanche au-dessus de la grille de jeu
#                 posx = pygame.mouse.get_pos()[0]  ## Récupération des coordonnées de position (x;y) du curseur de la souris
#                 if tour == humain:  ## Si c'est au tour de l'humain de jouer, celui-ci va devoir insérer un jeton rouge dans la case désirée
#                     pygame.draw.circle(grille, jeton_rouge, (posx, int(taille_case/2)), rayon_cercle)
#                 else:  ## Jeton jaune dans le cas où c'est à l'IA de commencer la partie
#                     pygame.draw.circle(grille, jeton_jaune, (posx, int(taille_case/2)), rayon_cercle)


#             pygame.display.update()  ## Actualisation de la fenêtre d'affichage


#             if event.type == pygame.MOUSEBUTTONDOWN:  ## Evenement : clic gauche de la souris sur un emplacement inoccupée de la grille de jeu
#                 pygame.draw.rect(grille, blanc, (0,0, largeur,taille_case))
           
#                 if tour == humain:
#                     posx = pygame.mouse.get_pos()[0]   ## Position en abscisse du curseur par rapport à la fenêtre d'affichage     
#                     col = posx // taille_case          ## Position en ordonnée du curseur par rapport à la fenêtre d'affichage
               
#                     if emplacementValide(etat, col):
#                         ligne = rangeeSuivante(etat, col)  ## Insertion du jeton de l'utilisateur dans le cas où la situation est favorable
#                         inserer_jeton(etat, ligne, col, 2)

#                         if estGagnant(etat,sys.argv[3],"H",[0,0,0]):     ## Si l'utilisateur remporte la partie, un message s'affiche en haut de la grille
#                             label = myfont.render("Victoire de l'humain !", 1, jeton_rouge)
#                             grille.blit(label, (40,10))
#                             fin_partie = True

#                         tour += 1         ## Incrémentation des tours pour permettre aux joueurs de jouer l'un après l'autre
#                         tour = tour % 2

#                         ## Mise à jour de la grille de jeu après plusieurs insertions de jetons
#                         grilleApparition(etat)
#                         affiche(etat)    ## Affichage de la grille en format ASCII sur le Terminal de Commandes

#             if tour == IA and not fin_partie:
#                 longueur = len(possibles(etat))
#                 coup = possibles(etat)[longueur//2] ## Jeton placé sur la 4e colonne de la grille 
#                 colonne = coup[1]              

#                 if emplacementValide(etat, colonne):
#                     ligne = rangeeSuivante(etat, colonne)
#                     inserer_jeton(etat, ligne, colonne, 1)

#                     if estGagnant(etat, sys.argv[3], "IA",[0,0,0]):
#                         ## Si l'IA remporte la partie, un message s'affiche en haut de la grille
#                         label = myfont.render("Victoire de l'IA !", 1, jeton_jaune) 
#                         grille.blit(label, (40, 10))
#                         fin_partie = True

                   
                    

#                     tour += 1
#                     tour = tour % 2

#                     grilleApparition(etat)
#                     affiche(etat)

#             if(possibles(etat) == [] and not (estGagnant(etat, sys.argv[3], "IA",[0,0,0]) == True) and not (estGagnant(etat, sys.argv[3], "H",[0,0,0]) == True)):
#                 ## Message affiché sur la bande horizontale blanche, dans le cas d'une saturation de la grille 
#                 label = myfont.render("MATCH NUL", 1, (0,0,255)) 
#                 grille.blit(label, (40, 10))
#                 pygame.time.wait(3000)
                    
#             if fin_partie:
#                 pygame.time.wait(3000) 
#             ## La fenêtre d'affichage se ferme 3000 ms après que la partie soit terminée


# print(jeu(etat))

###########ABDELLAH

# Boucle de jeu
while True :
    
    print("L'IA réfléchit...")
    meilleurCoup = explore(etat, sys.argv[3], 0, "IA")
    etat[meilleurCoup[0]][meilleurCoup[1]] = 1
    affiche(etat)
    if estGagnant(etat, nbPions, "IA", meilleurCoup) == True :
        print("Victoire de l'IA")
        exit()
    if possibles(etat) == [] :
        print("Grille pleine et aucun gagnant !")
        exit()
    #continuer = input("Voulez-vous arrêter la partie ? (oui ou non) : ")
    #if continuer == "oui":
    #    print("Partie arrêtée ! Aucun gagnant")
    #    exit()
    #else :
    coupH = coupHumain(etat, typeJeu)
    affiche(etat)
    if estGagnant(etat, nbPions, "H", coupH) == True:
        print("Victoire de l'humain")
        exit()             