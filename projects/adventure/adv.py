# from projects.adventure.room import Room
from room import Room
# from projects.adventure.world import World
from world import World

from player import Player

import random
from ast import literal_eval


class Queue():
    def __init__(self):
        self.queue = []

    def __str__(self):
        return f"{set(self.queue)}"

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Pathfinder:
    def __init__(self, player, initial_exits):
        self.player = player
        self.starting_room = player.current_room
        self.rooms = {}

    def add_room(self, room_id):
        self.rooms[room_id] = dict()

    def add_exit(self, r1, direction, r2='?'):
        self.rooms[r1][direction] = r2

    def get_exits(self, room_id):
        return self.rooms[room_id]

    def wander(self):
        q = Queue()
        q.enqueue(self.starting_room)
        visited = set()
        prev_room = None
        while q.size > 0:

            curr_room = q.dequeue()
            # add to visited, add exits
            if curr_room not in visited:
                visited.add(curr_room)
                possible_exits = curr_room.get_exits()
                if prev_room is not None:

                    # add exits if not already present
                for pot_exit in possible_exits:
                    if pot_exit not in curr_room:
                        self.add_exit(curr_room, pot_exit, '?')

        # choose exit


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

p = Pathfinder(player)
print("wander ", p.wander())

# start pathfinding at starting room


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
