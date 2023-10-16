## Le nombre de personnes dans la famille
N = 5

## On récupère les âges dans un liste
ages = []
for _ in range(N):
    # On oublie pas le int() pour transformer le texte en nombre
    age = int(input())
    ages.append(age) # On ajoute l'âge à la liste

## On compte combient de personnes ont 15 ans ou plus
count = 0
for age in ages:
    if age >= 15:
        count += 1 # On augmente de 1

## On affiche le résultat
print(count)
