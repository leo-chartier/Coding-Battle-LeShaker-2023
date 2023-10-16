## We get the input values
# The name of the target potion
target = input()
# The names of the potions available unlimitedly
N = int(input()) # The amount
unlimited = input().split(" ") # The names are separated with spaces
# The recipies, stored in a dictionary
# The key is the result and the values are the pairs of the necessary potions
recipes = {}
M = int(input()) # The amount
for _ in range(M):
    A, B, C = input().split(" ") # The three names are separated with spaces
    recipes[A] = (B, C)

## We initialize
# To solve this problem, we will start at the end and go towards the beginning
# We will consider that the target potion has been crafted...
count = 1
crafted = [target]
impossible = False

## Execution
# ... and we will decraft the potions until there is nothing left
while len(crafted) != 0:
    A = crafted.pop() # We get a potion to decraft

    # If the potion is in unlimited supplies, no need to decraft it
    if A in unlimited:
        continue

    # If it is neither unlimited, neither craftable, then the target potion is
    # impossible and we stop calculating
    if A not in recipes:
        impossible = True
        break
    
    # Otherwise, we find the recipe and add it to the list to continue
    b, c = recipes[A]
    crafted.append(b)
    crafted.append(c)
    count += 1

## We show the result
if impossible:
    print("impossible")
else:
    print(count)

## Possible improvements:
# - Do not calculate the cost of a same craft multiple times
# - If the target potion is already in illimited amount, no need to craft it
#   at all (result of 0, not 1)
