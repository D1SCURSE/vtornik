def main():
    import sys
    
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    N = int(data[0])
    
    dictionary = {}
    
    for i in range(1, N + 1):
        entry = data[i].split(maxsplit=1)
        word = entry[0]
        description = entry[1] if len(entry) > 1 else ''
        dictionary[word] = description
    
    M_index = N + 1
    M = int(data[M_index])
    
    results = []
    for i in range(M_index + 1, M_index + 1 + M):
        check_word = data[i]
        if check_word in dictionary:
            results.append(dictionary[check_word])
        else:
            results.append("Нет в словаре")
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()
