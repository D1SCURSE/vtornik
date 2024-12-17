def process_queue_events(events):
    queue = []
    
    for event in events:
        if "встал(а) в очередь." in event:
            surname = event.split(" ")[0]
            queue.append(surname)
        
        elif "Привет," in event:

            parts = event.split("!")
            surname1 = parts[0].split(", ")[1]  
            surname2 = parts[1].split(" ")[0]    
            index = queue.index(surname2) + 1    
            queue.insert(index, surname1)
        
        elif "хватит тут стоять, пошли отсюда." in event:           
            surname = event.split(",")[0]
            queue.remove(surname)
    
    return queue

import sys

input = sys.stdin.read
data = input().strip().splitlines()

N = int(data[0]) 
events = data[1:N + 1]

result_queue = process_queue_events(events)

for person in result_queue:
    print(person)
