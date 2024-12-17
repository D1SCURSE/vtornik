def max_treasure_points(points):
    from collections import defaultdict

    n = len(points)
    graph = defaultdict(list)
    
    last_digit_map = defaultdict(list)
    
    for i in range(n):
        x, y = points[i]
        last_digit_map[(x % 10, y % 10)].append(i)
    
    for (x_last, y_last), indices in last_digit_map.items():
        for i in indices:
            for j in indices:
                if i != j:
                    graph[i].append(j)

    def dfs(node, visited):
        visited.add(node)
        max_length = 1 
        for neighbor in graph[node]:
            if neighbor not in visited:
                max_length = max(max_length, 1 + dfs(neighbor, visited))
        visited.remove(node)
        return max_length

    max_points = 1
    for i in range(n):
        max_points = max(max_points, dfs(i, set()))

    return max_points

N = int(input().strip())
points = [tuple(map(int, input().strip().split())) for _ in range(N)]
result = max_treasure_points(points)
print(result)
