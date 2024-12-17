def main():
    import sys
    
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    n = int(data[0])
    bacteria = []
    
    for i in range(1, n * n + 1):
        bacteria.append(int(data[i]))
    
    grid = [bacteria[i * n:(i + 1) * n] for i in range(n)]
    
    k = int(data[n * n + 1])
    
    drops = []
    for i in range(n * n + 2, n * n + 2 + k * 2, 2):
        x = int(data[i])
        y = int(data[i + 1])
        drops.append((x, y))
    
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    for x, y in drops:
        if grid[y][x] > 0:
            grid[y][x] -= min(8, grid[y][x])
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n: 
                if grid[ny][nx] > 0:
                    grid[ny][nx] -= min(4, grid[ny][nx])
    
    for row in grid:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
