N = int(input().strip())

queue = []

for _ in range(N):
    event = input().strip()
    
    if "встал(а) в очередь." in event:
        surname = event.split()[0]
        queue.append(surname)
    
    elif "Привет," in event:
        parts = event.split()
        surname1 = parts[1]  
        surname2 = parts[5] 
        index = queue.index(surname1) 
        queue.insert(index + 1, surname2)  
    
    elif "хватит тут стоять," in event:
      
        surname = event.split(',')[0]
        queue.remove(surname)
for person in queue:
    print(person)
