N = int(input())

recipe_points = []

for _ in range(N):
    point = input().strip() 
    if 'лук' not in point.lower():  
        recipe_points.append(point)

output = ', '.join(recipe_points)

print(output)
