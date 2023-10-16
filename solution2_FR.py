## On récupère le nombre de fantômes
N = int(input())

## On stock les coordonnées dans 2 listes
Xs = []
Ys = []
for _ in range(N):
    line = input()
    # Les deux coordonnées sont séparées par un espace
    x, y = line.split(" ")
    # On ajoute à la liste en pensant à convertir en nombre
    Xs.append(int(x))
    Ys.append(int(y))

## On récupère les positions des côtés
left = min(Xs)
right = max(Xs)
down = min(Ys)
up = max(Ys)

## On en déduit la taille
width = right - left + 1
height = up - down + 1
# Puisque le drap n'est pas rectangulaire mais carré,
# on garde uniquement le plus grand côté
size = max(width, height)
area = size * size

## On affiche le résultat
print(area)
