from collections import Counter

def most_frequent_character(s):
    s = s.lower().replace(' ', '')
    
    frequency = Counter(s)
    most_frequent = min((char for char in frequency if frequency[char] == max(frequency.values())), default=None)
    
    return most_frequent

input_string = input().strip()

result = most_frequent_character(input_string)
print(result)
