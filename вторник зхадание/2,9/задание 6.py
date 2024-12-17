import sys
import re
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    N = int(data[0])
    word_count = defaultdict(int)
    
    word_pattern = re.compile(r'[а-яА-ЯёЁ]+')
    
    for i in range(1, N + 1):
        line = data[i]
        words = word_pattern.findall(line) 
        for word in words:
            word_count[word] += 1  
    
    sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_words:
        formatted_word = word.capitalize()  
        print(formatted_word)

if __name__ == "__main__":
    main()
