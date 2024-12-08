# Why testing is important ?

## What is this repository for ?

L'objectif de ce repository est de démontrer l'importance des tests dans le développement d'un logiciel. Il a été créé dans le cadre du cours de Veille Technologique dans ma troisième année de BUT Informatique à l'université de La Rochelle. Ce repository contient un mini-projet de calculatrice réalisé en Python, capable d'effectuer des opérations de base (addition, soustraction, multiplication, division), et de les enregistrer dans une base de donnée locale. Le projet contient plusieurs branches, chacune représentant une couche de tests supplémentaire.

## How do I get set up ?

Ce mini-projet est réalisé en Python 3.10.12 mais il est possible de l'exécuter avec une version antérieure de Python 3. Pour lancer le projet, il suffit de cloner le repository et d'exécuter le fichier `main.py` avec la commande `python3 main.py`. Pour une expérience améliorée, vous pouver ajouter la police de caractère `Digital-7.ttf` à votre système. Vous devrez également avoir installer `sqlite3` pour pouvoir utiliser la base de données et `pytest` pour lancer les tests.

## Etape 0 : Une première version

Rendez-vous sur la branche `step-0-no-test` pour voir le code de la première version du projet. Cette version ne contient aucun test. Pourtant, elle fonctionne correctement, vous pouvez effectuer des opérations de base avec la calculatrice sans rencontrer de problèmes. On pourrait alors penser que les tests ne sont pas nécessaires.

## Etape 1 : Ajout d'une couche de tests unitaires

**Définition :** Ces tests se concentrent sur les plus petites unités de vos logiciels, c'est-à-dire vos méthodes et fonctions. Ils s'assurent que la sortie de vos méthode et fonction est celle attendu pour une entrée donnée.

Rendez-vous sur la branche `step-1-unit-test` pour voir le code de la deuxième version du projet. Cette version contient des tests unitaires pour les fonctions de la calculatrice. Ces tests permettent de vérifier que chaque fonction de la calculatrice fonctionne correctement.
Executez la commande `python3 -m pytest --cov=calculator --cov-report=html --cov-report=term` pour lancer les tests.

On obtient le résultat suivant :
```
---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                            Stmts   Miss  Cover
---------------------------------------------------
calculator/CalculatorApp.py       105    105     0%
calculator/CalculatorLogic.py      39      1    97%
calculator/DatabaseManager.py      28      0   100%
---------------------------------------------------
TOTAL                             172    106    38%
Coverage HTML written to dir htmlcov

======short test summary info ======
FAILED tests/UnitTests/test_CalculatorLogic.py::test_division_by_zero - ZeroDivisionError: division by zero
FAILED tests/UnitTests/test_CalculatorLogic.py::test_calcul_division_by_zero - ZeroDivisionError: float division by zero
======2 failed, 22 passed in 0.39s =====
```
On voit que deux tests ont échoué. Ces tests ont permis de révéler des erreurs dans le code de la fonction `divide` de la classe `Calculator`. En effet, en regardant le code source, on voit que la division par zéro n'est pas prise en compte.
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

On peut maintenant relancer les tests pour vérifier que les erreurs ont été corrigées.
```
---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                            Stmts   Miss  Cover
---------------------------------------------------
calculator/CalculatorApp.py       105    105     0%
calculator/CalculatorLogic.py      41      1    98%
calculator/DatabaseManager.py      28      0   100%
---------------------------------------------------
TOTAL                             174    106    39%
Coverage HTML written to dir htmlcov


==== 24 passed in 0.24s ====
```

On voit que les tests passent tous, ils ont permis de révéler des erreurs dans le code et de les corriger. On voit également que la couverture des tests est de n'est que de 39%. Il reste donc des parties du code qui ne sont pas testées. Il faudra ajouter des tests pour ces parties du code.

## Etape 2 : Ajout d'une couche de tests d'intégration

**Définition :** Ces tests se concentrent sur les interactions entre les différentes unités de votre logiciel. Ils s'assurent que les différentes unités de votre logiciel fonctionnent correctement ensemble.

Rendez-vous sur la branche `step-2-integration-test` pour voir le code de la troisième version du projet. Cette version contient des tests d'intégration portant sur les interactions entre les différentes classes de la calculatrice. Ces tests permettent de vérifier que les différentes classes de la calculatrice fonctionnent correctement ensemble.
Executez la commande `python3 -m pytest --cov=calculator --cov-report=html --cov-report=term` pour lancer les tests.

On obtient le résultat suivant :
```
---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                            Stmts   Miss  Cover
---------------------------------------------------
calculator/CalculatorApp.py       105      7    93%
calculator/CalculatorLogic.py      41      1    98%
calculator/DatabaseManager.py      28      0   100%
---------------------------------------------------
TOTAL                             174      8    95%
Coverage HTML written to dir htmlcov

====short test summary info ====
FAILED tests/IntegrationTests/test_integration.py::test_calculation_integration - AssertionError: The result should be '9.2' in the database.
==== 1 failed, 27 passed in 0.91s ====
```
On voit que un test a échoué. Ce test a permis de révéler une erreur dans le code de la fonction `get_result` de la classe `CalculatorApp`. En effet, en regardant le code source, on voit que les résultats sont convertis en entier avant d'être enregistrés dans la base de données.
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

On peut maintenant relancer les tests pour vérifier que les erreurs ont été corrigées.
```
---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                            Stmts   Miss  Cover
---------------------------------------------------
calculator/CalculatorApp.py       105      7    93%
calculator/CalculatorLogic.py      41      1    98%
calculator/DatabaseManager.py      28      0   100%
---------------------------------------------------
TOTAL                             174      8    95%
Coverage HTML written to dir htmlcov


===== 28 passed in 0.86s ======
```
On voit que les tests passent tous, ils ont permis de révéler des erreurs dans le code et de les corriger. On voit également que la couverture des tests est de 95%. C'est mieux mais il reste encore des parties du code qui ne sont pas testées. Il faudra ajouter des tests pour ces parties du code.


## Etape 3 : Ajout d'une couche de tests fonctionnels

**Définition :** Ces tests se concentrent sur les fonctionnalités de votre logiciel. Ils s'assurent que votre logiciel fonctionne correctement pour l'utilisateur final. Ils simulent le déroulement d'un scénario métier (souvent définit par les exigences métier ou fonctionnels), sans prêter attention aux états intermédiaire de l'application mais en vérifiant les résultats finaux.

Rendez-vous sur la branche `step-3-functional-test` pour voir le code de la quatrième version du projet `git branch step-3-functional-test`. Cette version contient des tests fonctionnels portant sur les fonctionnalités de la calculatrice. Ces tests permettent de vérifier que la calculatrice fonctionne correctement pour l'utilisateur final.
Executez la commande `python3 -m pytest --cov=calculator --cov-report=html --cov-report=term` pour lancer les tests.

On obtient le résultat suivant :
```
---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                            Stmts   Miss  Cover
---------------------------------------------------
calculator/CalculatorApp.py       105      2    98%
calculator/CalculatorLogic.py      41      1    98%
calculator/DatabaseManager.py      28      0   100%
---------------------------------------------------
TOTAL                             174      3    98%
Coverage HTML written to dir htmlcov

===== short test summary info =====
FAILED tests/FonctionalTests/test_functional.py::test_calculate_result - AssertionError: assert 3.0 == '3.0'
===== 1 failed, 34 passed in 3.63s ======
```
On voit que un test a échoué. Ce test a permis de révéler une erreur dans le code de la fonction `get_result` de la classe `CalculatorApp`. En effet, en regardant le code source, on voit que le contenu du label n'est pas converti en string avant d'être affiché.
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

On peut maintenant relancer les tests pour vérifier que les erreurs ont été corrigées.
```
---------- coverage: platform linux, python 3.10.12-final-0 ----------
Name                            Stmts   Miss  Cover
---------------------------------------------------
calculator/CalculatorApp.py       105      2    98%
calculator/CalculatorLogic.py      41      1    98%
calculator/DatabaseManager.py      28      0   100%
---------------------------------------------------
TOTAL                             174      3    98%
Coverage HTML written to dir htmlcov


==== 35 passed in 3.55s ======
```
On voit que les tests passent tous, ils ont permis de révéler des erreurs dans le code et de les corriger. On voit également que la couverture des tests est de 98%. C'est un trés bon score, on peut considérer que cette couverture est suffisante pour ce projet, les prochains tests que nous allons ajouter seront plus orienté performance.


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