from room import Room
from player import Player
from world import World

import random
from ast import literal_eval




class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        for i in self.queue:
            if i == value:
                return
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


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
traversal_path_by_room = []


new_visited_rooms = set()

new_visited_rooms.add(000)

def get_neighbors(current_node):
    roomdict = room_graph[current_node][1]
    neighbors = []
    for key, value in roomdict.items():
        neighbors.append(value)
    
    return neighbors



def bfs(starting_vertex):
    q = Queue()
    q.enqueue([starting_vertex])

    while q.size() > 0:
        d = q.dequeue()
        l = d[-1]
        if l not in new_visited_rooms:
            return d

        neighbors = set(get_neighbors(l))
        
        for n in neighbors:
            if n not in d:
                new_path = d.copy()
                new_path.append(n)
                q.enqueue(new_path)


def dfs(starting_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    s = Stack()

    s.push([starting_vertex])

    while s.size() > 0:
        p = s.pop()
        l = p[-1]

        if l not in new_visited_rooms:
            return p
        neighbors = set(get_neighbors(l))
        
        for n in neighbors:
            new_path = p.copy()
            new_path.append(n)
            s.push(new_path)


current_node = 000

while len(new_visited_rooms) < len(room_graph):
    path = bfs(current_node)
    # path = dfs(current_node)
    
    for i in path[1:]:
        traversal_path_by_room.append(i)
        new_visited_rooms.add(i)
        roomdict = room_graph[current_node][1]

        
        for key, value in roomdict.items():
            if i == value:
                traversal_path.append(key)
        current_node = i


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

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
