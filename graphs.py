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
        description = f"Imagine a home with {num_rooms} rooms. "
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

    def generate_description_flowers(self):
        num_rooms = len(self.nodes)
        description = f"Imagine a garden with {num_rooms} sections of flowers. "
        room_descriptions = []
        for node, connections in self.nodes.items():
            connections_desc_list = []
            for conn in connections:
                conn = conn.lower()
                connections_desc_list.append(f"the {conn} section")

            if len(connections_desc_list) > 1:
                connections_desc = ', '.join(connections_desc_list[:-1]) + f" and {connections_desc_list[-1]}"
            elif connections_desc_list:
                connections_desc = connections_desc_list[0] # one connection
            else:
                connections_desc = 'no other sections' # no connections
            node = node.lower()
            room_descriptions.append(f"The {node} section is connected to {connections_desc}.")

        description += ' '.join(room_descriptions)
        return description


    def generate_description_friends(self):
        num_rooms = len(self.nodes)
        description = f"Imagine a group of {num_rooms} people. "
        room_descriptions = []
        for node, connections in self.nodes.items():
            connections_desc_list = []
            for conn in connections:
                connections_desc_list.append(conn)

            if len(connections_desc_list) > 1:
                connections_desc = ', '.join(connections_desc_list[:-1]) + f" and {connections_desc_list[-1]}"
            elif connections_desc_list:
                connections_desc = connections_desc_list[0] # one connection
            else:
                connections_desc = 'no other people' # no connections
            room_descriptions.append(f"{node} is friends with {connections_desc}.")

        description += ' '.join(room_descriptions)
        return description


    def n_step_path(self, start, end, n_steps):
        from collections import deque
        queue = deque([(start, 0)])  # queue of tuples (current node, current depth)
        visited = set()  # to keep track of visited nodes

        while queue:
            current_node, depth = queue.popleft()

            if depth > n_steps:
                continue  # Skip this level if depth exceeded n_steps

            if current_node == end and depth == n_steps:
                return True  # Found a path with exactly n_steps

            if current_node not in visited or depth < n_steps:
                visited.add(current_node)
                for neighbor in self.nodes.get(current_node, []):
                    if neighbor not in visited or depth + 1 <= n_steps:
                        queue.append((neighbor, depth + 1))

        return False  # No n-step path found

    def select_random_nodes(self, num_nodes):
        node_keys = list(self.nodes.keys())  # Get all node keys as a list
        if len(node_keys) < num_nodes:
            print("Not enough nodes to select", num_nodes, "unique items.")
            return None
        return np.random.choice(node_keys, num_nodes, replace=False)  # Randomly choose without replacement


    def is_path_valid(self, path_list):
        if not path_list:
            return False  # empty path cannot be valid
        for i in range(len(path_list) - 1):
            node = str(path_list[i]) # convert path string to node
            next_node = str(path_list[i+1])
            if node not in self.nodes or next_node not in self.nodes[node]: # if node isn't a node or next node isn't connected
                return False
        return True