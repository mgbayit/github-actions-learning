# 1. On importe le framework de test (optionnel ici, mais bonne pratique)
import pytest

# 2. Fonction de test pour l'addition
def test_calc_addition():
    output = 2 + 4
    assert output == 6  # On vérifie que 2 + 4 donne bien 6

# 3. Fonction de test pour la soustraction
def test_calc_substraction():
    output = 2 - 4
    assert output == -2  # On vérifie que 2 - 4 donne bien -2

# 4. Fonction de test pour la multiplication
def test_calc_multiply():
    output = 2 * 4
    assert output == 8   # On vérifie que 2 * 4 donne bien 8

# 5. Fonction de test pour une chaîne de caractères
def test_coucou():
    output = 'hello'
    assert output == 'hello'  # On vérifie que la variable contient bien 'hello'