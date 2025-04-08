"""
The given map was represented using a graph.
For a selected city, the program prints the shortest distances to all other cities using Dijkstra’s algorithm.
"""
import heapq

# Implements Dijkstra's algorithm to find the shortest path from a start city to all other cities
def dijkstra(graph, start):
    # Initialize distances for all cities as infinity, except the start city which is set to 0
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    # Priority queue to process the cities with the shortest known distance
    heap = [(0, start)]
    
    while heap:
        # Get the city with the smallest distance
        (dist, current) = heapq.heappop(heap)
        
        # If this distance is greater than the already known shortest distance, continue
        if dist > distances[current]:
            continue
        
        # Update the distances for all the neighbors of the current city
        for neighbor, weight in graph[current].items():
            distance = dist + weight  # Calculate the distance to this neighbor
            if distance < distances[neighbor]:  # If we found a shorter path
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))  # Add the neighbor to the priority queue
                
    return distances


# Graph representation of cities and the distances between them (weighted graph)
graph = {
    'Ostrava': {'Olomouc': 84, 'Liberec': 340},
    'Liberec': {'Ostrava': 340, 'Praha': 75},
    'Praha': {'Liberec': 75, 'Plzeň': 120, 'Brno': 186, 'České Budějovice': 77, 'Olomouc': 252},
    'Brno': {'Praha': 186, 'Olomouc': 95},
    'Olomouc': {'Ostrava': 84, 'Brno': 95, 'Praha': 252},
    'České Budějovice': {'Praha': 77, 'Plzeň': 92},
    'Plzeň': {'Praha': 120, 'České Budějovice': 92}
}

# Select the starting city
start_city = 'Ostrava'

# The order in which the cities will be printed
city_order = ['Ostrava', 'Praha', 'Liberec', 'Plzeň', 'České Budějovice', 'Brno', 'Olomouc']

# Find the shortest distances from the start city to all other cities
distances = dijkstra(graph, start_city)

# Print the shortest distances to each city from the start city
print(f'From the city {start_city}, the other cities are located at:')
for city in sorted(distances.keys(), key=lambda x: city_order.index(x)):
    if city != start_city:
        print(f'{city}: {distances[city]} km.')
