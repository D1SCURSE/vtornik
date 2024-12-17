input_data = input()

numbers = map(int, input_data.split())

output = '\n'.join('*' * num for num in numbers)
print(output)
