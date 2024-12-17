rows = int(input())
cols = int(input())

table = []

for _ in range(rows * cols):
    element = input().strip()
    table.append(element)

for i in range(rows):
    row_elements = table[i * cols:(i + 1) * cols]  
    print("\t".join(row_elements)) 
