#!/usr/bin/env python3

# *-* coding:utf-8 *-*


import sys
import numpy as np
import copy
from numpy.linalg import inv

global dimension
global coupsPossibles
global nbCoupsPossibles

IA = 'O'
H = 'X'

etat = [['' for x in range(3)] for y in range(3)]



#####################   Fonctions de RECHERCHE   #####################


def rechercheDiagonales(L):


    Diagonales = []

    tmp1 = copy.deepcopy(L)

    diag = np.diagonal(L)

    anti_diag = np.fliplr(L).diagonal()

    tmp2 = copy.deepcopy(L)

    Diagonales.append(diag)
    Diagonales.append(anti_diag)

    while np.size(tmp1) > 16:

        tmp1 = np.delete(tmp1,0,0) ## première ligne

        tmp1 = np.delete(tmp1,-1,-1) ## dernière colonne


        tmp2 = np.delete(tmp2,0,1)  ## Première colonne

        tmp2 = np.delete(tmp2,-1,0) ## dernière ligne

        diag = np.diagonal(tmp1)

        anti_diag = np.fliplr(tmp1).diagonal()

        Diagonales.append(diag)
        Diagonales.append(anti_diag)

        diag = np.diagonal(tmp2)

        anti_diag = np.fliplr(tmp2).diagonal()

        Diagonales.append(diag)
        Diagonales.append(anti_diag)


    return Diagonales

def rechercheLignes(L):
    dimension = np.shape(L)
    lignes = dimension[0]

    Lignes=[]
    for i in range(lignes):
        Lignes.append(L[i])

    return Lignes

def rechercheColonnes(L):
    dimension = np.shape(L)
    colonnes = dimension[1]

    Colonnes=[]
    for i in range(colonnes):
        Colonnes.append(L[:,i])

    return Colonnes


# grill=np.array([[1,0,0,0,9],[1,0,0,0,5],[1,0,0,0,4],[1,0,0,0,3],[1,0,0,0,2]])

# #####################   Fonction   #####################

def estGagnant(joueur,L):

    cpt_horizontal = 0
    cpt_vertical = 0
    cpt_diagonale = 0
    dimension = np.shape(L)

    trouve=False

    lignes=rechercheLignes(L)
    colonnes=rechercheColonnes(L)
    diagonales=rechercheDiagonales(L)
    i=0
    s=0

    if (np.size(L)==9):

        while (i < 3 and trouve==False):
            l=lignes[i]
            c=colonnes[i]

            if(l[0]==joueur and l[1]==joueur and l[2]==joueur):
                trouve=True
            if(c[0]==joueur and c[1]==joueur and c[2]==joueur):
                trouve=True
            
            i=i+1

            for j in range(2):
                d=diagonales[j]
                if(d[0]==joueur and d[1]==joueur):
                    trouve=True
    
    else:

        while(i < len(lignes) and trouve == False):

            l=lignes[i]
            c=colonnes[i]
            j=0
            while(cpt_horizontal<4 and cpt_vertical<4 and j<len(colonnes)):
                if(l[j]==pion):
                    cpt_horizontal+=1
                else:
                    cpt_horizontal=0
                if(c[j]==joueur) :
                    cpt_vertical+=1
                else:
                    cpt_vertical=0
                j+=1
            if(cpt_vertical==4 or cpt_horizontal==4):
                    trouve=True
            i+=1
        
        while(s<len(diagonales) and trouve==False):
            j=0
            d=diagonales[s]
            while(cpt_diagonale<4 and j<len(colonnes)):
                if(d[j]==joueur):
                    cpt_diagonale+=1
                else:
                    cpt_diagonale=0
                j+=1
            if(cpt_diagonale==4):
                trouve=True
            s+=1
    # print("Le joueur",joueur," a remporté la partie")
    return trouve


############################################################################



def fin_partie(etat):

	return estGagnant(etat,1) or estGagnant(etat,2)



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


print(affiche(np.array([[0,1,0],[0,0,0],[0,0,0]]),1,1))
        
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


# def estPleine(etat):

#     coupsPossibles = possibles(etat)
#     nbCoupsPossibles = len(coupsPossibles)



#     if(nbCoupsPossibles== 0):

#         print("Grille Pleine")
#         return True
#     else:

#         print("Grille non pleine")
#         return False

def estPleine(etat):

    if len(coupsPossibles) == 0:
        return True
    else:
        return False








def score_joueur(etat):
    global score

    if estGagnant("IA",etat) == True:
        score = 1

    elif estGagnant("H",etat) == True:
        score = -1
    else:
        print(" La grille est pleine !")

        score = 0

        print("Score :")

    return score






def minimax(etat, profondeur, joueur):
    coupsPossibles = possibles(etat)
    nbCoupsPossibles = len(coupsPossibles)
    scoreCoups = []

    if joueur == "IA":
        L = [-1,-1,-10]
    else:
        L = [-1,-1,10]

	if(profondeur == 0 or fin_partie(etat)):

		score = score_joueur(etat)

		for coup in coupsPossibles:

			etat[coup[0]][coup[1]] = 1
			infos = minimax(etat,profondeur-1,joueur)
            scoreCoups.append(infos)
			etat[coup[0]][coup[1]] = 2
			score[0] = coup[0]
            score[1] = coup[1]

		if joueur == "IA":

            return max(scoreCoups)

        else:

            return min(scoreCoups)


print(minimax(np.array([[1,0,0],[0,0,0],[2,0,0]]),1,"IA"))




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

 



