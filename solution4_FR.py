## On récupère les données
N = int(input()) # Le nombre le mots
words = []
for _ in range(N):
    word = input()
    words.append(word)

## On pré-calcule les mots suivants chaque autre mots
# Il s'agit juste ici d'un gain de temps, sinon l'ordinateur calcule 3000 fois
# la même chose pour peu d'efficacité.
# On utilise donc un dictionnaire avec pour chaque mots, une liste avec tous
# les mots suivants
next_words = {}
for word in words:
    # On définie une liste vide par défaut au cas où il n'y ait pas de suite
    if word not in next_words:
        next_words[word] = []
    size = len(word)

    # On itère sur le nombre de lettres du mot, dans l'ordre décroissant
    for i in range(size-1, -1, -1):
        start = word[:i] # Le début du mot
        next_word = word[:i+1] # Le début avec une lettre en plus

        # On ajoute ensuite le mot à la liste
        if start not in next_words:
            next_words[start] = []
        if next_word not in next_words[start]:
            next_words[start].append(next_word)

# Sous forme de fonction, la syntax serait plus simple:
def next_word_function(start):
    size = len(start) + 1 # La taille des mots suivants
    possibles = []
    for word in words:

        # Si le mot a le même début et la bonne taille, il pourra être utilisé
        if word.startswith(start) and len(word) >= size:
            # On ne veut que le début du mot
            truncated = word[:size]
            possibles.append(truncated)
    return possibles

## On écrit une fonction qui vérifie si le mot me fait gagner ou perdre
# Note: pour voir les étapes suivantes, on appelle cette fonction récursivement
def check(start, my_turn):
    next_turn = not my_turn

    if my_turn: # Je vais dire la lettre
        for word in next_words[start]:
            if check(word, next_turn):
                return True # La lettre me fait toujours gagner!!!
        return False # Aucune des lettres suivantes ne me fait gagner
    
    else: # La sorcière va dire la lettre
        for word in next_words[start]:
            if not check(word, next_turn):
                return False # La lettre lui permet de toujours gagner
        return True # Aucune des lettres suivantes ne la fait gagner!!!

# L'algorithm précédant est plus connu sous le nom de Minimax
# https://fr.wikipedia.org/wiki/Algorithme_minimax

## On récupère la liste des première lettres
letters = []
for word in words:
    letter = word[0]
    if letter not in letters:
        letters.append(letter)

## On calcule quelles lettres me font gagner
winners = []
for letter in letters:
    if check(letter, False):
        winners.append(letter)

## On affiche le résultat
if len(winners) == 0:
    print("impossible")
else:
    winners.sort() # On veut les résultats dans l'ordre alphabétique
    for letter in winners:
        print(letter)
