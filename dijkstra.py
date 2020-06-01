"""

1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.

2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other
nodes. Set the initial node as current

3. For the current node, consider all of its unvisited neighbours and calculate their tentative distances through the
current node. Compare the newly calculated tentative distance to the current assigned value and assign the smaller
one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbour B
has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater
than 8 then change it to 8. Otherwise, the current value will be kept.

4. When we are done considering all of the unvisited neighbours of the current node, mark the current node as visited
and remove it from the unvisited set. A visited node will never be checked again

5. If the destination node has been marked visited (when planning a route between two specific nodes) or if the
smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal;
occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. The algorithm
has finished

6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new
"current node", and go back to step 3

"""

import numpy as np
import itertools
import matplotlib.pyplot as plt
import random


class Node:
    def __init__(self, coords, distance=np.inf, previous=(), neighbors=None):
        if neighbors is None:
            neighbors = []
        self.coords = coords
        self.distance = distance
        self.neighbors = neighbors
        self.previous = previous


def dist_between(p1, p2):
    # Accepts two points in tuple form and returns distance between
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def get_neighbors(coords):
    valid_spots = []
    for r in range(coords[0]-1, coords[0]+2):
        if r < 0 or r > ROWS:
            continue
        for c in range(coords[1] - 1, coords[1] + 2):
            if c < 0 or c > COLS:
                continue
            # Else, add this coord to our returned locations
            if (r, c) != coords:
                valid_spots.append((r, c))
    return valid_spots


def find(lst, points):
    # Return index locations of coordinates in the Q set
    if type(points) != list:
        # Handle a single coordinate tuple
        points = [points]

    return [idx for idx, val in enumerate(lst) if val.coords in points]


def rect(top, bot, left, right):
    # Return all grid points between four corners (inclusive)
    points = []
    for x in range(left, right+1):
        for y in range(bot, top+1):
            points.append((x, y))
    return points


def create_full_grid(R, C):
    locations = list(itertools.product(range(0, R), range(0, C), repeat=1))
    nodes = []
    for idx in range(len(locations)):
        # [ (location), distance, (previous), [(neighbors)]]
        # Update: Get neighbors now, instead of later
        # nodes.append([locations[idx], np.inf, (), get_neighbors(locations[idx])])
        # Update: Change to object format, same info
        nodes.append(Node(coords=locations[idx],
                          distance=np.inf,
                          previous=(),
                          neighbors=get_neighbors(locations[idx])))
    return nodes


def create_sparse_grid(R, C, N):
    coords = []
    # Create N (unique points)
    for n in range(N):
        new_coord = None
        attempts = 0
        while not new_coord:
            attempts += 1
            new_coord = (random.randint(0, R), random.randint(0, C))
            if new_coord in coords:
                new_coord = None  # Throw away if now unique
            if attempts > 100:
                print('Failed to find unique coords')
                break
        # print(f'adding new coord {new_coord}')
        coords.append(new_coord)

    nodes = []
    # Connect each to a few others
    for c in coords:
        n_conn = int(np.random.uniform(5))
        # n_conn = 5
        # Create a list of distances that aligns with list of coords
        # print(f'Measuring distances from {c}')
        dist_to_neighbors = [dist_between(c, neighbor) for neighbor in coords]
        my_neighbors = []
        for n in range(1, n_conn+1):
            # Starting at 1 excludes ourself
            dist_of_neighbor = sorted(dist_to_neighbors)[n]
            neighbor_idx = dist_to_neighbors.index(dist_of_neighbor)
            my_neighbors.append(coords[neighbor_idx])
        nodes.append(Node(coords=c,
                          neighbors=my_neighbors))
        # Sort other points by distance

    return nodes


# Create an N x N grid
ROWS = 40
COLS = 40


# Maps of distance and previous locations
# Q = create_full_grid(ROWS, COLS)
Q = create_sparse_grid(ROWS, COLS, 150)
visited = []

# Delete
#n_blocks = int(len(Q)/2.2)  # Half of locations
#for b in range(n_blocks):
#    Q.pop(random.randrange(len(Q)))

# Choose end-points from what's left
rand_origin = random.choice(Q)
origin = rand_origin.coords
rand_dest = random.choice(Q)
destination = rand_dest.coords

print(f'Navigating from {origin} to {destination}')

origin_idx = find(Q, origin)[0]
Q[origin_idx].distance = 0  # Initial distance = 0

##### PLOTTING PART 1  #####
fig, ax = plt.subplots(figsize=(8, 8))
grid_points_i = [q.coords for q in Q]
x_i, y_i = zip(*grid_points_i)  # Unzip to two arrays
# Plot all points
ax.scatter(x_i, y_i, marker='s', c='grey')
# Plot all connections
for q in Q:
    for n in q.neighbors:
        ax.plot((q.coords[0], n[0]), (q.coords[1], n[1]), ':', linewidth=2, c='grey')
# Highlight endpoints
ax.scatter((origin[0], destination[0]), (origin[1], destination[1]), facecolors='none', edgecolors='r')

##### Calculate route  #####
while Q:
    distances = [node.distance for node in Q]
    min_dist = min(distances)
    u = Q[distances.index(min_dist)]  # Select entire row at minimum distance

    # Remove u from Q
    Q.remove(u)
    visited.append(u)
    # Check neighbors of u
    #neighbors = get_neighbors(u[0])  # list of tuple coords
    #neighbors = u[3]
    neighbors = u.neighbors
    neighbor_idx = find(Q, neighbors)
    print(f'Checking on my {len(neighbor_idx)} neighbors')
    try:
        for n in neighbor_idx:

            if not Q[n]:
                print('No valid neighbors')
                break
            # alt = u.distance + np.sqrt((Q[n].coords[0]-u.coords[0])**2 + (Q[n].coords[1]-u.coords[1])**2)
            alt = u.distance + dist_between(Q[n].coords, u.coords)
            if alt < Q[n].distance:
                Q[n].distance = alt
                Q[n].previous = u.coords
    except Exception as e:
        print(f'Failed with exception: {e}')
        break

##### PLOTTING PART 2  #####
grid_points = [q.coords for q in visited]
clrs = [q.distance for q in visited]
x, y = zip(*grid_points)  # Unzip to two arrays
# Plot active grid
ax.scatter(x, y, c=clrs, marker='s')
# Highlight endpoints
ax.scatter((origin[0], destination[0]), (origin[1], destination[1]), marker='s', facecolors='none', edgecolors='r')
ax.set_aspect('equal')

# Navigate from finish to start
loc = destination
steps_traveled = 0
dist_traveled = 0
try:
    while loc != origin:
        next_row = visited[find(visited, loc)[0]]
        next_loc = next_row.previous
        # Plot path segment
        ax.plot((loc[0], next_loc[0]), (loc[1], next_loc[1]), 'r-', linewidth=2)
        loc = next_loc
        steps_traveled += 1
        dist_traveled += next_row.distance
    print(f'arrived in {steps_traveled} steps, dist: {dist_traveled}')
except IndexError as e:
    print(f"Couldn't plot path! : {e}")
plt.show()

"""
function Dijkstra(Graph, source):
 2
 3      create vertex set Q
 4
 5      for each vertex v in Graph:             
 6          dist[v] ← INFINITY                  
 7          prev[v] ← UNDEFINED                 
 8          add v to Q                      
10      dist[source] ← 0                        
11      
12      while Q is not empty:
13          u ← vertex in Q with min dist[u]    
14                                              
15          remove u from Q 
16          
17          for each neighbor v of u:           // only v that are still in Q
18              alt ← dist[u] + length(u, v)
19              if alt < dist[v]:               
20                  dist[v] ← alt 
21                  prev[v] ← u 
22
23      return dist[], prev[]
"""


"""
# destination = (np.random.randint(1, ROWS-1), np.random.randint(1, COLS-1))
#destination = (1, 25)
#destination = (25, 20)
#origin = (10, 10)
block = [(21, 14), (21, 13), (22, 13), (23, 13), (24, 13),
         (21, 15), (21, 16), (21, 17), (21, 18), (21, 19),
         (22, 19), (23, 19), (24, 19), (25, 19),
         (25, 18), (25, 17), (25, 16), (25, 15),
         (24, 15), (23, 15), (23, 16), (23, 17)]
block += rect(top=12, bot=0, left=24, right=24)
# block += rect(top=10, bot=0, left=25, right=29)
block += rect(top=28, bot=0, left=6, right=6)
block += rect(top=29, bot=3, left=3, right=3)

# Create obstacles
#for b in block:
#    Q.pop(find(Q, b)[0])
"""