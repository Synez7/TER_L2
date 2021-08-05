#!/usr/bin/env python3

# *-* coding:utf-8 *-*

import sys
import time


def affiche(etat) :
    i = 0
    while i < len(etat) :
        j = 0
        while j < len(etat[i]) :
            print(etat[i][j], end="")
            j += 1
        print()
        i += 1
    print()


def coupHumain(etat) :
    dim = len(etat)    
    while True :
        abs = input("Ligne (entre 0 et 2) ? ")
        ord = input("Colonnee (entre 0 et 2) ? ")
        if abs.isdigit() and int(abs) >= 0 and int(abs) < dim and ord.isdigit() and int(ord) >= 0 and int(ord) < dim and etat[int(abs)][int(ord)] == 0 :
            etat[int(abs)][int(ord)] = 2
            return
        print("Coup impossible !")



# def estGagnant(etat, nbPions, joueur) :
#     # Ne fonctionne pour l'instant que sur une grille carrée (tests des horizontales/verticales)
#     # et 3x3 (tests des deux grandes diagonales )
#     dim = len(etat)
#     pion = 2
#     if joueur == "IA": 
#         pion = 1
#     # Recherche d'un alignement horizontal
#     i = 0
#     while i < dim :
#         nbPionsAlignes = 0
#         j = 0
#         while j < dim :
#             if etat[i][j] == pion : 
#                 nbPionsAlignes += 1
            
#             if nbPionsAlignes == nbPions : 
#                 return True
#             else:
#                 nbPionsAlignes = 0
            
#             j += 1
#         i += 1
#     # Recherche d'un alignement vertical 
#     i = 0
#     while i < dim :
#         nbPionsAlignes = 0
#         j = 0
#         while j < dim :
#             if etat[j][i] == pion : 
#                 nbPionsAlignes += 1
#             if nbPionsAlignes == nbPions : 
#                 return True
#             else:
#                 nbPionsAlignes = 0
#             j += 1
#         i += 1
#     # Recherche d'un alignement diagonal
#     # programmation "brutale" pour les deux grandes diagonales
#     # à adapter pour des grilles plus grandes
#     i = 0
#     nbPionsAlignes = 0
#     while i < dim :
#         if etat[i][i] == pion : 
#             nbPionsAlignes += 1
#         if nbPionsAlignes == nbPions : 
#             return True
#         i += 1
#     i = 0
#     nbPionsAlignes = 0
#     while i < dim :
#         if etat[i][dim -1 -i] == pion : nbPionsAlignes += 1
#         if nbPionsAlignes == 3 : return True
#         i += 1
#     # Sinon, estGagnant() renvoie faux
#     return False


# print(estGagnant([[1,1,0],[0,0,0],[0,0,0]], 3, "H"))

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
            if etat[i][j] == 0 and gravite(etat, i, j) :
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




def extraction_diag(etat):   ## Retourne une liste de 2 sous-liste contenant les diagonales avant " \ " et les diagonales arrière " / "
    nbreLignes = len(etat)
    nbreColonnes = len(etat[0])
    
    diagonales_arriere = [[] for i in range(nbreColonnes + nbreLignes - 1)]  ## Création d'une liste contenant les diagonales arrières " / "
    diagonales_avant = [[] for i in range(len(diagonales_arriere))]   ##  Création d'une liste contenant les  " \ "
    min_diagonales_avant = - nbreLignes + 1

    for x in range(nbreColonnes):
        for y in range(nbreLignes):
            diagonales_arriere[x+y].append(etat[y][x])
            diagonales_avant[x-y-min_diagonales_avant].append(etat[y][x])

   
    return diagonales_avant,diagonales_arriere

### TESTS POUR L'EXTRACTION DES DIAGONALES AVANT ET ARRIERE D'UNE GRILLE M * N ###

# print(extraction_diag(([[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0]]))[0])
# print(extraction_diag(([[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0]]))[1])


def estGagnant(etat,nbPions,joueur):

    

    nbreLignes = len(etat)      ## Récupération du nombre de lignes d'une grille m * n étant m
    nbreColonnes = len(etat[0]) ## Récupération du nombre de colonnes d'une grille m * n étant n
    diagonales_avant = extraction_diag(etat)[0]  ## Liste des diagonales avant d'une grille quelconque
    diagonales_arriere = extraction_diag(etat)[1] ## Liste des diagonales arrière d'une grille quelconque
    pion = 2
    
    if joueur == "IA": 
        pion = 1

    # if (nbPions > nbreLignes and nbPions > nbreColonnes) or nbPions < 0:  ## Vérification  (nbPions <= m  ou nbPions <= n)
    #     print("Le nombre de pions à aligner pour gagner ne doit pas dépasser la hauteur et la largeur de la grille !")



    
        ###    Vérification  de l'alignement horizontal de nbPions     ###
           ############################################################

    for ligne in range(nbreLignes): 
        nbPionsAlignes = 0
        for colonne in range(nbreColonnes):
            if etat[ligne][colonne] == pion:
                nbPionsAlignes += 1
            else:
                nbPionsAlignes = 0        # Remise à zéro nbPionsAlignés lorsqu'un pion adverse est rencontré
            if nbPionsAlignes == nbPions:
                return True


        ###    Vérification  de l'alignement vertical de nbPions      ###
           ###########################################################


    for colonne in range(nbreColonnes):
        nbPionsAlignes = 0
        for ligne in range(nbreLignes):
            if etat[ligne][colonne] == pion:
                nbPionsAlignes += 1
            else:
                nbPionsAlignes = 0

            if nbPionsAlignes == nbPions:
                return True

        ###    Vérification  de l'alignement de nbPions à partir des diagonales avants " \ " ###
           ################################################################################

    for d in diagonales_avant:
        nbPionsAlignes = 0  ## Parcours de la liste contenant les diagonales avant
        for case in d:
            if case == 0:   ## Vérification de la case si celle-ci est égale à 0 , on parcourt la case suivante [0,0,1,0] 
                nbPionsAlignes = 0
            if case == pion:
                nbPionsAlignes += 1 ## Trou rencontré en la présence d'un pion adverse
            else:
                nbPionsAlignes = 0  
            
            if nbPionsAlignes == nbPions:    

                return True

        ###    Vérification  de l'alignement de nbPions à partir des diagonales arrières " / " ###
           ##################################################################################

    for d in diagonales_arriere:
        nbPionsAlignes = 0   ## Parcours de la liste contenant les diagonales avant
        for case in d:
            if case == 0:
                nbPionsAlignes = 0
            if case == pion:
                nbPionsAlignes += 1
            else:
                nbPionsAlignes = 0

            if nbPionsAlignes == nbPions:
                return True

    return False                          ## Cas où aucune combinaison gagnante est satisfaite au cours de la partie jouée


## Remarques : J'ai essayé d'implémenté votre idée concernant la gestion de l'indice en abscisse notamment.
## J'ai rencontré qques soucis par rapport à cela, cette fonction générique semble pour moi pas la plus optimisée avec la multitude de boucles.
## Il est bien possible de compacter le code pour ce qu'il en est de la vérification de l'alignement horizontal avec celle de l'alignement vertical, comme pour les diagonales.


# t1 = time.time()
# print(estGagnantV2(([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]]),4,"IA"))
# t2 = time.time()
# print("Temps d'execution : ",str(t2-t1),"s")




def explore(etat, profondeur, joueur) :
    coupsPossibles = possibles(etat)
    nbCoupsPossibles = len(coupsPossibles)
    autreJoueur = "H"
    if joueur == "H" : autreJoueur = "IA"
    scores = []
    numCoup = 0
    for coup in coupsPossibles :
        if joueur == "IA" : etat[coup[0]][coup[1]] = 1
        else : etat[coup[0]][coup[1]] = 2
        if estGagnant(etat, 4, joueur) == True :
            if joueur == "IA" :
                scores.append(1)     # Une optimisation pourrait être implémentée dans ce cas
                etat[coup[0]][coup[1]] = 0
                numCoup += 1
                break                    # car on n'a pas besoin d'envisager les coups suivants
            else :
                scores.append(-1) # idem
                etat[coup[0]][coup[1]] = 0
                numCoup += 1
                break #break permet de sortir de la boucle pour ne plus envisager les autres cas l
        else :
            if nbCoupsPossibles == 1 :
                scores.append(0)  # Partie bloquée
            else :
                scores.append(explore(etat, profondeur+1, autreJoueur))
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
    
etat = [[0,0,0,0,1,1,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
print(explore(etat,3,"IA"))
# Boucle de jeu

    
# while True :
#     print("L'IA réfléchit...")
#     meilleurCoup = explore(etat, 0, "IA")
#     etat[meilleurCoup[0]][meilleurCoup[1]] = 1
#     affiche(etat)
#     if estGagnant(etat, 4, "IA") == True :
#         print("Victoire de l'IA")
#         exit()
#     else :
#         if possibles(etat) == [] and not(estGagnant(etat, 4, "IA") == True) and not(estGagnant(etat, 4, "H") == True): 
#                 print("Grille pleine et aucun gagnant !")
#                 exit()
#     continuer = input("Voulez-vous arrêter la partie ? (oui ou non) : ")
#     if continuer == "oui":
#         print("Partie arrêtée ! Aucun gagnant")
#         exit()
#     else :
#         coupHumain(etat)
#         affiche(etat)
#         if estGagnant(etat, 4, "H") == True:
#             print("Victoire de l'humain")
#             exit()    
