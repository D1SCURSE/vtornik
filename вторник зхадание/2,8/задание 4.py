def brain_explode_interpreter(program):
    tape = [0] * 30000
    pointer = 0
    
    output = []
    
    for command in program:
        if command == '>':
            pointer = (pointer + 1) % 30000
        elif command == '<':
            pointer = (pointer - 1) % 30000
        elif command == '+':
            tape[pointer] = (tape[pointer] + 1) % 256
        elif command == '-':
            tape[pointer] = (tape[pointer] - 1) % 256
        elif command == '.':
            output.append(tape[pointer])
    
    return output

program = input().strip()

result = brain_explode_interpreter(program)
print(' '.join(map(str, result)))
