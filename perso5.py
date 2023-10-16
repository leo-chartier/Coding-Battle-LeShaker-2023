# First and only attempt.
# Didn't have time to do more. This solution times-out.

R2 = int(input()) ** 2
N = int(input())
coords = [tuple(int(x) for x in input().split(" ")) for _ in range(N)]

from itertools import combinations

M = 0
for n in range(1, N+1):
    for combi in combinations(coords, n):
        sx = 0
        sy = 0
        for x, y in combi:
            sx += x
            sy += y
        cx = sx / n
        cy = sy / n
        c = sum((x-cx)*(x-cx) + (y-cy)+(y-cy) <= R2 for x, y in coords)
        M = max(M, c)
print(M)
