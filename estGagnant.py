#!/usr/bin/env python3

# *-* coding:utf-8 *-*

import time


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


def estGagnantV2(etat,nbPions,joueur):

    

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


t1 = time.time()
print(estGagnantV2(([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]]),4,"IA"))
t2 = time.time()
print("Temps d'execution : ",str(t2-t1),"s")
