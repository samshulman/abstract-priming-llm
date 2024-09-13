import json
import numpy as np
import graphs
import os

n7line_rooms = graphs.Graph()
for i in range (1, 8):
	n7line_rooms.add_node(i)
n7line_rooms.connect_nodes(1, 2)
n7line_rooms.connect_nodes(1, 3)
n7line_rooms.connect_nodes(2, 4)
n7line_rooms.connect_nodes(3, 5)
n7line_rooms.connect_nodes(4, 6)
n7line_rooms.connect_nodes(5, 7)
n7line_rooms_desc = n7line_rooms.generate_description_rooms()




# n7tree
n7tree_rooms = graphs.Graph()
for i in range (1, 8):
    n7tree_rooms.add_node(i)
n7tree_rooms.connect_nodes(1, 2)
n7tree_rooms.connect_nodes(1, 3)
n7tree_rooms.connect_nodes(2, 4)
n7tree_rooms.connect_nodes(2, 5)
n7tree_rooms.connect_nodes(3, 6)
n7tree_rooms.connect_nodes(3, 7)
n7tree_rooms_desc = n7tree_rooms.generate_description_rooms()


graph_names = ["n7line_rooms",  "n7tree_rooms"]
graph_list = [n7line_rooms, n7tree_rooms]
graph_dict = dict(zip(graph_names, graph_list))

graph_desc_list = [n7line_rooms_desc, n7tree_rooms_desc]
graph_desc_dict = dict(zip(graph_names, graph_desc_list))


def name_question(start, end):
  start = "room " + start
  end = "room " + end
  return f"What is the shortest path from {start} to {end}? Starting from {start}, please only list the room numbers in order, including {start}, separated by commas. Answer: "

def characteristic_question(start, end, color_list):
  start = "the " + color_list[int(start) -1] + " room"
  end = "the " + color_list[int(end) -1] + " room"
  return f"What is the shortest path from {start} to {end}? Starting from {start}, please only list the room numbers in order, including {start}, separated by commas. Answer: "

def abstract_desc(graph, color_list):
  color_desc = graph.generate_description_colors(color_list)
  room_desc = graph.generate_description_rooms()
  return color_desc + " " + room_desc

def path_desc(graph, color_list):
  color_desc = graph.generate_description_colors(color_list)
  room_desc = graph.generate_description_rooms()
  return room_desc + " " + color_desc

def mixed_desc(graph, color_list):
  color_desc = graph.generate_description_colors(color_list)
  mixed_desc = graph.generate_description_mixed(color_list)
  return color_desc + " " + mixed_desc

def abstract_desc_characteristic_question(graph, start, end, color_list):
  desc = abstract_desc(graph, color_list)
  question = characteristic_question(start, end, color_list)
  return desc + " " + question

def abstract_desc_name_question(graph, start, end, color_list):
  desc = abstract_desc(graph, color_list)
  question = name_question(start, end)
  return desc + " " + question

def path_desc_characteristic_question(graph, start, end, color_list):
  desc = path_desc(graph, color_list)
  question = characteristic_question(start, end, color_list)
  return desc + " " + question

def path_desc_name_question(graph, start, end, color_list):
  desc = path_desc(graph, color_list)
  question = name_question(start, end)
  return desc + " " + question

def mixed_desc_characteristic_question(graph, start, end, color_list):
  desc = mixed_desc(graph, color_list)
  question = characteristic_question(start, end, color_list)
  return desc + " " + question

def mixed_desc_name_question(graph, start, end, color_list):
  desc = mixed_desc(graph, color_list)
  question = name_question(start, end)
  return desc + " " + question


for graph_title in graph_names:
  for i in range(100):

    graph_name = graph_title

    file_path = f"{graph_name}_questions.jsonl"
    graph = graph_dict[graph_name]
    nodes = graph.select_random_nodes(2)
    start = nodes[0]
    end = nodes[1]
    
    if len(graph.find_shortest_path(start, end)) == 2:
      nodes = graph.select_random_nodes(2)
      start = nodes[0]
      end = nodes[1]

    shortest_path = graph.find_shortest_path(start, end)
    color_list = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]


    json_dict = {
                      "Graph": graph_name,

                      "abstract desc characteristic question": abstract_desc_characteristic_question(graph, start, end, color_list),
                      "abstract desc characteristic question answer": shortest_path,

                      "abstract desc name question": abstract_desc_name_question(graph, start, end, color_list),
                      "abstract desc name question answer": shortest_path,

                      "path desc characteristic question": path_desc_characteristic_question(graph, start, end, color_list),
                      "path desc characteristic question answer": shortest_path,

                      "path desc name question": path_desc_name_question(graph, start, end, color_list),
                      "path desc name question answer": shortest_path,

                      "mixed desc characteristic question": mixed_desc_characteristic_question(graph, start, end, color_list),
                      "mixed desc characteristic question answer": shortest_path,

                      "mixed desc name question": mixed_desc_name_question(graph, start, end, color_list),
                      "mixed desc name question answer": shortest_path,

                  }



    with open(file_path, 'a') as outfile:
          json_string = json.dumps(json_dict)
          outfile.write(json_string + '\n')