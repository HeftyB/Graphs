from room import Room
from player import Player
from world import World

import random
from ast import literal_eval




class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)





# class Graph:

#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         """
#         Add a vertex to the graph.
#         """
#         self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         """
#         Add an undirected edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#             self.vertices[v2].add(v1)
#         else:
#             raise IndexError("That vertex does not exist!")


#     def get_neighbors(self, vertex_id):
#         """
#         Get all neighbors (edges) of a vertex.
#         """
#         return self.vertices[vertex_id]

#     def bft(self, starting_vertex):
#         """
#         Print each vertex in breadth-first order
#         beginning from starting_vertex.
#         """
#         q = Queue()
#         v = set()

#         q.enqueue(starting_vertex)

#         while q.size() > 0:
#             x = q.dequeue()

#             if x not in v:
#                 print(x)
#                 v.add(x)

#                 for n in self.get_neighbors(x):
#                     if n == x:
#                         continue
#                     q.enqueue(n)

#     def dft(self, starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """
#         s = Stack()
#         v = set()

#         s.push(starting_vertex)

#         while s.size() > 0:
#             x = s.pop()

#             if x not in v:
#                 print(x)
#                 v.add(x)

#                 for n in self.get_neighbors(x):
#                     if n == x:
#                         continue
#                     s.push(n)

#     def dft_recursive(self, starting_vertex, visted = set()):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.

#         This should be done using recursion.
#         """
#         print(starting_vertex)
#         if starting_vertex not in visted:
#             visted.add(starting_vertex)
        
#         for i in self.get_neighbors(starting_vertex):
#             if i in visted:
#                 continue
#             else:
#                 self.dft_recursive(i, visted)

#     def bfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """
#         q = Queue()
#         q.enqueue([starting_vertex])

#         while q.size() > 0:
#             d = q.dequeue()
#             l = d[-1]
#             if l == destination_vertex:
#                 return d

#             for n in self.get_neighbors(l):
#                 new_path = d.copy()
#                 new_path.append(n)
#                 q.enqueue(new_path)

#     def dfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.
#         """
#         s = Stack()
        
#         s.push([starting_vertex])

#         while s.size() > 0:
#             p = s.pop()
#             l = p[-1]

#             if l == destination_vertex:
#                 return p

#             for n in self.get_neighbors(l):
#                 new_path = p.copy()
#                 new_path.append(n)
#                 s.push(new_path)


#     def dfs_recursive(self, starting_vertex, destination_vertex, current_node=None, visited=set(), path=[]):
#         """
#         Return a list containing a path from
#         starting_vertex to destination_vertex in
#         depth-first order.

#         This should be done using recursion.
#         """

#         # not finished 
#         if current_node is None:
#             current_node = starting_vertex
#         if current_node in visited:
#             return
#         visited.add(current_node)
#         path.append(current_node)
#         if current_node == destination_vertex:
#             return path
#         else:
#             print(path)
#             for n in self.get_neighbors(current_node):
#                 if n in visited:
#                     continue
#                 else:
#                     return self.dfs_recursive(starting_vertex, destination_vertex, n, visited, path)



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

visited_rooms.add(000)




def get_neighbors(current_node):
    roomdict = room_graph[current_node][1]
    neighbors = []
    for key, value in roomdict.items():
        neighbors.append(value)
    # if len(neighbors) == 0:
    #     return False
    else:
        return neighbors



def bfs(starting_vertex):
    q = Queue()
    q.enqueue([starting_vertex])

    while q.size() > 0:
        d = q.dequeue()
        l = d[-1]
        if l not in visited_rooms:
            return d

        neighbors = set(get_neighbors(l))
        # neighbors.difference_update(visited_rooms)

        for n in neighbors:
            new_path = d.copy()
            new_path.append(n)
            q.enqueue(new_path)


current_node = 000

while len(visited_rooms) < len(room_graph):
    path = bfs(current_node)

    for i in path[1:]:
        traversal_path.append(i)
        visited_rooms.add(i)

    current_node = path[-1]
print()
print()
print("**********************")
print("**********************")
print(f"traverse path ->>>> {traversal_path}")
print(f"visited rooms ->>>> {visited_rooms}")
print("**********************")
print(f"TOTAL STEPS IS     {len(traversal_path)}")
print()
print()

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
