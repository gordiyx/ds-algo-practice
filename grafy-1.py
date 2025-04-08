"""
The given map was represented using a graph structure.
For a selected city, the program prints how many cities are reachable and through how many intermediate cities (using Breadth-First Search (BFS)).
"""

from collections import deque

# Graph representation of cities and direct connections (undirected)
graph = {
    'Ostrava': ['Olomouc', 'Liberec'],
    'Liberec': ['Ostrava', 'Praha'],
    'Praha': ['Liberec', 'Plzeň', 'Brno', 'České Budějovice'],
    'Brno': ['Praha'],
    'Olomouc': ['Ostrava', 'Brno'],
    'České Budějovice': ['Praha', 'Plzeň'],
    'Plzeň': ['Praha', 'České Budějovice']
}

# Performs Breadth-First Search from the starting city
# Returns a dictionary of reachable cities and the number of steps (edges) required to reach each
def bfs(graph, start):
    visited = set()
    result = {}  # Stores city: distance_from_start
    queue = deque([(start, 0)])
    visited.add(start)

    while queue:
        vertex, dist = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                result[neighbor] = dist + 1  # Distance from start
    return result


# Choose the starting city
start_city = 'Ostrava'
reachable_cities = bfs(graph, start_city)

# Cities in consistent output order
cities_in_order = ['Praha', 'Liberec', 'Plzeň', 'České Budějovice', 'Brno', 'Olomouc']

# Display reachable cities with intermediate step count
print(f'From {start_city}, the following cities are reachable:')
for city in cities_in_order:
    if city in reachable_cities:
        distance = reachable_cities[city]
        if distance == 1:
            print(f'  - {city} is directly connected to {start_city}.')
        else:
            print(f'  - {city} is reachable through {distance - 1} intermediate cities.')
