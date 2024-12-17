N = int(input().strip())

strings = [input().strip() for _ in range(N)]

sorted_strings = sorted(strings, key=lambda s: (len(s), s))

for string in sorted_strings:
    print(string)
