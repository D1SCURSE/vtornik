def main():
    import sys
    from collections import defaultdict
    
    text = sys.stdin.read().strip()
    
    words = text.split()
    
    word_count = defaultdict(int)
    
    result = []
    
    for word in words:
        word_count[word] += 1
        result.append(word_count[word])
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
