# Original not kept, re-created afterwards
coords = [tuple(int(component) for component in input().split()) for _ in range(int(input()))]
width = max(coord[0] for coord in coords) - min(coord[0] for coord in coords) + 1
height = max(coord[1] for coord in coords) - min(coord[1] for coord in coords) + 1
print(max(width, height) ** 2)