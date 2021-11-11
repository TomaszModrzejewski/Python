
import heapq
from pprint import pprint
items = [
    {'name': 'Item-1', 'price': 101.1},
    {'name': 'Item-2', 'price': 555.22},
    {'name': 'Item-3', 'price': 45.09},
    {'name': 'Item-4', 'price': 22.75},
    {'name': 'Item-5', 'price': 16.30},
    {'name': 'Item-6', 'price': 110.65}
]

cheap = heapq.nsmallest(3, items, key=lambda s: s['price'])
expensive = heapq.nlargest(3, items, key=lambda s: s['price'])
print("Original datasets:")
pprint(items)
print("\nFirst 3 expensive items:")
pprint(expensive)
print("\nFirst 3 cheap items:")
pprint(cheap)
				 
	
