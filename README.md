# Why testing is important ?

## What is this repository for ?

L'objectif de ce repository est de démontrer l'importance des tests dans le développement d'un logiciel. Il a été créé dans le cadre du cours de Veille Technologique dans ma troisième année de BUT Informatique à l'université de La Rochelle. Ce repository contient un mini-projet de calculatrice réalisé en Python, capable d'effectuer des opérations de base (addition, soustraction, multiplication, division), et de les enregistrer dans une base de donnée locale. Le projet contient plusieurs branches, chacune représentant une couche de tests supplémentaire.

## How do I get set up ?

Ce mini-projet est réalisé en Python 3.10.12 mais il est possible de l'exécuter avec une version antérieure de Python 3. Pour lancer le projet, il suffit de cloner le repository et d'exécuter le fichier `main.py` avec la commande `python3 main.py`. Pour une expérience améliorée, vous pouver ajouer la police de caractère `Digital-7.ttf` à votre système. Vous devrez également avoir installer `sqlite3` pour pouvoir utiliser la base de données et `pytest` pour lancer les tests.

## Etape 0 : Une première version

Rendez-vous sur la branche `step-0-no-test` pour voir le code de la première version du projet. Cette version ne contient aucun test. Pourtant, elle fonctionne correctement, vous pouvez effectuer des opérations de base avec la calculatrice sans rencontrer de problèmes. On pourrait alors penser que les tests ne sont pas nécessaires.

## Etape 1 : Ajout d'une couche de tests unitaires

**Définition :** Ces tests se concentrent sur les plus petites unités de vos logiciels, c'est-à-dire vos méthodes et fonctions. Ils s'assurent que la sortie de vos méthode et fonction est celle attendu pour une entrée donnée.

Rendez-vous sur la branche `step-1-unit-test` pour voir le code de la deuxième version du projet. Cette version contient des tests unitaires pour les fonctions de la calculatrice. Ces tests permettent de vérifier que chaque fonction de la calculatrice fonctionne correctement.
Executez la commande `python3 -m pytest tests/` pour lancer les tests.

- Erreure reveler par les tests unitaires la division par zero n'est pas prise ne compte

```python
def divide(self, a, b):
    """Do the division."""
    return a / b
```

On peut modifier la fonction `divide` de la classe `Calculator` pour prendre en compte la division par zéro :
```python
def divide(self, a, b):
    """Do the division."""
    if b == 0:
        return "Syntax error"
    return a / b
```

## Etape 2 : Ajout d'une couche de tests d'intégration

**Définition :** Ces tests se concentrent sur les interactions entre les différentes unités de votre logiciel. Ils s'assurent que les différentes unités de votre logiciel fonctionnent correctement ensemble.

- Erreur reveler : les resultat sont converie en entier avant d'etre rentré dans la base de donnée dans l'appelle depuis app

```python
def get_result(self):
    """Calculate the result, display it and save it."""
    first_value = self.first_value_entry.get()
    operator = self.operator_entry.get()
    second_value = self.second_value_entry.get()
    self.calculator_logic.calcul[0] = first_value
    self.calculator_logic.calcul[1] = operator
    self.calculator_logic.calcul[2] = second_value
    result = self.calculator_logic.calculate_result()
    self.db_manager.save_calculation(first_value, operator, second_value, int(result)) #<----
    self.show_history()
    self.result_display.config(text=str(result))
```

On peut retirer la conversion en entier pour que les résultats soient enregistrés correctement dans la base de données :
```python
def get_result(self):
    """Calculate the result, display it and save it."""
    first_value = self.first_value_entry.get()
    operator = self.operator_entry.get()
    second_value = self.second_value_entry.get()
    self.calculator_logic.calcul[0] = first_value
    self.calculator_logic.calcul[1] = operator
    self.calculator_logic.calcul[2] = second_value
    result = self.calculator_logic.calculate_result()
    self.db_manager.save_calculation(first_value, operator, second_value, result) #<----
    self.show_history()
    self.result_display.config(text=str(result))
```




## Etape 3 : Ajout d'une couche de tests fonctionnels

**Définition :** Ces tests se concentrent sur les fonctionnalités de votre logiciel. Ils s'assurent que votre logiciel fonctionne correctement pour l'utilisateur final. Ils simulent le déroulement d'un scénario métier (souvent définit par les exigences métier ou fonctionnels), sans prêter attention aux états intermédiaire de l'application mais en vérifiant les résultats finaux.

- Erreur reveler : le contenu du label n'est pas un string mais on nombre, la conversion en string doit etre faite avant l'affichage

```python
def get_result(self):
    """Calculate the result, display it and save it."""
    first_value = self.first_value_entry.get()
    operator = self.operator_entry.get()
    second_value = self.second_value_entry.get()
    self.calculator_logic.calcul[0] = first_value
    self.calculator_logic.calcul[1] = operator
    self.calculator_logic.calcul[2] = second_value
    result = self.calculator_logic.calculate_result()
    self.db_manager.save_calculation(first_value, operator, second_value, result)
    self.show_history()
    self.result_display.config(text=result) #<----
```

On peut convertir le résultat en string avant de l'afficher :
```python
def get_result(self):
    """Calculate the result, display it and save it."""
    first_value = self.first_value_entry.get()
    operator = self.operator_entry.get()
    second_value = self.second_value_entry.get()
    self.calculator_logic.calcul[0] = first_value
    self.calculator_logic.calcul[1] = operator
    self.calculator_logic.calcul[2] = second_value
    result = self.calculator_logic.calculate_result()
    self.db_manager.save_calculation(first_value, operator, second_value, result)
    self.show_history()
    self.result_display.config(text=str(result)) #<----
```


## Etape 4 : Ajout d'une couche de tests de performance

**Définition :** Ces tests se concentrent sur les performances de votre logiciel. Ils s'assurent que votre logiciel fonctionne correctement en terme de temps d'exécution, de consommation de ressources, etc.

- Erreur reveler : - La multiplication fait des trucs de zinzin en temre de ressource mais sort le bon resultat

```python
def multiply(self, a, b):
    """Do the multiplication."""
    for i in range(100000):
        a * b + i
    return a * b
```

On peut retirer la boucle inutile pour améliorer les performances de la fonction `multiply` :
```python
def multiply(self, a, b):
    """Do the multiplication."""
    return a * b
```

## Etape 5 : Ajout d'une couche de tests exploratoires

- Erreur reveler : on peut rentrer des lettres et des signes dan sles mauvais champs dans la calculatrice 


# Reste a faire
- inclure les notion de test coverage
- finir l'ecriture de ce doc
- faire la mini-video de test exploratoire
- faire un ligne pip3 install avec tout les package necessaire