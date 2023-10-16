# Original not kept, re-created afterwards
target = input()
input()
available = input().split()
recipies_raw = [input() for _ in range(int(input()))]
recipes = {line.split()[0]: line.split()[1:] for line in recipies_raw}

count = 1
remaining = [target]
while remaining:
    result = remaining.pop()
    if result in available:
        continue
    if result not in recipes:
        print("impossible")
        exit()
    for ingredient in recipes[result]:
        remaining.append(ingredient)
    count += 1
print(count)