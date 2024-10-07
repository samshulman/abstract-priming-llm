import numpy as np
import random
from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.nodes = defaultdict(list)
        self.colors = {}
        self.room_numbers = {}

    def add_node(self, node, color, room_number):
        if node not in self.colors:
            self.colors[node] = color
            self.room_numbers[node] = room_number

    def add_edge(self, node1, node2):
        self.nodes[node1].append(node2)
        self.nodes[node2].append(node1)

    def display_graph(self):
        """
        Creates a text-based representation of the graph structure.
        Returns a string containing the node colors and connections.
        """
        result = "Node Colors:\n"
        for node in sorted(self.nodes.keys()):
            result += f"Node {node} (Room {self.room_numbers[node]}): {self.colors[node]}\n"
        
        result += "\nConnections:\n"
        for node in sorted(self.nodes.keys()):
            connections = self.nodes[node]
            if connections:
                conn_desc = [f"Node {conn} (Room {self.room_numbers[conn]})" for conn in sorted(connections)]
                result += f"Node {node} is connected to: {', '.join(conn_desc)}\n"
            else:
                result += f"Node {node} has no connections\n"
        
        return result

    def generate_desc_color(self):
        description = []
        for node, connections in self.nodes.items():
            node_color = self.colors[node]
            if connections:
                conn_colors = [f"the {self.colors[conn]} room" for conn in connections]
                if len(conn_colors) > 1:
                    conn_desc = ', '.join(conn_colors[:-1]) + f" and {conn_colors[-1]}"
                else:
                    conn_desc = conn_colors[0]
            else:
                conn_desc = "no other rooms"
            description.append(f"The {node_color} room is connected to {conn_desc}.")
        random.shuffle(description)
        return ' '.join(description)

    def generate_desc_room(self):
        description = []
        for node, connections in self.nodes.items():
            room_number = self.room_numbers[node]
            if connections:
                conn_rooms = [f"Room {self.room_numbers[conn]}" for conn in connections]
                if len(conn_rooms) > 1:
                    conn_desc = ', '.join(conn_rooms[:-1]) + f" and {conn_rooms[-1]}"
                else:
                    conn_desc = conn_rooms[0]
            else:
                conn_desc = "no other rooms"
            description.append(f"Room {room_number} is connected to {conn_desc}.")
        random.shuffle(description)
        return ' '.join(description)
    
    def generate_desc_mixed(self):
        """
        Generates a mixed description of the graph, randomly using either room numbers or colors for each node.
        Returns a string describing each node's connections with a mix of room numbers and colors.
        """
        description = []
        for node, connections in self.nodes.items():
            # Randomly choose whether to use color or room number for this node
            if random.choice([True, False]):
                node_desc = f"The {self.colors[node]} room"
            else:
                node_desc = f"Room {self.room_numbers[node]}"
            
            if connections:
                conn_desc = []
                for conn in connections:
                    # Randomly choose whether to use color or room number for each connection
                    if random.choice([True, False]):
                        conn_desc.append(f"the {self.colors[conn]} room")
                    else:
                        conn_desc.append(f"Room {self.room_numbers[conn]}")
                
                if len(conn_desc) > 1:
                    conn_str = ', '.join(conn_desc[:-1]) + f" and {conn_desc[-1]}"
                else:
                    conn_str = conn_desc[0]
            else:
                conn_str = "no other rooms"
            
            description.append(f"{node_desc} is connected to {conn_str}.")
        random.shuffle(description)
        return ' '.join(description)

    def shortest_path(self, start, end, by_attribute):
        queue = [(0, start, [])]
        visited = set()

        while queue:
            (cost, current, path) = heapq.heappop(queue)
            if current not in visited:
                visited.add(current)
                path = path + [current]

                if by_attribute(current) == end:
                    return path

                for neighbor in self.nodes[current]:
                    if neighbor not in visited:
                        heapq.heappush(queue, (cost + 1, neighbor, path))
        return None

    def shortest_path_color(self, start_color, end_color):
        """
        Find the shortest path between two colors.
        start_color and end_color are color strings.
        """
        start_node = next((node for node, color in self.colors.items() if color == start_color), None)
        if start_node is None:
            return None  # Start color not found in the graph

        path = self.shortest_path(start_node, end_color, lambda node: self.colors[node])
        if path:
            return [self.colors[node] for node in path]
        return None

    def shortest_path_room(self, start_room, end_room):
        """
        Find the shortest path between two room numbers.
        start_room and end_room are room number integers.
        """
        start_node = next((node for node, room in self.room_numbers.items() if room == start_room), None)
        if start_node is None:
            return None  # Start room not found in the graph

        path = self.shortest_path(start_node, end_room, lambda node: self.room_numbers[node])
        if path:
            return [self.room_numbers[node] for node in path]
        return None

    def select_random_nodes(self, n, return_type='node'):
        """
        Select n random nodes from the graph.
        
        Parameters:
        - n: number of nodes to select
        - return_type: 'node', 'room', or 'color' to specify the return format
        
        Returns a list of node identifiers, room numbers, or colors depending on return_type.
        """
        all_nodes = list(self.nodes.keys())
        selected_nodes = random.sample(all_nodes, min(n, len(all_nodes)))
        
        if return_type == 'node':
            return selected_nodes
        elif return_type == 'room':
            return [self.room_numbers[node] for node in selected_nodes]
        elif return_type == 'color':
            return [self.colors[node] for node in selected_nodes]
        else:
            raise ValueError("Invalid return_type. Choose 'node', 'room', or 'color'.")

    def generate_new_graph_with_different_labels(self):
        """
        Generate a new graph with the same structure but different labels.
        Returns a new Graph object.
        """
        new_graph = Graph()
        
        # Generate new colors and room numbers
        new_colors = list(self.colors.values())
        new_room_numbers = list(self.room_numbers.values())
        random.shuffle(new_colors)
        random.shuffle(new_room_numbers)
        
        # Add nodes with new labels
        for i, node in enumerate(self.nodes.keys()):
            new_graph.add_node(node, new_colors[i], new_room_numbers[i])
        
        # Add edges (only once per pair of nodes)
        added_edges = set()
        for node, connections in self.nodes.items():
            for conn in connections:
                # Create a sorted tuple of the node pair to ensure uniqueness
                edge = tuple(sorted([node, conn]))
                if edge not in added_edges:
                    new_graph.add_edge(node, conn)
                    added_edges.add(edge)
        
        return new_graph

    def describe_room_color_mapping(self):
        """
        Generates a description of the mapping between room numbers and colors.
        Returns a string with each room number and its corresponding color.
        """
        mapping = []
        for node, room_number in self.room_numbers.items():
            color = self.colors[node]
            mapping.append(f"Room {room_number} is {color}")

        # Randomize the order of the mapping
        random.shuffle(mapping)
        return ". ".join(mapping) + "."

        
    def select_two_non_adjacent_nodes_with_path(self, return_type='node'):
        """
        Selects two non-adjacent nodes from the graph that have a valid path between them.

        Parameters:
        - return_type: 'node', 'room', or 'color' to specify the return format.

        Returns a tuple of two node identifiers, room numbers, or colors depending on return_type.
        Returns None if no such pair exists or if an invalid return_type is specified.
        """
        all_nodes = list(self.nodes.keys())

        if len(all_nodes) < 2:
            return None  # Not enough nodes in the graph

        def has_path(start, target):
            if self.shortest_path_room(self.room_numbers[start], self.room_numbers[target]) != None:
                return True
            return False

        for _ in range(100):  # Limit attempts to avoid infinite loop in dense graphs
            node1 = random.choice(all_nodes)
            possible_node2 = [node for node in all_nodes if node != node1 and node not in self.nodes[node1]]

            if possible_node2:
                node2 = random.choice(possible_node2)
                # Ensure there is a valid path between node1 and node2
                if has_path(node1, node2):
                    
                    if return_type == 'node': 
                        return (node1, node2)
                    elif return_type == 'room':
                        return (self.room_numbers[node1], self.room_numbers[node2])
                    elif return_type == 'color':
                        return (self.colors[node1], self.colors[node2])
                    else:
                        return None

        return None


# n7line_double = Graph()
# n7line_double.add_node('A', 'red', 1)
# n7line_double.add_node('B', 'blue', 2)
# n7line_double.add_node('C', 'green', 3)
# n7line_double.add_node('D', 'yellow', 4)
# n7line_double.add_node('E', 'purple', 5)
# n7line_double.add_node('F', 'orange', 6)
# n7line_double.add_node('G', 'pink', 7)
# n7line_double.add_edge('A', 'B')
# n7line_double.add_edge('A', 'C')
# n7line_double.add_edge('B', 'D')
# n7line_double.add_edge('C', 'E')
# n7line_double.add_edge('D', 'F')
# n7line_double.add_edge('E', 'G')
# n7line_double.add_node('H', 'turquoise', 8)
# n7line_double.add_node('I', 'cyan', 9)
# n7line_double.add_node('J', 'magenta', 10)
# n7line_double.add_node('K', 'indigo', 11)
# n7line_double.add_node('L', 'navy', 12)
# n7line_double.add_node('M', 'beige', 13)
# n7line_double.add_node('N', 'grey', 14)
# n7line_double.add_edge('H', 'I')
# n7line_double.add_edge('H', 'J')
# n7line_double.add_edge('I', 'K')
# n7line_double.add_edge('J', 'L')
# n7line_double.add_edge('K', 'M')
# n7line_double.add_edge('L', 'N')

# print(n7line_double.select_two_non_adjacent_nodes_with_path())

# for i in range(10):
#     n7line = n7line.generate_new_graph_with_different_labels()

#     nodes_room = n7line.select_random_nodes(2, 'room')
#     nodes_color = n7line.select_random_nodes(2, 'color')
#     print(n7line.shortest_path_room(nodes_room[0], nodes_room[1]))
#     print(n7line.shortest_path_color(nodes_color[0], nodes_color[1]))

#     # CONSISTENT

#     # AVG over 
#     print("\nMapping, Desc, Consistent Room")
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(n7line.generate_desc_room()) # room 1 is connected to room 2
#     print(f"What is the shortest path from room {nodes_room[0]} to room {nodes_room[1]}?")

#     print("\nMapping, Desc, Consistent Color")
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(n7line.generate_desc_color()) # the red room is connected to the blue room
#     print(f"What is the shortest path from the {nodes_color[0]} room to the {nodes_color[1]} room?")


#     # AVG over 
#     print("\nDesc, Mapping, Consistent Room")
#     print(n7line.generate_desc_room()) # room 1 is connected to room 2
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(f"What is the shortest path from room {nodes_room[0]} to room {nodes_room[1]}?")

#     print("\nDesc, Mapping, Consistent Color")
#     print(n7line.generate_desc_color()) # the red room is connected to the blue room
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(f"What is the shortest path from the {nodes_color[0]} room to the {nodes_color[1]} room?")



#     # INCONSISTENT

#     # AVG over 
#     print("\nMapping, Desc, Inconsistent Color-Room")
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(n7line.generate_desc_room()) # room 1 is connected to room 2
#     print(f"What is the shortest path from the {nodes_color[0]} room to the {nodes_color[1]} room?")

#     print("\nMapping, Desc, Inconsistent Room-Color")
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(n7line.generate_desc_color()) # the red room is connected to the blue room
#     print(f"What is the shortest path from room {nodes_room[0]} to room {nodes_room[1]}?")


#     # AVG over 
#     print("\nDesc, Mapping, Inconsistent Color-Room")
#     print(n7line.generate_desc_room()) # room 1 is connected to room 2
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(f"What is the shortest path from the {nodes_color[0]} room to the {nodes_color[1]} room?")

#     print("\nDesc, Mapping, Inconsistent Room-Color")
#     print(n7line.generate_desc_color()) # the red room is connected to the blue room
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(f"What is the shortest path from room {nodes_room[0]} to room {nodes_room[1]}?")



#     # MIXED

#     # AVG over 
#     print("\nMapping, Desc, Room")
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(n7line.generate_desc_mixed()) # room 1 is connected to the blue room
#     print(f"What is the shortest path from room {nodes_room[0]} to room {nodes_room[1]}?")

#     print("\nMapping, Desc, Color")
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(n7line.generate_desc_mixed()) # room 1 is connected to the blue room
#     print(f"What is the shortest path from the {nodes_color[0]} room to the {nodes_color[1]} room?")


#     # AVG over 
#     print("\nDesc, Mapping, Room")
#     print(n7line.generate_desc_mixed()) # room 1 is connected to the blue room
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(f"What is the shortest path from room {nodes_room[0]} to room {nodes_room[1]}?")

#     print("\nnDesc, Mapping, Color")
#     print(n7line.generate_desc_mixed()) # room 1 is connected to the blue room
#     print(n7line.describe_room_color_mapping()) # room 1 is red 
#     print(f"What is the shortest path from the {nodes_color[0]} room to the {nodes_color[1]} room?")

