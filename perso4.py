N = int(input())
words = []
for _ in range(N):
    word = input()
    words.append(word)

# Post-battle note:
"""
I originally tried a recursive version of the min-max algorithm that reached
the limit (probably the function that calculates the next words on the fly
rather than pre-computing like what is done here).
So i tried to make an iterative version which required the algorithm to go
bottom-up and using a dictionary to act as a sort of stack for the different
states.
This version ended-up timing-out (as I feared) and with some testing, it turned
out that I tried too hard to use any() and all() and that the naive version
with a manual loop worked like a charm.
So much time wasted. ;(
The variable status is a remnant of the iterative attempt.
"""

nexts = {}
for word in words:
    if word not in nexts:
        nexts[word] = set()
    for i in range(len(word)):
        a, b = word[:i], word[:i+1]
        if a not in nexts:
            nexts[a] = set()
        nexts[a].add(b)
        
# status = {start: True for start in nexts}

def check(start):
    if len(start) % 2: # I said the letter
        for word in nexts[start]:
            if not check(word):
                return False
        return True
    else: # She said the letter
        for word in nexts[start]:
            if check(word):
                return True
        return False

finalists = [letter for letter in nexts if len(letter) == 1 and check(letter)]
if finalists:
    for letter in sorted(finalists):
        print(letter)
else:
    print("impossible")