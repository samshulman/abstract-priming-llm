import json
import numpy as np
import graphs
import os

n7line = graphs.Graph()
n7line.add_node('A', 'red', 1)
n7line.add_node('B', 'blue', 2)
n7line.add_node('C', 'green', 3)
n7line.add_node('D', 'yellow', 4)
n7line.add_node('E', 'purple', 5)
n7line.add_node('F', 'orange', 6)
n7line.add_node('G', 'pink', 7)
n7line.add_edge('A', 'B')
n7line.add_edge('A', 'C')
n7line.add_edge('B', 'D')
n7line.add_edge('C', 'E')
n7line.add_edge('D', 'F')
n7line.add_edge('E', 'G')

n7tree = graphs.Graph()
n7tree.add_node('A', 'red', 1)
n7tree.add_node('B', 'blue', 2)
n7tree.add_node('C', 'green', 3)
n7tree.add_node('D', 'yellow', 4)
n7tree.add_node('E', 'purple', 5)
n7tree.add_node('F', 'orange', 6)
n7tree.add_node('G', 'pink', 7)
n7tree.add_edge('A', 'B')
n7tree.add_edge('A', 'C')
n7tree.add_edge('B', 'D')
n7tree.add_edge('C', 'E')
n7tree.add_edge('B', 'F')
n7tree.add_edge('C', 'G')

n7fork = graphs.Graph()
n7fork.add_node('A', 'red', 1)
n7fork.add_node('B', 'blue', 2)
n7fork.add_node('C', 'green', 3)
n7fork.add_node('D', 'yellow', 4)
n7fork.add_node('E', 'purple', 5)
n7fork.add_node('F', 'orange', 6)
n7fork.add_node('G', 'pink', 7)
n7fork.add_edge('A', 'B')
n7fork.add_edge('A', 'D')
n7fork.add_edge('A', 'F')
n7fork.add_edge('B', 'C')
n7fork.add_edge('D', 'E')
n7fork.add_edge('F', 'G')

n7star = graphs.Graph()
n7star.add_node('A', 'red', 1)
n7star.add_node('B', 'blue', 2)
n7star.add_node('C', 'green', 3)
n7star.add_node('D', 'yellow', 4)
n7star.add_node('E', 'purple', 5)
n7star.add_node('F', 'orange', 6)
n7star.add_node('G', 'pink', 7)
n7star.add_edge('A', 'B')
n7star.add_edge('A', 'C')
n7star.add_edge('A', 'F')
n7star.add_edge('A', 'E')
n7star.add_edge('B', 'D')
n7star.add_edge('F', 'G')

n7bone = graphs.Graph()
n7bone.add_node('A', 'red', 1)
n7bone.add_node('B', 'blue', 2)
n7bone.add_node('C', 'green', 3)
n7bone.add_node('D', 'yellow', 4)
n7bone.add_node('E', 'purple', 5)
n7bone.add_node('F', 'orange', 6)
n7bone.add_node('G', 'pink', 7)
n7bone.add_edge('A', 'B')
n7bone.add_edge('A', 'C')
n7bone.add_edge('A', 'D')
n7bone.add_edge('D', 'F')
n7bone.add_edge('D', 'G')
n7bone.add_edge('B', 'E')


# double the graphs for consistent questions

n7line_double = graphs.Graph()
n7line_double.add_node('A', 'red', 1)
n7line_double.add_node('B', 'blue', 2)
n7line_double.add_node('C', 'green', 3)
n7line_double.add_node('D', 'yellow', 4)
n7line_double.add_node('E', 'purple', 5)
n7line_double.add_node('F', 'orange', 6)
n7line_double.add_node('G', 'pink', 7)
n7line_double.add_edge('A', 'B')
n7line_double.add_edge('A', 'C')
n7line_double.add_edge('B', 'D')
n7line_double.add_edge('C', 'E')
n7line_double.add_edge('D', 'F')
n7line_double.add_edge('E', 'G')
n7line_double.add_node('H', 'turquoise', 8)
n7line_double.add_node('I', 'cyan', 9)
n7line_double.add_node('J', 'magenta', 10)
n7line_double.add_node('K', 'indigo', 11)
n7line_double.add_node('L', 'navy', 12)
n7line_double.add_node('M', 'beige', 13)
n7line_double.add_node('N', 'grey', 14)
n7line_double.add_edge('H', 'I')
n7line_double.add_edge('H', 'J')
n7line_double.add_edge('I', 'K')
n7line_double.add_edge('J', 'L')
n7line_double.add_edge('K', 'M')
n7line_double.add_edge('L', 'N')

n7tree_double = graphs.Graph()
n7tree_double.add_node('A', 'red', 1)
n7tree_double.add_node('B', 'blue', 2)
n7tree_double.add_node('C', 'green', 3)
n7tree_double.add_node('D', 'yellow', 4)
n7tree_double.add_node('E', 'purple', 5)
n7tree_double.add_node('F', 'orange', 6)
n7tree_double.add_node('G', 'pink', 7)
n7tree_double.add_edge('A', 'B')
n7tree_double.add_edge('A', 'C')
n7tree_double.add_edge('B', 'D')
n7tree_double.add_edge('C', 'E')
n7tree_double.add_edge('B', 'F')
n7tree_double.add_edge('C', 'G')
n7tree_double.add_node('H', 'turquoise', 8)
n7tree_double.add_node('I', 'cyan', 9)
n7tree_double.add_node('J', 'magenta', 10)
n7tree_double.add_node('K', 'indigo', 11)
n7tree_double.add_node('L', 'navy', 12)
n7tree_double.add_node('M', 'beige', 13)
n7tree_double.add_node('N', 'grey', 14)
n7tree_double.add_edge('H', 'I')
n7tree_double.add_edge('H', 'J')
n7tree_double.add_edge('I', 'K')
n7tree_double.add_edge('J', 'L')
n7tree_double.add_edge('I', 'M')
n7tree_double.add_edge('J', 'N')

n7fork_double = graphs.Graph()
n7fork_double.add_node('A', 'red', 1)
n7fork_double.add_node('B', 'blue', 2)
n7fork_double.add_node('C', 'green', 3)
n7fork_double.add_node('D', 'yellow', 4)
n7fork_double.add_node('E', 'purple', 5)
n7fork_double.add_node('F', 'orange', 6)
n7fork_double.add_node('G', 'pink', 7)
n7fork_double.add_edge('A', 'B')
n7fork_double.add_edge('A', 'D')
n7fork_double.add_edge('A', 'F')
n7fork_double.add_edge('B', 'C')
n7fork_double.add_edge('D', 'E')
n7fork_double.add_edge('F', 'G')
n7fork_double.add_node('H', 'turquoise', 8)
n7fork_double.add_node('I', 'cyan', 9)
n7fork_double.add_node('J', 'magenta', 10)
n7fork_double.add_node('K', 'indigo', 11)
n7fork_double.add_node('L', 'navy', 12)
n7fork_double.add_node('M', 'beige', 13)
n7fork_double.add_node('N', 'grey', 14)
n7fork_double.add_edge('H', 'I')
n7fork_double.add_edge('H', 'K')
n7fork_double.add_edge('H', 'M')
n7fork_double.add_edge('I', 'J')
n7fork_double.add_edge('K', 'L')
n7fork_double.add_edge('M', 'N')

n7star_double = graphs.Graph()
n7star_double.add_node('A', 'red', 1)
n7star_double.add_node('B', 'blue', 2)
n7star_double.add_node('C', 'green', 3)
n7star_double.add_node('D', 'yellow', 4)
n7star_double.add_node('E', 'purple', 5)
n7star_double.add_node('F', 'orange', 6)
n7star_double.add_node('G', 'pink', 7)
n7star_double.add_edge('A', 'B')
n7star_double.add_edge('A', 'C')
n7star_double.add_edge('A', 'F')
n7star_double.add_edge('A', 'E')
n7star_double.add_edge('B', 'D')
n7star_double.add_edge('F', 'G')
n7star_double.add_node('H', 'turquoise', 8)
n7star_double.add_node('I', 'cyan', 9)
n7star_double.add_node('J', 'magenta', 10)
n7star_double.add_node('K', 'indigo', 11)
n7star_double.add_node('L', 'navy', 12)
n7star_double.add_node('M', 'beige', 13)
n7star_double.add_node('N', 'grey', 14)
n7star_double.add_edge('H', 'I')
n7star_double.add_edge('H', 'J')
n7star_double.add_edge('H', 'F')
n7star_double.add_edge('H', 'L')
n7star_double.add_edge('I', 'K')
n7star_double.add_edge('M', 'N')

n7bone_double = graphs.Graph()
n7bone_double.add_node('A', 'red', 1)
n7bone_double.add_node('B', 'blue', 2)
n7bone_double.add_node('C', 'green', 3)
n7bone_double.add_node('D', 'yellow', 4)
n7bone_double.add_node('E', 'purple', 5)
n7bone_double.add_node('F', 'orange', 6)
n7bone_double.add_node('G', 'pink', 7)
n7bone_double.add_edge('A', 'B')
n7bone_double.add_edge('A', 'C')
n7bone_double.add_edge('A', 'D')
n7bone_double.add_edge('D', 'F')
n7bone_double.add_edge('D', 'G')
n7bone_double.add_edge('B', 'E')
n7bone_double.add_node('H', 'turquoise', 8)
n7bone_double.add_node('I', 'cyan', 9)
n7bone_double.add_node('J', 'magenta', 10)
n7bone_double.add_node('K', 'indigo', 11)
n7bone_double.add_node('L', 'navy', 12)
n7bone_double.add_node('M', 'beige', 13)
n7bone_double.add_node('N', 'grey', 14)
n7bone_double.add_edge('H', 'I')
n7bone_double.add_edge('H', 'J')
n7bone_double.add_edge('H', 'K')
n7bone_double.add_edge('K', 'M')
n7bone_double.add_edge('K', 'N')
n7bone_double.add_edge('I', 'L')

graphs = [n7line, n7tree, n7fork, n7star, n7bone]
graphs_double = [n7line_double, n7tree_double, n7fork_double, n7star_double, n7bone_double]

graph_strings = ['n7line', 'n7tree', 'n7fork', 'n7star', 'n7bone']
graph_strings_double = ['n7line_double', 'n7tree_double', 'n7fork_double', 'n7star_double', 'n7bone_double']

for i, selected_graph in enumerate(graphs):
    
  for j in range(100):
    graph = selected_graph.generate_new_graph_with_different_labels()

    nodes_room = graph.select_two_non_adjacent_nodes_with_path('room')
    nodes_color = graph.select_two_non_adjacent_nodes_with_path('color')
    shortest_path_room = graph.shortest_path_room(nodes_room[0], nodes_room[1])
    shortest_path_color = graph.shortest_path_color(nodes_color[0], nodes_color[1])
    
    mapping = graph.describe_room_color_mapping()
    room_desc = graph.generate_desc_room()
    color_desc = graph.generate_desc_color()
    mixed_desc = graph.generate_desc_mixed()
    room_question = f"What is the shortest path from room {nodes_room[0]} to room {nodes_room[1]}? Starting from room {nodes_room[0]}, please only list the room numbers in order, including {nodes_room[0]}, separated by commas. Answer: "
    color_question = f"What is the shortest path from the {nodes_color[0]} room to the {nodes_color[1]} room? Starting with {nodes_color[0]}, please only list the colors of the rooms in order, including {nodes_color[0]}, separated by commas. Answer: "
    

    file_path = f"{graph_strings[i]}_questions.jsonl"

    json_dict = {
                  "Graph": graph_strings[i],


                  "Mapping, Room Desc, Room Question": mapping + " " + room_desc + " " + room_question,
                  "Mapping, Room Desc, Room Question Answer": shortest_path_room,
                  
                  "Mapping, Color Desc, Color Question": mapping + " " + color_desc + " " + color_question,
                  "Mapping, Color Desc, Color Question Answer": shortest_path_color,

                  "Room Desc, Mapping, Room Question": room_desc + " " + mapping + " " + room_question,
                  "Room Desc, Mapping, Room Question Answer": shortest_path_room,
                  
                  "Color Desc, Mapping, Color Question": color_desc + " " + mapping + " " + color_question,
                  "Color Desc, Mapping, Color Question Answer": shortest_path_color,


                  "Mapping, Color Desc, Room Question": mapping + " " + color_desc + " " + room_question,
                  "Mapping, Color Desc, Room Question Answer": shortest_path_room,
                  
                  "Mapping, Room Desc, Color Question": mapping + " " + room_desc + " " + color_question,
                  "Mapping, Room Desc, Color Question Answer": shortest_path_color,

                  "Color Desc, Mapping, Room Question": color_desc + " " + mapping + " " + room_question,
                  "Color Desc, Mapping, Room Question Answer": shortest_path_room,

                  "Room Desc, Mapping, Color Question": room_desc + " " + mapping + " " + color_question,
                  "Room Desc, Mapping, Color Question Answer": shortest_path_color,


                  "Mapping, Mixed Desc, Room Question": mapping + " " + mixed_desc + " " + room_question,
                  "Mapping, Mixed Desc, Room Question Answer": shortest_path_room,
                  
                  "Mapping, Mixed Desc, Color Question": mapping + " " + mixed_desc + " " + color_question,
                  "Mapping, Mixed Desc, Color Question Answer": shortest_path_color,

                  "Mixed Desc, Mapping, Room Question": mixed_desc + " " + mapping + " " + room_question,
                  "Mixed Desc, Mapping, Room Question Answer": shortest_path_room,
                  
                  "Mixed Desc, Mapping, Color Question": mixed_desc + " " + mapping + " " + color_question,
                  "Mixed Desc, Mapping, Color Question Answer": shortest_path_color,

                }


    with open(file_path, 'a') as outfile:
          json_string = json.dumps(json_dict)
          outfile.write(json_string + '\n')