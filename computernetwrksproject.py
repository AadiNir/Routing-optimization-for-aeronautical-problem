import math
import networkx as nx
import csv
import matplotlib.pyplot as plt                                                                                                                                                                                                                         
class Plane:
    def __init__(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
    def display(self):
        return str(self.latitude) + " " + str(self.longitude) + " " + str(self.altitude)

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

def find_shortest_distance(planes, ground_stations, plane1, plane2):
    # Create a weighted graph
    G = nx.Graph()

    # Add nodes (planes and ground stations) to the graph
    for i, plane in enumerate(planes):
        G.add_node(i, type='Plane')
    for j, station in enumerate(ground_stations):
        G.add_node(len(planes) + j, type='Ground Station')

    # Calculate distance between each plane and each ground station and add weighted edges to the graph
    for i, plane in enumerate(planes):
        # if i not in (plane1, plane2):
            for j, station in enumerate(ground_stations):
                # print(plane.display())
                distance = calculate_distance(plane.latitude, plane.longitude, plane.altitude, station[0], station[1], station[2])
                G.add_edge(i, len(planes) + j, weight=distance)

    # Calculate distance between each planes and add weighted edges to the graph
    for i, p1 in enumerate(planes):
        for j, p2 in enumerate(planes):
            # if (i != plane1 or i != plane2) and (j != plane1 or j != plane2):
            distance = calculate_distance(p1.latitude, p1.longitude, p1.altitude, p2.latitude, p2.longitude, p2.altitude)
            G.add_edge(i, j, weight=distance)
    G.remove_edge(plane1, plane2)
    pos = nx.spring_layout(G, k=0.15, seed=42)
    plt.figure(figsize=(20, 20))
    nx.draw(G, pos, node_size=50, node_color='skyblue', edge_color='gray', width=0.5, with_labels=True)
    nx.draw(G)
    plt.savefig("filename9.png")
    plt.show()

    # Find the shortest path and distance between plane1 and plane2
  
    shortest_path = nx.dijkstra_path(G, source=plane1, target=plane2, weight='weight')
    shortest_distance = nx.dijkstra_path_length(G, source=plane1, target=plane2, weight='weight')

    # Calculate the distances between ground stations
    ground_station_distances = []
    for j, station in enumerate(ground_stations):
        distance = calculate_distance(station[1], station[0], station[2], station[1], station[0], station[2])
        ground_station_distances.append(distance)

    # Add plane1 to ground station distances
    for j, station in enumerate(ground_stations):
        distance = calculate_distance(planes[plane1].latitude, planes[plane1].longitude, planes[plane1].altitude, station[0], station[1], station[2])
        ground_station_distances[j] += distance

    # Add plane2 to ground station distances
    for j, station in enumerate(ground_stations):
        distance = calculate_distance(planes[plane2].latitude, planes[plane2].longitude, planes[plane2].altitude, station[0], station[1], station[2])
        ground_station_distances[j] += distance

    # Find the ground station with the shortest distance
    min_distance = min(ground_station_distances)
    min_distance_index = ground_station_distances.index(min_distance)

    return shortest_path, shortest_distance, min_distance_index

# Read the data from the CSV file
csv_filename = 'Computer-network/Dataset.csv'
data = read_csv_file(csv_filename)

# Extract the plane information from the data
planes = []
for row in data:
    latitude = float(row[3])
    longitude = float(row[4])
    altitude = float(row[2])
    plane = Plane(latitude, longitude, altitude)
    planes.append(plane)



# Define the ground stations
#0LHR  1EWR
ground_stations = [
    [0.4543, 51.4700,81.73],
    [74.1745, 40.6895,8.72]
]

# Define the indices of the planes you want to find the shortest distance between
plane1=72
plane2=89 # Find the shortest distance
#2
#84

#99
#121
# print(planes[:2])
# for i in range(148):
#     for j in range(148):
shortest_path, shortest_distance, min_distance_index = find_shortest_distance(planes, ground_stations, plane1, plane2)
print("Shortest path:", shortest_path)
# print("Shortest distance between plane1 and plane2:", shortest_distance)
# print("Ground station with the shortest distance:", min_distance_index)

Plane1=shortest_path[0]
Plane2=shortest_path[2]
plane11 = planes[Plane1]
plane22 = planes[Plane2]
lat1 = plane11.latitude
lon1 = plane11.longitude
alt1 = plane11.altitude

lat2 = plane22.latitude
lon2 = plane22.longitude
alt2 = plane22.altitude

if(min_distance_index==1):
    lat3=ground_stations[1][0]
    long3=ground_stations[1][1]
    alt3=ground_stations[1][2]
    n="LHR"
else:
    lat3=ground_stations[0][0]
    long3=ground_stations[0][1]
    alt3=ground_stations[0][2]
    n="EWR"

plt.scatter([lon1, lon2, long3], [lat1, lat2, lat3], c='b')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Points Plot')
plt.show()
# Assume you have the value of the speed of light in the specific medium
speed_of_light = 200000000 
total_distance = shortest_distance




def calculate_distance(lat1, lon1, alt1, lat2, lon2, alt2):
    
    lat1_rad = math.radians(float(lat1))
    lon1_rad = math.radians(float(lon1))
    alt1 = float(alt1)

    lat2_rad = math.radians(float(lat2))
    lon2_rad = math.radians(float(lon2))
    alt2 = float(alt2)

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = math.sqrt(c ** 2 + (alt2 - alt1) ** 2)

    return distance

d1=calculate_distance(data[shortest_path[0]][3],data[shortest_path[0]][4],data[shortest_path[0]][2],data[shortest_path[1]][3],data[shortest_path[1]][4],data[shortest_path[1]][2])
d2=calculate_distance(data[shortest_path[1]][3],data[shortest_path[1]][4],data[shortest_path[1]][2],data[shortest_path[2]][3],data[shortest_path[2]][4],data[shortest_path[2]][2])
if(d1>500):
    k=31.895
elif(d1<500 and 400<d1):
    k=43.505
elif(d1<400 and 300<d1):
    k=52.857
elif(d1<300 and 190<d1):
    k=63.970
elif(d1<190 and 90<d1):
    k=77.071
elif(d1<90 and 35<d1):
    k=93.854
else:
    k=119.130

if(d2>500):
    p=31.895
elif(d2<500 and 400<d2):
    p=43.505
elif(d2<400 and 300<d2):
    p=52.857
elif(d2<300 and 190<d2):
    p=63.970
elif(d2<190 and 90<d2):
    p=77.071
elif(d2<90 and 35<d2):
    p=93.854
else:
    p=119.130


# Calculate the latency delay
latency_delay = total_distance / speed_of_light

# Print the latency delay

print("{"+data[shortest_path[0]][0]+' routing path :'+"("+data[shortest_path[0]][0]+","+str(k)+"),("+data[shortest_path[1]][0]+","+str(p)+") => "+data[shortest_path[2]][0]+" end to end transmission rate:"+str(k)+" Ground station it used "+str(n)+" Latency delay is "+str(latency_delay)+"}")
