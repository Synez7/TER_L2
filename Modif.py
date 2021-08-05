#!/usr/bin/env python3

# *-* coding:utf-8 *-*


import sys
import time

global coupsPossibles
global nbCoupsPossibles





# #####################   Fonction   #####################

def possibles(etat):
    possibles = []
    i = 0
    while i < len(etat) :
        j = 0
        while j < len(etat[i]) :
            if etat[i][j] == 0 :
                possibles.append([i,j])
            j += 1
        i += 1
    return possibles



def estPleine(etat):
    coupsPossibles = possibles(etat)
    if len(coupsPossibles) == 0:
        return True
    else:
        return False

def rechercheLignes(L):
    Lignes=[]
    for i in range(len(L)):
        Lignes.append(L[i])

    return Lignes

def rechercheColonnes(L):
    Colonnes=[]
    for i in range(len(L)):
        Colonnes.append([row[i] for row in L])

    return Colonnes




def rechercheDiagonales(L):

    nb_lignes = len(L[0])
    nb_colonnes = len(L)
    Diagonales_1 = [[] for i in range(nb_lignes + nb_colonnes - 1)]  # Liste des diagonales parcourues à partir de la première case du tableau
    Diagonales_2 = [[] for i in range(len(Diagonales_1))]  # Liste des diagonales parcourues à partir de la première case de la dernière ligne du tableau
    min_Diagonales_2 = - nb_lignes + 1

    for x in range(nb_lignes):
        for y in range(nb_colonnes):
            Diagonales_1[x+y].append(L[y][x])
            Diagonales_2[x-y-min_Diagonales_2].append(L[y][x])



   

    return Diagonales_1,Diagonales_2  ## Résultat Liste composée de 2 sous listes ( Diago parcourues en avant I  Diago parcoures en arrière)


# print(rechercheDiagonales([[1,2,3],[4,5,6],[7,8,9]]))

def estGagnant(joueur,etat):    ## Grille 3*3

    trouve = False

    ## CAS DES HORIZONTALES

    if etat[0][0] == joueur and etat[0][1] == joueur and etat[0][2] == joueur:
        trouve = True
    elif etat[1][0] == joueur and etat[1][1] == joueur and etat[1][2] == joueur:
        trouve = True
    elif etat[2][0] == joueur and etat[2][1] == joueur and etat[2][2] == joueur:
        trouve = True


    ## CAS DES VERTICALES

    elif etat[0][0] == joueur and etat[1][0] == joueur and etat[2][0] == joueur:

        trouve = True
    elif etat[0][1] == joueur and etat[1][1] == joueur and etat[2][1] == joueur:
        trouve = True
    elif etat[0][2] == joueur and etat[1][2] == joueur and etat[2][2] == joueur:
        trouve = True

    ## CAS DES DIAGONALES

    elif etat[0][0] == joueur and etat[1][1] == joueur and etat[2][2] == joueur:
        trouve = True
    elif etat[0][2] == joueur and etat[1][1] == joueur and etat[2][0] == joueur:
        trouve = True

    ## Score à renvoyer pour l'humain et l'IA si les coups gagnants ont été satisfaits

    # print("Le score est: \n")

    if joueur == 1 and trouve == True:
        
        return 1
    
    elif joueur == 2 and trouve == True:

        return - 1
    
    elif estPleine(etat):
        return 0


# print(estGagnant(2,[[1,1,1],[1,2,1],[1,1,2]]))



############################################################################


# def fin_partie(etat):

# 	return estGagnant(etat,1) or estGagnant(etat,2)



def affiche(etat, profondeur, joueur) :
    
    print(joueur, "("+str(profondeur)+") :")
    i = 0
    while i < len(etat) :
        j = 0
        while j < len(etat[i]) :
            print(etat[i][j], end="")
            j += 1
        print()
        i += 1
    print()





trace = False
nbNoeudsAAfficher = 0
nbNoeudsExplores = 0
if len(sys.argv) > 1 :
    trace = True
    nbNoeudsAAfficher = int(sys.argv[1])

def explore(etat, profondeur, joueur) :
    global nbNoeudsExplores
    nbNoeudsExplores += 1
    nbN = 1
    coupsPossibles = possibles(etat)
    nbCoupsPossibles = len(coupsPossibles)
    autreJoueur = "H"
    if joueur == "H": 
        autreJoueur = "IA"
    for coup in coupsPossibles :
        if joueur == "IA":
          
            etat[coup[0]][coup[1]] = 1
        else:
           
            etat[coup[0]][coup[1]] = 2
        if trace and nbNoeudsExplores <= nbNoeudsAAfficher: 
            affiche(etat, profondeur, joueur) 
        if nbCoupsPossibles == 1 :
            etat[coup[0]][coup[1]] = 0
            if trace and nbNoeudsExplores <= nbNoeudsAAfficher :
                print("REMONTEE : la grille est remplie")            
            return 1
        nbN += explore(etat, profondeur+1, autreJoueur)
        etat[coup[0]][coup[1]] = 0
    if trace and nbNoeudsExplores <= nbNoeudsAAfficher : 
        print("REMONTEE")
    return nbN
###TESTS

t1 = time.time()
print(explore(([[0,0,0,0],[0,0,0,0],[0,0,0,0]]),0,"H"))
t2 = time.time()
print("Temps d'execution : ",str(t2-t1),"s")
