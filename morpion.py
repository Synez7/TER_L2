#!/usr/bin/env python3


# *-* coding:utf-8 *-*

import numpy as np
import copy
from numpy.linalg import inv

global dimension


# print(np.diagonal(L))

# R = np.fliplr(L).diagonal()
# print("Antidiago ")
# print(R)


# tmp = copy.deepcopy(L)

# Z = np.delete(L,0,1)
# Y = np.delete(Z,0,0)
# print(L)
# print(Y)
# Minv = np.linalg.inv(L)
# print(Minv)

# print(dimension)



# print(colonnes)

# tmp1 = np.delete(L,0,0)
# print("Matrice :")
# print(L)
# print("Temporaire :")
# print(tmp1)


# dimension = np.shape(L)
# colonnes = dimension[1]
# # tmp1 = np.delete(L,0,2)
# print(L)
# print("APRES")
# print(np.delete(L,-1,0))  ### dernière ligne
# print("PASSAGE A 4*4")
# print(tmp1)




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
		Colonnes.append(L[i][i])

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
				if(l[j]==joueur):
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

	return trouve

grille =np.array([["7","0","7"],["0","0","0"],["0","0","0"],["0","0","0"]])

# grill=np.array([[1,0,0,0,9],[1,0,0,0,5],[1,0,0,0,4],[1,0,0,0,3],[1,0,0,0,2]])


print(grille)
print("JE TESTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
# print(rechercheDiagonales(grill))
# print("JE TESTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
print(estGagnant("7",grille))

# print(rechercheLignes(grill))
# print("JE TESTEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
# print(rechercheColonnes(grill))


