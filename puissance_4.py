import sys
import pygame
import math
import random





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
            return
        print("Coup impossible !")



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
        if estGagnant(etat, 3, joueur) == True :
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
# print(explore(([[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),3,1,"IA"))

# if len(sys.argv) != 3 :
#     print("Usage : puissance4 <dimension> <nb pions à aligner>")
#     exit()
# if not sys.argv[1].isdigit() or not sys.argv[2].isdigit() : 
#     print("La dimension et le nombre des pions doivent être des entiers")
#     exit()


    
# dimension = int(sys.argv[1])
# nbPions = int(sys.argv[2])

m = 6
n = 7
etat = []
for i in range(0,m) :
    etat.append([])
    for j in range(0,n) :
        etat[i].append(0)
# print(etat)

#####################  INTERFACE GRAPHIQUE  #####################

taille_case = 100                     ## Taille en pixels d'une case de la grille de jeu
rayon_cercle = int(taille_case/2 - 4) ## Rayon du cercle 
cadre = (0, 0, 255)                   ## Cadre bleue de la grille de jeu
blanc = (255, 255, 255)               ## Case initialement non remplie
jeton_rouge = (255, 0, 0)             ## Jeton utilisé par l'utilisateur
jeton_jaune = (255, 255, 0)           ## Jeton utilisé par l'IA
pion_joueur = 2                       ## pion utilisé par l'utilisateur
pion_IA = 1                           ## pion utilisé par l'IA

humain = 0                            ## Variables 'humain' et 'IA' utilisées pour définir les tours de jeu
IA = 1


largeur = len(etat[0]) * taille_case         ## Dimensions de la grille de jeu
hauteur = (len(etat) + 1) * taille_case


pygame.init()



def inserer_jeton(etat,i,j,pion):          ## Fonction permettant l'insertion d'un jeton de joueur (Utilisateur / IA)
    if i < len(etat) and j < len(etat[0]): ## etat : grille de jeu , i : abscisse du jeton inséré
        etat[i][j] = pion                  ## j : ordonnée du jeton inséré , pion : 1 ou 2

def emplacementValide(etat,colonne):     ## Fonction vérifiant  si une case de la grille de jeu est inoccupée avant l'inserion d'un jeton de joueur
    if etat[len(etat)-1][colonne] == 0:  ## Le jeton inséré doit occuper la position la plus basse sur une colonne (gravité)
        return True                      ## colonne : ordonnée de la case donnée
    else:
        return False


def rangeeSuivante(etat, colonne):   ## Fonction recherchant une ligne non occupée de la grille de jeu
    for ligne in range(len(etat)):   
        if etat[ligne][colonne] == 0:
            return ligne



def grilleApparition(etat):
    for colonne in range(len(etat[0])):
        for ligne in range(len(etat)):
            ## Construction des emplacements pour l'insertion des jetons
            pygame.draw.rect(grille, cadre, (colonne*taille_case, (ligne+1)* taille_case, taille_case, taille_case))
            pygame.draw.circle(grille, blanc, (int(colonne*taille_case + taille_case/2), int((ligne+1)*taille_case + taille_case/2)), rayon_cercle)
    
    for colonne in range(len(etat[0])):
        for ligne in range(len(etat)):
            # Si c'est au tour de l'humain d'insérer un jeton, création d'un jeton rouge à insérer dans la case souhaitée
            if etat[ligne][colonne] == pion_joueur:
                pygame.draw.circle(grille, jeton_rouge, (int(colonne*taille_case + taille_case/2), hauteur-int((ligne)*taille_case + taille_case/2)), rayon_cercle)
            # Si c'est au tour de l'IA d'insérer un jeton, création d'un jeton jaune à insérer dans la case souhaitée
            elif etat[ligne][colonne] == pion_IA:
                pygame.draw.circle(grille, jeton_jaune, (int(colonne*taille_case + taille_case/2), hauteur-int((ligne)*taille_case + taille_case/2)), rayon_cercle)
    # Mise à jour de la grille de jeu
    pygame.display.update()

largeur = len(etat[0]) * taille_case         
hauteur = len(etat) * taille_case
grille = pygame.display.set_mode((600, 400))
etat = [[0,0,0],[0,0,0],[0,0,0]]
print(grilleApparition(etat))


def jeu():
    etat = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]] ## Grille de jeu 6 * 7
    fin_partie = False
   
    
    myfont = pygame.font.SysFont("comicsansms", 40) ## Police d'écriture utilisée pour l'affichage du gagnant de la partie / égalité
    
    tour = random.randint(humain,IA)    ## Gestion des tours de jeu 


    while not fin_partie and len(possibles(etat)) != 0:  
        
        for event in pygame.event.get():
            ## Si clic sur la croix de la fenêtre d'affichage, celle-ci se ferme
            if event.type == pygame.QUIT: 
                sys.exit()

            if event.type == pygame.MOUSEMOTION: ## Mouvement du curseur
                pygame.draw.rect(grille, blanc, (0,0, largeur, taille_case)) ## Bande horizontale blanche au-dessus de la grille de jeu
                posx = pygame.mouse.get_pos()[0]  ## Récupération des coordonnées de position (x;y) du curseur de la souris
                if tour == humain:  ## Si c'est au tour de l'humain de jouer, celui-ci va devoir insérer un jeton rouge dans la case désirée
                    pygame.draw.circle(grille, jeton_rouge, (posx, int(taille_case/2)), rayon_cercle)
                else:  ## Jeton jaune dans le cas où c'est à l'IA de commencer la partie
                    pygame.draw.circle(grille, jeton_jaune, (posx, int(taille_case/2)), rayon_cercle)


            pygame.display.update()  ## Actualisation de la fenêtre d'affichage


            if event.type == pygame.MOUSEBUTTONDOWN:  ## Evenement : clic gauche de la souris sur un emplacement inoccupée de la grille de jeu
                pygame.draw.rect(grille, blanc, (0,0, largeur,taille_case))
           
                if tour == humain:
                    posx = pygame.mouse.get_pos()[0]   ## Position en abscisse du curseur par rapport à la fenêtre d'affichage     
                    col = posx // taille_case          ## Position en ordonnée du curseur par rapport à la fenêtre d'affichage
               
                    if emplacementValide(etat, col):
                        ligne = rangeeSuivante(etat, col)  ## Insertion du jeton de l'utilisateur dans le cas où la situation est favorable
                        inserer_jeton(etat, ligne, col, 2)

                        if estGagnant(etat,3,"H"):     ## Si l'utilisateur remporte la partie, un message s'affiche en haut de la grille
                            label = myfont.render("Victoire de l'humain !", 1, jeton_rouge)
                            grille.blit(label, (40,10))
                            fin_partie = True

                        tour += 1         ## Incrémentation des tours pour permettre aux joueurs de jouer l'un après l'autre
                        tour = tour % 2

                        ## Mise à jour de la grille de jeu après plusieurs insertions de jetons
                        grilleApparition(etat)
                        affiche(etat)

            if tour == IA and not fin_partie:
                longueur = len(possibles(etat))
                coup = possibles(etat)[longueur // 2] ## Jeton placé sur la 4e colonne de la grille 
                colonne = coup[1]              

                if emplacementValide(etat, colonne):
                    ligne = rangeeSuivante(etat, colonne)
                    inserer_jeton(etat, ligne, colonne, 1)

                    if estGagnant(etat, 4, "IA"):
                        ## Si l'IA remporte la partie, un message s'affiche en haut de la grille
                        label = myfont.render("Victoire de l'IA !", 1, jeton_jaune) 
                        grille.blit(label, (40, 10))
                        fin_partie = True

                   
                    

                    tour += 1
                    tour = tour % 2

                    grilleApparition(etat)
                    affiche(etat)

            if(possibles(etat) == [] and not (estGagnant(etat, 4, "IA") == True) and not (estGagnant(etat, 4, "H") == True)):
                ## Message affiché sur la bande horizontale blanche, dans le cas d'une saturation de la grille 
                label = myfont.render("MATCH NUL", 1, (0,0,255)) 
                grille.blit(label, (40, 10))
                pygame.time.wait(3000)

            if fin_partie:
                pygame.time.wait(3000) 
                ## La fenêtre d'affichage se ferme 3000 ms après que la partie soit terminée


jeu()





# while True :
    
#     print("L'IA réfléchit...")
#     meilleurCoup = explore(etat, nbPions, 0, "IA")
#     etat[meilleurCoup[0]][meilleurCoup[1]] = 1
#     affiche(etat)
#     if estGagnant(etat, 3, "IA") == True :
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

