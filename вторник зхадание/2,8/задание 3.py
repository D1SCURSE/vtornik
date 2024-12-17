def main():
    import sys
    
    R = int(sys.stdin.readline().strip())
    
    table = [sys.stdin.readline().strip().split(',') for _ in range(R)]
    
    N = int(sys.stdin.readline().strip())
    
    for _ in range(N):
        row, col = map(int, sys.stdin.readline().strip().split(','))
        print(table[row][col])

if __name__ == "__main__":
    main()
