import math
import networkx as nx
import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calculate_distance(lat1, lon1, alt1, lat2, lon2, alt2):
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    alt1 = alt1

    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    alt2 = alt2

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = math.sqrt(c ** 2 + (alt2 - alt1) ** 2)

    return distance

# Read the data from the CSV file
csv_filename = 'Computer-network/Dataset.csv'
data = read_csv_file(csv_filename)

# Extract the required information (latitude, longitude, altitude)
result = [[float(num) for num in inner_list[2:5]] for inner_list in data]

# Create a weighted graph
G = nx.Graph()
ground_stations = [
    [81.73, 0.4543, 51.4700],
    [8.72, 74.1745, 40.6895]
]

# Add nodes (planes and ground stations) to the graph
for i, plane in enumerate(result):
    G.add_node(i, type='Plane')
for j, station in enumerate(ground_stations):
    G.add_node(len(result) + j, type='Ground Station')

# Calculate distance between each plane and each ground station and add weighted edges to the graph
for i, plane in enumerate(result):
    for j, station in enumerate(ground_stations):
        distance = calculate_distance(plane[2], plane[1], plane[0],
                                      station[1], station[0], station[2])
        G.add_edge(i, len(result) + j, weight=distance)

# Find the shortest path and distance using Dijkstra's algorithm
shortest_path = nx.dijkstra_path(G, source=4, target=len(result) + 1, weight='weight')
shortest_distance = nx.dijkstra_path_length(G, source=19, target=len(result) + 1, weight='weight')

# Extract the routing path coordinates and node indices
path_coordinates = [(result[node][1], result[node][0], result[node][2]) for node in shortest_path[:-1]]
path_indices = shortest_path[:-1]

print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)
print("Path coordinates:", path_coordinates)
print("Path indices:", path_indices)
for node in shortest_path:
    if node < len(result):
        print("Plane:", node)
        # Access other plane information using result[node]
    else:
        print("Ground Station:", node - len(result))

