n0 = int(input().strip())
items = [input().strip() for _ in range(n0)]

k = int(input().strip())

current_items = items[:]  

for _ in range(k):
    ni = len(current_items)  
    ni_plus_1 = int(input().strip())  
    new_indices = [int(input().strip()) - 1 for _ in range(ni_plus_1)] 
    
    current_items = [current_items[i] for i in new_indices]


for item in current_items:
    print(item)
