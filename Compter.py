#!/usr/bin/env python3

# *-* coding:utf-8 *-*


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

def explore(etat) :
    nbN = 1
    coupsPossibles = possibles(etat)
    nbCoupsPossibles = len(coupsPossibles)
    for coup in coupsPossibles :
        etat[coup[0]][coup[1]] = 1
        if nbCoupsPossibles == 1 :
            etat[coup[0]][coup[1]] = 0
            return 1
        nbN += explore(etat)
        etat[coup[0]][coup[1]] = 0
    return nbN
        
print(explore([[0,0,0], [0,0,0], [0,0,0]]))