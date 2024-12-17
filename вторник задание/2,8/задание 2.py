rows = int(input())
cols = int(input())

table = []


for _ in range(rows):
    row = [input().strip() for _ in range(cols)]
    table.append(row)

for row in table:
    print('\t'.join(row))

print()

for col in range(cols):
    transposed_row = [table[row][col] for row in range(rows)]
    print('\t'.join(transposed_row))
