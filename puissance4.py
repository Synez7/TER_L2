import sys
import pygame
import math
import random

taille_case = 100
rayon_cercle = int(taille_case/2 - 4)
grille = (0, 0, 255)
blanc = (255, 255, 255)
jeton_rouge = (255, 0, 0)
jeton_jaune = (255, 255, 0)
humain = 0
IA = 1

case_vide = 0
jeton_humain = 1
jeton_IA = 2

pygame.init()
msg_font = pygame.font.SysFont("comicsansms", 40)


def inserer_jeton(etat,i,j,pion):
    etat[i][j] = pion



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
    dim = len(etat)    
    while True :
        abs = input("Ligne (entre 0 et "+str(dim-1)+") ? ")
        ord = input("Colonne (entre 0 et "+str(dim-1)+") ? ")
        if abs.isdigit() and int(abs) >= 0 and int(abs) < dim and ord.isdigit() and int(ord) >= 0 and int(ord) < dim and etat[int(abs)][int(ord)] == 0  and gravite(etat, int(abs), int(ord)) :
            etat[int(abs)][int(ord)] = 2
            retour
        print("Coup impossible !")


###### ALI


def extraction_diag(etat):   ## Retourne un tuple de 2 sous-liste contenant les diagonales avant " \ " et les diagonales arrière " / "
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

        ###    Vérification  de l'alignement de nbPions à partir des diagonales avant " \ " ###
        ################################################################################

    for d in diagonales_avant:
        nbPionsAlignes = 0  ## Parcours de la liste contenant les diagonales avant
        for case in d:
            #if case == 0:   ## Vérification de la case si celle-ci est égale à 0 , on parcourt la case suivante [0,0,1,0] 
            #    nbPionsAlignes = 0
            if case == pion:
                nbPionsAlignes += 1 ## Trou rencontré en la présence d'un pion adverse
            else:
                nbPionsAlignes = 0  
            
            if nbPionsAlignes == nbPions :
                return True

        ###    Vérification  de l'alignement de nbPions à partir des diagonales arrières " / " ###
           ##################################################################################

    for d in diagonales_arriere:
        nbPionsAlignes = 0   ## Parcours de la liste contenant les diagonales avant
        for case in d:
            #if case == 0:
            #    nbPionsAlignes = 0
            if case == pion:
                nbPionsAlignes += 1
            else:
                nbPionsAlignes = 0

            if nbPionsAlignes == nbPions:
                return True

    return False                          ## Cas où aucune combinaison gagnante est satisfaite au cours de la partie jouée



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
        if estGagnant(etat, 4, joueur) == True :
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

if len(sys.argv) != 3 :
    print("Usage : puissance4 <dimension> <nb pions à aligner>")
    exit()
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit() : 
    print("La dimension et le nombre des pions doivent être des entiers")
    exit()

# if(int(sys.argv[2]) > (int(sys.argv[1]))):
#     print("Le nombre de pions à aligner doit être <= à la dimension de la grille \n")
#     exit()

        
dimension = int(sys.argv[1])
nbPions = int(sys.argv[2])
etat = [[] for i in range(0, dimension)]
for i in range(0, dimension) :
    for j in range(0, dimension) :
        etat[i].append(0)

print(etat)


############ABDELLAH

def grilleApparition(etat):
    for colonne in range(len(etat[0])):
        for ligne in range(len(etat)):
            pygame.draw.rect(fenetre, grille, (colonne*taille_case, (ligne+1)* taille_case, taille_case, taille_case))
            pygame.draw.circle(fenetre, blanc, (int(colonne*taille_case + taille_case/2), int((ligne+1)*taille_case + taille_case/2)), rayon_cercle)
    
    for colonne in range(len(etat[0])):
        for ligne in range(len(etat)):
            if etat[ligne][colonne] == jeton_humain:
                pygame.draw.circle(fenetre, jeton_rouge, (int(colonne*taille_case + taille_case/2), hauteur-int((ligne)*taille_case + taille_case/2)), rayon_cercle)
            elif etat[ligne][colonne] == jeton_IA:
                pygame.draw.circle(fenetre, jeton_jaune, (int(colonne*taille_case + taille_case/2), hauteur-int((ligne)*taille_case + taille_case/2)), rayon_cercle)
    pygame.display.update()

largeur = len(etat[0]) * taille_case
hauteur = (len(etat) + 1) * taille_case
fenetre = pygame.display.set_mode((largeur, hauteur))
fin_partie = False
pygame.display.update()
grilleApparition(etat)

tour = random.randint(humain,IA)

while not fin_partie:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(fenetre, blanc, (0,0, largeur, taille_case))
            posx = event.pos[0]
            if tour == humain:
                pygame.draw.circle(fenetre, jeton_rouge, (posx, int(taille_case/2)), rayon_cercle)
            else:
                pygame.draw.circle(fenetre, jeton_jaune, (posx, int(taille_case/2)), rayon)


        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(fenetre, blanc, (0,0, largeur, taille_case))
           
            if tour == HUMAIN:
                posx = event.pos[0]
                col = int(math.floor(posx/taille_case))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    isnert_token(board, row, col, 2)

                    if isWinner(board,4,"H"):
                        label = myfont.render("Victoiry of human !", 1, red)
                        fenetre.blit(label, (40,10))
                        end_game = True

                    tour += 1
                    tour = tour % 2

                    print_board(board)
                    gridApparition(board)


  
    if tour == IA and not end_game:
        posx = event.pos[0]
        column = random.choice(len(etat[0]))
        col = int(math.floor(posx/taille_case))

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            isnert_token(board, row, col, 1)

            if isWinner(board,4,"IA"):
                label = myfont.render("Victory of AI !", 1, jeton_jaune)
                fenetre.blit(label, (40,10))
                end_game = True

            print_board(board)
            gridApparition(board)

            tour += 1
            tour = tour % 2

    if possible_moves(board) == [] and not(isWinner(board, 4, "IA") == True) and not(isWinner(board, 4, "H") == True): 
        label = myfont.render("A DRAW", 1, blanc)
        fenetre.blit(label, (40,10))
        exit()
  

    if end_game:
        pygame.time.wait(3000)
























# while True :
    
#     print("L'IA réfléchit...")
#     meilleurCoup = explore(etat, nbPions, 0, "IA")
#     etat[meilleurCoup[0]][meilleurCoup[1]] = 1
#     affiche(etat)
#     if estGagnant(etat, nbPions, "IA") == True :
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
#     coupHumain(etat)
#     affiche(etat)
#     if estGagnant(etat, 3, "H") == True:
#         print("Victoire de l'humain")
#         exit()             

