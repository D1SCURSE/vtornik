def main():
    import sys
    
    input_data = sys.stdin.read().strip().splitlines()
    indices = list(map(int, input_data[0].split()))
    words = input_data[1].split()
    
    result_words = [words[i - 1] for i in indices]
    result_sentence = ' '.join(result_words)
    
    result_sentence = result_sentence.capitalize()
    print(result_sentence)

if __name__ == "__main__":
    main()
