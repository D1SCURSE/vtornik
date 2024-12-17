def generate_bar_chart(data):
    max_height = max(data)

    width = len(data) + 2
    print('*' * width)
    
    for level in range(max_height, 0, -1):

        line = '*'
        
        for height in data:
            if height >= level:
                line += '*'
            else:
                line += ' '
        
        line += '*'
        
        print(line)
    
    print('*' * width)

input_data = input()
numbers = list(map(int, input_data.split()))

generate_bar_chart(numbers)
