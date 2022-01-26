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
        nbPionsAlignes = 0
        j = 0
        while j < dim :
            if etat[ligne][j] == pion :
                nbPionsAlignes += 1
                if nbPionsAlignes == nbPions : return True
            else : nbPionsAlignes = 0 
            j += 1
    nbPionsAlignes = 0
    i = 0
    while i < dim :
        if etat[i][colonne] == pion :
            nbPionsAlignes += 1
            if nbPionsAlignes == nbPions : return True
        else : nbPionsAlignes = 0 
        i += 1
        
    nbPionsAlignes = 0
    lignetest = ligne
    colonnetest = colonne
    while lignetest > 0 and colonnetest > 0 :
        lignetest -= 1
        colonnetest -= 1
    while lignetest < dim and colonnetest < dim :
        if etat[lignetest][colonnetest] == pion :
            nbPionsAlignes += 1
            if nbPionsAlignes == nbPions : return True
        else : nbPionsAlignes = 0 
        lignetest += 1
        colonnetest += 1
        
    nbPionsAlignes = 0
    lignetest = ligne
    colonnetest = colonne
    while lignetest < dim-1 and colonnetest > 0 :
        lignetest += 1
        colonnetest -= 1
    while lignetest >= 0 and colonnetest < dim :
        if etat[lignetest][colonnetest] == pion :
            nbPionsAlignes += 1
            if nbPionsAlignes == nbPions : return True
        else : nbPionsAlignes = 0 
        lignetest -= 1
        colonnetest += 1

    
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
        if joueur == "IA" : etat[coup[0]][coup[1]] = 1
        else : etat[coup[0]][coup[1]] = 2
        if estGagnant(etat, nbPions, joueur, coup) == True :
            if joueur == "IA" :
                scores.append(1)
                etat[coup[0]][coup[1]] = 0
                break                    
            else :
                scores.append(-1)
                etat[coup[0]][coup[1]] = 0
                break                   
        else :
            if nbCoupsPossibles == 1 :
                scores.append(0) 
            else :
                scores.append(explore(etat, nbPions, profondeur+1, autreJoueur))
        etat[coup[0]][coup[1]] = 0
        numCoup += 1
    if joueur == "H" :
        numCoup = min(scores)
        if profondeur == 0 :  
            return coupsPossibles[numCoup]
        return scores[numCoup]
    if joueur == "IA" :
        numCoup = max(scores)
        if profondeur == 0 :  
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

# Boucle de jeu
while True :
    
    print("L'IA réfléchit...")
    meilleurCoup = explore(etat, nbPions, 0, "IA")
    etat[meilleurCoup[0]][meilleurCoup[1]] = 1
    affiche(etat)
    if estGagnant(etat, nbPions, "IA", meilleurCoup) == True :
        print("Victoire de l'IA")
        exit()
    if possibles(etat) == [] :
        print("Grille pleine et aucun gagnant !")
        exit()
    coupH = coupHumain(etat, typeJeu)
    affiche(etat)
    if estGagnant(etat, nbPions, "H", coupH) == True:
        print("Victoire de l'humain")
        exit()             

