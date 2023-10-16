## On récupère les valeurs d'entrée
# Le nom de la potion voulue
target = input()
# Les noms des potions disponibles en illimités
N = int(input()) # La quantité
unlimited = input().split(" ") # Les noms sont séparés par des espaces
# Les recettes, stockées dans un dictionnaire
# La clé serra le résultat, et les valeurs la paire de potions nécéssaires
recipes = {}
M = int(input()) # La quantité
for _ in range(M):
    A, B, C = input().split(" ") # Les trois noms sont séparés par des espaces
    recipes[A] = (B, C)

## On initialise
# Pour résoudre ce problème, nous allons partir de la fin et aller au début
# Nous allons considérer que la potion finale à été faite...
count = 1
crafted = [target]
impossible = False

## Exécution
# ... et nous allons défabriquer les potions jusqu'à ce qu'il ne reste plus rien
while len(crafted) != 0:
    A = crafted.pop() # On récupère un potion à défabriquer

    # Si la potion est disponible en quantité illimité,
    # pas la peine de la défabriquer
    if A in unlimited:
        continue

    # Si elle n'est ni en quantité illimité et que l'on ne peut pas la fabriquer,
    # alors la potion de base est impossible et on arrête de calculer
    if A not in recipes:
        impossible = True
        break
    
    # Sinon, on trouve la recette et on ajoute à la liste pour continuer
    b, c = recipes[A]
    crafted.append(b)
    crafted.append(c)
    count += 1

## On affiche le résultat
if impossible:
    print("impossible")
else:
    print(count)

## Améliorations possibles:
# - Ne pas calculer le coût d'une même fabrication plusieurs fois
# - Si la potion de base est déjà en quantité illimité, on ne la fabrique
#   même pas du tout (résultat de 0 et non de 1)
