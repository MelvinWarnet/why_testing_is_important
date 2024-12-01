# Why testing is important ?

## What is this repository for ?

L'objectif de ce repository est de démontrer l'importance des tests dans le développement d'un logiciel. Il a été créé dans le cadre du cours de Veille Technologique dans ma troisième année de BUT Informatique à l'université de La Rochelle. Ce repository contient un mini-projet de calculatrice réalisé en Python, capable d'effectuer des opérations de base (addition, soustraction, multiplication, division), et de les enregistrer dans une base de donnée. Le projet contient plusieurs branches, chacune représentant une couche de tests supplémentaire.

## How do I get set up ?

Ce mini-projet est réalisé en Python 3.10.12 mais il est possible de l'exécuter avec une version antérieure de Python 3. Pour lancer le projet, il suffit de cloner le repository et d'exécuter le fichier `main.py` avec la commande `python3 main.py`. Pour une expérience améliorée, vous pouver ajouer la police de caractère `Digital-7.ttf` à votre système. Vous devrez également avoir installer `sqlite3` pour pouvoir utiliser la base de données et `pytest` pour lancer les tests.

## Etape 0 : Une première version

Rendez-vous sur la branche `step-0-no-test` pour voir le code de la première version du projet. Cette version ne contient aucun test. Pourtant, elle fonctionne correctement, vous pouvez effectuer des opérations de base avec la calculatrice sans rencontrer de problèmes. On pourrait alors penser que les tests ne sont pas nécessaires.

## Etape 1 : Ajout d'une couche de tests unitaires

**Définition :** Ces tests se concentrent sur les plus petites unités de vos logiciels, c'est-à-dire vos méthodes et fonctions. Ils s'assurent que la sortie de vos méthode et fonction est celle attendu pour une entrée donnée.

Rendez-vous sur la branche `step-1-unit-test` pour voir le code de la deuxième version du projet. Cette version contient des tests unitaires pour les fonctions de la calculatrice. Ces tests permettent de vérifier que chaque fonction de la calculatrice fonctionne correctement.
Executez la commande `python3 -m unittest` pour lancer les tests.

- Erreure reveler par les tests unitaires la division par zero n'est pas prise ne compte

## Etape 2 : Ajout d'une couche de tests d'intégration

**Définition :** Ces tests se concentrent sur les interactions entre les différentes unités de votre logiciel. Ils s'assurent que les différentes unités de votre logiciel fonctionnent correctement ensemble.

- Erreur reveler :

## Etape 3 : Ajout d'une couche de tests fonctionnels




## Etape 4 : Ajout d'une couche de tests de performance

- Erreur reveler : - La multiplication 

## Etape 5 : Ajout d'une couche de tests exploratoires

