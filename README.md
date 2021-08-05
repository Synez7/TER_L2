# TER_L2

Intitulé du projet : IA_Puissance4

Dates du projet : 20/01/2020 - 30/04/2020

Descrpition du projet réalisé :

Ce projet de programmation est consacré au développement d'une IA pour le jeu du " Connect 4 ", Puissance 4 en Anglais. 
L'algorithme d'exploration utilisé est le Minimax, celui-ci consiste à passer en revue tout le champ des possibles dans un arbre de recherche comme structure de données, pour un nombre limité de coups.

Brièvement, l'implémentation d'un tel algorithme a pour but de maximiser les chances d'une IA de remporter la victoire au cours d'une partie face à l'humain
via l'assignation d'un max et d'un min pour chaque état correspondant à la grille de jeu pour le Puissance 4.

Des tests ont été réalisés sur des grilles de différentes dimensions avec un nombre de pions à aligner défini. À partir de l'implémentation du minimax, la boucle
de jeu est effective pour une grille 3*3 et 4*4 avec un nombre de pions à aligner inférieur à 4.

Une autre approche a été étudiée, la méthode " Monte-Carlo ". Son implémentation n'a pas pu être faite mais l'idée était d'en apprendre davantage sur celle-ci et de la confronter avec le Minimax.
