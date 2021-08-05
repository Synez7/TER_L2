import sys

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

def coupHumain(etat) :
    nbLignes = len(etat)
    nbColonnes = len(etat[0])
    while True :
        abs = input("Ligne (entre 0 et "+str(nbLignes-1)+") ? ")
        ord = input("Colonne (entre 0 et "+str(nbColonnes-1)+") ? ")
        if abs.isdigit() and int(abs) >= 0 and int(abs) < nbLignes and ord.isdigit() and int(ord) >= 0 and int(ord) < nbColonnes and etat[int(abs)][int(ord)] == 0  and gravite(etat, int(abs), int(ord)) :
            etat[int(abs)][int(ord)] = 2
            return [int(ord), int(abs)]
        print("Coup impossible !")
    return

###### ALI


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

###### ALI


def estGagnant(etat,nbPions,joueur,dernierCoup):
    nombrePionsAlignes = 0
    indice_ligne = dernierCoup[0]
    indice_colonne = dernierCoup[1]
    
    
    if joueur == "IA":
        pion = 1
    else:
        pion = 2


    for j in range(len(etat[0])):              # Exploration de la ligne contenant le case du dernier coup joué
        if etat[indice_ligne][j] == pion:
            nombrePionsAlignes += 1
        else:
            nombrePionsAlignes = 0
        if nombrePionsAlignes == nbPions:
            return True

    for i in range(len(etat)):           # Exploration de la colonne contenant la case du dernier coup joué
        if etat[i][indice_colonne] == pion:
            nombrePionsAlignes += 1
        else:
            nombrePionsAlignes = 0
        if nombrePionsAlignes == nbPions:
            return True

 




print("TEST")
print(estGagnant(([[1,0,0],[0,1,0],[0,0,1],[0,0,0]]),3,"IA",[0,0]))

# t1 = time.time()
# print(estGagnant(([[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0]]),4,"IA"))
# t2 = time.time()
# print("Temps d'execution : ",str(t2-t1),"s")

def gravite(etat, i, j) :
    if i == len(etat)-1 :
        return True
    if etat[i+1][j] != 0 :
        return True
    return False

############LEA

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

def explore(etat, nbPions, profondeur, joueur) :
    coupsPossibles = possibles(etat)
    nbCoupsPossibles = len(coupsPossibles)
    autreJoueur = "H"
    if joueur == "H" : autreJoueur = "IA"
    scores = []
    numCoup = 0
    for coup in coupsPossibles :
        if joueur == "IA" : etat[coup[0]][coup[1]] = 1
        else : etat[coup[0]][coup[1]] = 2
        if estGagnant(etat, 3, joueur, coup) == True :
            if joueur == "IA" :
                scores.append(1)
                etat[coup[0]][coup[1]] = 0
                break                    # car on n'a pas besoin d'envisager les coups suivants
            else :
                scores.append(-1)
                etat[coup[0]][coup[1]] = 0
                break #break permet de sortir de la boucle pour ne plus envisager les autres cas l
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


# if len(sys.argv) != 3 :
#     print("Usage : puissance4 <dimension> <nb pions à aligner>")
#     exit()
# if not sys.argv[1].isdigit() or not sys.argv[2].isdigit() :
#     print("La dimension et le nombre des pions doivent être des entiers")
#     exit()

# dimension = int(sys.argv[1])
# nbPions = int(sys.argv[2])
# etat = [[] for i in range(0, dimension)]
# for i in range(0, dimension) :
#     for j in range(0, dimension) :
#         etat[i].append(0)
# print(etat)

############ABDELLAH


#Boucle de jeu
# while True :

#     print("L'IA réfléchit...")
#     meilleurCoup = explore(etat, 4, 0, "IA")
#     etat[meilleurCoup[0]][meilleurCoup[1]] = 1
#     affiche(etat)
#     if estGagnant(etat, 4, "IA",meilleurCoup) == True :
#         print("Victoire de l'IA")
#         exit()
#     if possibles(etat) == [] :
#         print("Grille pleine et aucun gagnant !")
#         exit()
#     #continuer = input("Voulez-vous arrêter la partie ? (oui ou non) : ")
#     #if continuer == "oui":
#     #    print("Partie arrêtée ! Aucun gagnant")
#     #    exit()
#     #else :
#     coup = coupHumain(etat)
#     print(coup)
#     affiche(etat)
#     if estGagnant(etat, 4, "H", coup) == True:
#         print("Victoire de l'humain")
#         exit()
