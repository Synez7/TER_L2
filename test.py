#!/usr/bin/env python3


# *-* coding:utf-8 *-*

import numpy as np
import copy
from numpy.linalg import inv


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




#####################  RECHERCHER DIAGONALES   #####################


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


print(np.array([[1,0,0,0,9],[1,0,0,0,5],[1,0,0,0,4],[1,0,0,0,3],[1,0,0,0,2]]))

print(rechercheDiagonales([[1,0,0,0,9],[1,0,0,0,5],[1,0,0,0,4],[1,0,0,0,3],[1,0,0,0,2]]))






def winCheck(etat):

	vertical = 0
	horizontal = 0
	diagonal = 0
	anti_diagonal = 0

	