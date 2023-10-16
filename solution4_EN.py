## We get the data
N = int(input()) # The number of words
words = []
for _ in range(N):
    word = input()
    words.append(word)

## We pre-calculate the nexts words following other words
# It simply a gain of time, otherwise the computer does the same calculation
# 3000 times with no efficiency.
# On utilise donc un dictionnaire avec pour chaque mots, une liste avec tous
# We use a dictionary with, for each word, a list with all the next words.
next_words = {}
for word in words:
    # We define an empty list by default in case there is no follow-up
    if word not in next_words:
        next_words[word] = []
    size = len(word)

    # We iterate on the number of letters of the word, in decreasing order
    for i in range(size-1, -1, -1):
        start = word[:i] # The beginning of the word
        next_word = word[:i+1] # The beginning with an extra letter

        # We then add the word to the list
        if start not in next_words:
            next_words[start] = []
        if next_word not in next_words[start]:
            next_words[start].append(next_word)

# As a function, the syntax would be much simpler:
def next_word_function(start):
    size = len(start) + 1 # The size of the next words
    possibles = []
    for word in words:

        # If the word has the same start and the right size, it could be used
        if word.startswith(start) and len(word) >= size:
            # We only want the beginning of the word
            truncated = word[:size]
            possibles.append(truncated)
    return possibles

## We write a function that checks if the words lets us win of lose
# Note: to check the next steps, we recursivly call the function
def check(start, my_turn):
    next_turn = not my_turn

    if my_turn: # I will say the letter
        for word in next_words[start]:
            if check(word, next_turn):
                return True # I always win with this letter!!!
        return False # None of the next letters allows me to win
    
    else: # The witch will say the letter
        for word in next_words[start]:
            if not check(word, next_turn):
                return False # She always win with this letter
        return True # None of the next letters allows her to win!!!

# The preceding algorithm is more commonly known as Minimax
# https://en.wikipedia.org/wiki/Minimax

## We get the list of all the first letters
letters = []
for word in words:
    letter = word[0]
    if letter not in letters:
        letters.append(letter)

## We calculate which ones allows me to win
winners = []
for letter in letters:
    if check(letter, False):
        winners.append(letter)

## We display the result
if len(winners) == 0:
    print("impossible")
else:
    winners.sort() # We want the results in alphabetical order
    for letter in winners:
        print(letter)
