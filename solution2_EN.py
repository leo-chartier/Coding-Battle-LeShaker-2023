## We get the number of ghosts
N = int(input())

## We store the coordinates in 2 lists
Xs = []
Ys = []
for _ in range(N):
    line = input()
    # The coordinates are separated with a space
    x, y = line.split(" ")
    # We add to the list while converting to numbers
    Xs.append(int(x))
    Ys.append(int(y))

## We calculate the positions of the sides
left = min(Xs)
right = max(Xs)
down = min(Ys)
up = max(Ys)

## We deduce the size
width = right - left + 1
height = up - down + 1
# Since the sheet is not rectangulare but square,
# we only keep the largest side
size = max(width, height)
area = size * size

## We display the result
print(area)
