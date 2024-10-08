import numpy as np

class Graph:
    def __init__(self):
        self.nodes = {}  # dictionary to store the adjacency list

    def add_node(self, node):
        node = str(node)
        if node not in self.nodes:
            self.nodes[node] = []
        else:
            print(f"Node {node} already exists in the graph.")

    def connect_nodes(self, node1, node2):
        node1 = str(node1)
        node2 = str(node2)
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1].append(node2)
            self.nodes[node2].append(node1)  # For undirected graph, add both connections
        else:
            print(f"One or both of the nodes {node1}, {node2} do not exist.")

    def find_shortest_path(self, start_node, end_node):
        from collections import deque

        # Convert start_node and end_node to strings
        start_node = str(start_node)
        end_node = str(end_node)

        # Convert all keys in self.nodes to strings
        self.nodes = {str(k): [str(n) for n in v] for k, v in self.nodes.items()}

        if start_node not in self.nodes:
            print("Start node does not exist.")
            return None

        if end_node not in self.nodes:
            print("End node does not exist.")
            return None

        queue = deque([(start_node, [start_node])])
        visited = set()

        while queue:
            current_node, path = queue.popleft()

            if current_node == end_node:
                return path

            if current_node not in visited:
                visited.add(current_node)
                for neighbor in self.nodes[current_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        print("No path found")
        return None

    def display_graph(self):
        for node, connections in self.nodes.items():
            print(f"Node {node} has connections to: {connections}")


    def generate_description_rooms(self):
        num_rooms = len(self.nodes)
        description = ""
        room_descriptions = []
        for node, connections in self.nodes.items():
            node_desc = f"Room {node}"
            connections_desc_list = []
            for conn in connections:
                connections_desc_list.append(f"Room {conn}")

            if len(connections_desc_list) > 1:
                connections_desc = ', '.join(connections_desc_list[:-1]) + f" and {connections_desc_list[-1]}"
            elif connections_desc_list:
                connections_desc = connections_desc_list[0] # one connection
            else:
                connections_desc = 'no other rooms' # no connections
            room_descriptions.append(f"{node_desc} is connected to {connections_desc}.")

        description += ' '.join(room_descriptions)
        return description
    
    def generate_description_colors(self, color_list):
        num_rooms = len(self.nodes)
        if num_rooms != len(color_list):
            raise ValueError("The number of colors must match the number of rooms")
        room_color_descriptions = ""
        nodes = self.nodes.keys()
        counter = 0
        for node in nodes:
            color = color_list[counter]
            room_color_descriptions+= ''.join(f"Room {node} is {color}. ")
            counter+=1
        return room_color_descriptions
    
    def generate_description_mixed(self, color_list):
        num_rooms = len(self.nodes)
        if num_rooms != len(color_list):
            raise ValueError("The number of colors must match the number of rooms")

        description = ""
        room_descriptions = []
        color_dict = {i+1: color for i, color in enumerate(color_list)}

        for node, connections in self.nodes.items():
            # Randomly choose between room number and color for the current room
            rand = np.random.rand()
            current_room_desc = f"Room {node}" if rand > 0.5 else f"The {color_dict[int(node)]} room"
            
            connections_desc_list = []
            for conn in connections:
                # Randomly choose between room number and color for connected rooms
                rand = np.random.rand()
                conn_desc = f"Room {conn}" if rand > 0.5 else f"the {color_dict[int(conn)]} room"
                connections_desc_list.append(conn_desc)

            if len(connections_desc_list) > 1:
                connections_desc = ', '.join(connections_desc_list[:-1]) + f" and {connections_desc_list[-1]}"
            elif connections_desc_list:
                connections_desc = connections_desc_list[0]  # one connection
            else:
                connections_desc = 'no other rooms'  # no connections
            
            room_descriptions.append(f"{current_room_desc} is connected to {connections_desc}.")

        description = ' '.join(room_descriptions)
        return description

    def select_random_nodes(self, num_nodes):
        node_keys = list(self.nodes.keys())  # Get all node keys as a list
        if len(node_keys) < num_nodes:
            print("Not enough nodes to select", num_nodes, "unique items.")
            return None
        return np.random.choice(node_keys, num_nodes, replace=False)  # Randomly choose without replacement


n7line_rooms = Graph()
for i in range (1, 8):
	n7line_rooms.add_node(i)
n7line_rooms.connect_nodes(1, 2)
n7line_rooms.connect_nodes(1, 3)
n7line_rooms.connect_nodes(2, 4)
n7line_rooms.connect_nodes(3, 5)
n7line_rooms.connect_nodes(4, 6)
n7line_rooms.connect_nodes(5, 7)
n7line_rooms_desc = n7line_rooms.generate_description_rooms()
color_list = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

color_desc = n7line_rooms.generate_description_mixed(color_list)
print(color_desc)