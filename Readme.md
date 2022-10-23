<h1 align="center"> HLIN405 - TER_L2 </h1>
<h3 align="center"> Intitulé du projet : IA_Puissance4 </h3>
<h5 align="center"> Dates du projet : 20/01/2020 - 30/04/2020 </h5>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)


## Description du projet réalisé 

Ce projet de programmation est consacré au développement d'une IA pour le jeu du **Connect 4**, Puissance 4 en Anglais. 
L'algorithme d'exploration utilisé est le Minimax, celui-ci consiste à passer en revue tout le champ des possibles dans un arbre de recherche comme structure de données, pour un nombre limité de coups.

Brièvement, l'implémentation d'un tel algorithme a pour but de maximiser les chances d'une IA de remporter la victoire au cours d'une partie face à l'humain
via l'assignation d'un max et d'un min pour chaque état correspondant à la grille de jeu pour le Puissance 4.

Des tests ont été réalisés sur des grilles de différentes dimensions avec un nombre de pions à aligner défini. La boucle de jeu implémentée dans l'algorithme du Minimax est effective pour une grille `3 * 3` et `4 * 4` avec un nombre de pions à aligner inférieur à 4. Au delà d'une grille de dimension `4 * 4`, l'algorithme n'est pas optimisé.

Une autre approche a été étudiée, la méthode " Monte-Carlo ". Son implémentation n'a pas pu être faite mais l'idée était d'en apprendre davantage sur celle-ci et de la confronter avec le Minimax.

## Guide d'exécution 

Comment exécuter le programme "code_final_projet.py" ?

Depuis un terminal UNIX dans le dossier `TER_L2/`, effectuez les commandes ci-dessous:

```
chmod +x code_final_projet.py
python3 code_final_projet.py <ttt ou p4> <dimension> <nb pions à aligner>

```
# Remarque 
Pour la dimension, il faut saisir soit 3 soit 4 vu nos contraintes d'implémentation.
Il faut aussi penser à choisir un nombre de pions à aligner inférieur à 4 pour le bon fonctionnement du programme.
