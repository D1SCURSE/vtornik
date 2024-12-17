input_string = input()

count = sum(1 for char in input_string if char not in (' ', '\t'))

print(count)
