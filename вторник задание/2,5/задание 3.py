def sort_strings():
    import sys

    n = int(sys.stdin.readline().strip())
    
    strings = [sys.stdin.readline().strip() for _ in range(n)]
    
    sorted_strings = sorted(strings)
    
    for string in sorted_strings:
        print(string)

if __name__ == "__main__":
    sort_strings()
