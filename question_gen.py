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
# print(n7line_rooms_desc)

n7line_friends = graphs.Graph()
n7line_friends.add_node("Anne")
n7line_friends.add_node("Bob")
n7line_friends.add_node("Charles")
n7line_friends.add_node("Deborah")
n7line_friends.add_node("Emily")
n7line_friends.add_node("Mary")
n7line_friends.add_node("Kelly")
n7line_friends.connect_nodes("Anne", "Bob")
n7line_friends.connect_nodes("Anne", "Charles")
n7line_friends.connect_nodes("Bob", "Deborah")
n7line_friends.connect_nodes("Charles", "Emily")
n7line_friends.connect_nodes("Deborah", "Mary")
n7line_friends.connect_nodes("Emily", "Kelly")
n7line_friends_desc = n7line_friends.generate_description_friends()
# print(n7line_friends_desc)

n7line_flowers = graphs.Graph()
n7line_flowers.add_node("Rose")
n7line_flowers.add_node("Tulip")
n7line_flowers.add_node("Lavender")
n7line_flowers.add_node("Sunflower")
n7line_flowers.add_node("Daffodil")
n7line_flowers.add_node("Peony")
n7line_flowers.add_node("Geranium")
n7line_flowers.connect_nodes("Rose", "Tulip")
n7line_flowers.connect_nodes("Rose", "Lavender")
n7line_flowers.connect_nodes("Tulip", "Sunflower")
n7line_flowers.connect_nodes("Lavender", "Daffodil")
n7line_flowers.connect_nodes("Sunflower", "Peony")
n7line_flowers.connect_nodes("Daffodil", "Geranium")
n7line_flowers_desc = n7line_flowers.generate_description_flowers()
# print(n7line_flowers_desc)



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
# print(n7tree_rooms_desc)

n7tree_friends = graphs.Graph()
n7tree_friends.add_node("Anne")
n7tree_friends.add_node("Bob")
n7tree_friends.add_node("Charles")
n7tree_friends.add_node("Deborah")
n7tree_friends.add_node("Emily")
n7tree_friends.add_node("Mary")
n7tree_friends.add_node("Kelly")
n7tree_friends.connect_nodes("Anne", "Bob")
n7tree_friends.connect_nodes("Anne", "Charles")
n7tree_friends.connect_nodes("Bob", "Deborah")
n7tree_friends.connect_nodes("Bob", "Emily")
n7tree_friends.connect_nodes("Charles", "Mary")
n7tree_friends.connect_nodes("Charles", "Kelly")
n7tree_friends_desc = n7tree_friends.generate_description_friends()
# print(n7tree_friends_desc)

n7tree_flowers = graphs.Graph()
n7tree_flowers.add_node("Rose")
n7tree_flowers.add_node("Tulip")
n7tree_flowers.add_node("Lavender")
n7tree_flowers.add_node("Sunflower")
n7tree_flowers.add_node("Daffodil")
n7tree_flowers.add_node("Peony")
n7tree_flowers.add_node("Geranium")
n7tree_flowers.connect_nodes("Rose", "Tulip")
n7tree_flowers.connect_nodes("Rose", "Lavender")
n7tree_flowers.connect_nodes("Tulip", "Sunflower")
n7tree_flowers.connect_nodes("Tulip", "Daffodil")
n7tree_flowers.connect_nodes("Lavender", "Peony")
n7tree_flowers.connect_nodes("Lavender", "Geranium")
n7tree_flowers_desc = n7tree_flowers.generate_description_flowers()
# print(n7tree_flowers_desc)

# n13line
n13line_rooms = graphs.Graph()
for i in range (1, 14):
	n13line_rooms.add_node(i)
n13line_rooms.connect_nodes(1, 2)
n13line_rooms.connect_nodes(1, 3)
n13line_rooms.connect_nodes(2, 4)
n13line_rooms.connect_nodes(4, 6)
n13line_rooms.connect_nodes(6, 8)
n13line_rooms.connect_nodes(8, 10)
n13line_rooms.connect_nodes(10, 12)
n13line_rooms.connect_nodes(3, 5)
n13line_rooms.connect_nodes(5, 7)
n13line_rooms.connect_nodes(7, 9)
n13line_rooms.connect_nodes(9, 11)
n13line_rooms.connect_nodes(11, 13)
n13line_rooms_desc = n13line_rooms.generate_description_rooms()
# print(n13line_rooms_desc)

n13line_friends = graphs.Graph()
n13line_friends.add_node("Anne")
n13line_friends.add_node("Bob")
n13line_friends.add_node("Charles")
n13line_friends.add_node("Deborah")
n13line_friends.add_node("Emily")
n13line_friends.add_node("Mary")
n13line_friends.add_node("Kelly")
n13line_friends.add_node("Sam")
n13line_friends.add_node("John")
n13line_friends.add_node("George")
n13line_friends.add_node("Fred")
n13line_friends.add_node("Harrison")
n13line_friends.add_node("Isabelle")
n13line_friends.connect_nodes("Anne", "Bob")
n13line_friends.connect_nodes("Anne", "Charles")
n13line_friends.connect_nodes("Bob", "Deborah")
n13line_friends.connect_nodes("Deborah", "Mary")
n13line_friends.connect_nodes("Mary", "Sam")
n13line_friends.connect_nodes("Sam", "George")
n13line_friends.connect_nodes("George", "Harrison")
n13line_friends.connect_nodes("Charles", "Emily")
n13line_friends.connect_nodes("Emily", "Kelly")
n13line_friends.connect_nodes("Kelly", "John")
n13line_friends.connect_nodes("John", "Fred")
n13line_friends.connect_nodes("Fred", "Isabelle")
n13line_friends_desc = n13line_friends.generate_description_friends()
# print(n13line_friends_desc)


n13line_flowers = graphs.Graph()
n13line_flowers.add_node("Rose")
n13line_flowers.add_node("Tulip")
n13line_flowers.add_node("Lavender")
n13line_flowers.add_node("Sunflower")
n13line_flowers.add_node("Daffodil")
n13line_flowers.add_node("Peony")
n13line_flowers.add_node("Geranium")
n13line_flowers.add_node("Carnation")
n13line_flowers.add_node("Daisy")
n13line_flowers.add_node("Orchid")
n13line_flowers.add_node("Iris")
n13line_flowers.add_node("Poppy")
n13line_flowers.add_node("Marigold")
n13line_flowers.connect_nodes("Rose", "Tulip")
n13line_flowers.connect_nodes("Rose","Lavender")
n13line_flowers.connect_nodes("Tulip", "Sunflower")
n13line_flowers.connect_nodes("Sunflower", "Peony")
n13line_flowers.connect_nodes("Peony", "Carnation")
n13line_flowers.connect_nodes("Carnation", "Orchid")
n13line_flowers.connect_nodes("Orchid", "Poppy")
n13line_flowers.connect_nodes("Lavender", "Daffodil")
n13line_flowers.connect_nodes("Daffodil", "Geranium")
n13line_flowers.connect_nodes("Geranium", "Daisy")
n13line_flowers.connect_nodes("Daisy", "Iris")
n13line_flowers.connect_nodes("Iris", "Marigold")
n13line_flowers_desc = n13line_flowers.generate_description_flowers()
# print(n13line_flowers_desc)




# n15star
n15star_rooms = graphs.Graph()
for i in range (1, 16):
	n15star_rooms.add_node(i)
n15star_rooms.connect_nodes(1, 2)
n15star_rooms.connect_nodes(1, 3)
n15star_rooms.connect_nodes(1, 4)
n15star_rooms.connect_nodes(1, 5)
n15star_rooms.connect_nodes(2, 3)
n15star_rooms.connect_nodes(2, 4)
n15star_rooms.connect_nodes(2, 5)
n15star_rooms.connect_nodes(3, 4)
n15star_rooms.connect_nodes(3, 5)
n15star_rooms.connect_nodes(4, 6)
n15star_rooms.connect_nodes(6, 7)
n15star_rooms.connect_nodes(6, 8)
n15star_rooms.connect_nodes(6, 9)
n15star_rooms.connect_nodes(7, 8)
n15star_rooms.connect_nodes(7, 9)
n15star_rooms.connect_nodes(7, 10)
n15star_rooms.connect_nodes(8, 9)
n15star_rooms.connect_nodes(8, 10)
n15star_rooms.connect_nodes(9, 10)
n15star_rooms.connect_nodes(10, 11)
n15star_rooms.connect_nodes(11, 12)
n15star_rooms.connect_nodes(11, 13)
n15star_rooms.connect_nodes(11, 14)
n15star_rooms.connect_nodes(12, 13)
n15star_rooms.connect_nodes(12, 14)
n15star_rooms.connect_nodes(12, 15)
n15star_rooms.connect_nodes(13, 14)
n15star_rooms.connect_nodes(13, 15)
n15star_rooms.connect_nodes(14, 15)
n15star_rooms.connect_nodes(5, 15)
n15star_rooms_desc = n15star_rooms.generate_description_rooms()
# print(n15star_rooms_desc)

n15star_friends = graphs.Graph()
n15star_friends.add_node("Anne")
n15star_friends.add_node("Bob")
n15star_friends.add_node("Charles")
n15star_friends.add_node("Deborah")
n15star_friends.add_node("Emily")
n15star_friends.add_node("Mary")
n15star_friends.add_node("Kelly")
n15star_friends.add_node("Sam")
n15star_friends.add_node("John")
n15star_friends.add_node("George")
n15star_friends.add_node("Fred")
n15star_friends.add_node("Harrison")
n15star_friends.add_node("Isabelle")
n15star_friends.add_node("Lauren")
n15star_friends.add_node("Ned")
n15star_friends.connect_nodes("Anne", "Bob")
n15star_friends.connect_nodes("Anne", "Charles")
n15star_friends.connect_nodes("Anne", "Deborah")
n15star_friends.connect_nodes("Anne", "Emily")
n15star_friends.connect_nodes("Bob", "Charles")
n15star_friends.connect_nodes("Bob", "Deborah")
n15star_friends.connect_nodes("Bob", "Emily")
n15star_friends.connect_nodes("Charles", "Deborah")
n15star_friends.connect_nodes("Charles", "Emily")
n15star_friends.connect_nodes("Deborah", "Mary")
n15star_friends.connect_nodes("Mary", "Kelly")
n15star_friends.connect_nodes("Mary", "Sam")
n15star_friends.connect_nodes("Mary", "John")
n15star_friends.connect_nodes("Kelly", "Sam")
n15star_friends.connect_nodes("Kelly", "John")
n15star_friends.connect_nodes("Kelly", "George")
n15star_friends.connect_nodes("Sam", "John")
n15star_friends.connect_nodes("Sam", "George")
n15star_friends.connect_nodes("John", "George")
n15star_friends.connect_nodes("George", "Fred")
n15star_friends.connect_nodes("Fred", "Harrison")
n15star_friends.connect_nodes("Fred", "Isabelle")
n15star_friends.connect_nodes("Fred", "Lauren")
n15star_friends.connect_nodes("Harrison", "Isabelle")
n15star_friends.connect_nodes("Harrison", "Lauren")
n15star_friends.connect_nodes("Harrison", "Ned")
n15star_friends.connect_nodes("Isabelle", "Lauren")
n15star_friends.connect_nodes("Isabelle", "Ned")
n15star_friends.connect_nodes("Lauren", "Ned")
n15star_friends.connect_nodes("Emily", "Ned")
n15star_friends_desc = n15star_friends.generate_description_friends()
# print(n15star_friends_desc)

n15star_flowers = graphs.Graph()
n15star_flowers.add_node("Rose")
n15star_flowers.add_node("Tulip")
n15star_flowers.add_node("Lavender")
n15star_flowers.add_node("Sunflower")
n15star_flowers.add_node("Daffodil")
n15star_flowers.add_node("Peony")
n15star_flowers.add_node("Geranium")
n15star_flowers.add_node("Carnation")
n15star_flowers.add_node("Daisy")
n15star_flowers.add_node("Orchid")
n15star_flowers.add_node("Iris")
n15star_flowers.add_node("Poppy")
n15star_flowers.add_node("Marigold")
n15star_flowers.add_node("Lily")
n15star_flowers.add_node("Hyacinth")
n15star_flowers.connect_nodes("Rose", "Tulip")
n15star_flowers.connect_nodes("Rose", "Lavender")
n15star_flowers.connect_nodes("Rose", "Sunflower")
n15star_flowers.connect_nodes("Rose", "Daffodil")
n15star_flowers.connect_nodes("Tulip", "Lavender")
n15star_flowers.connect_nodes("Tulip", "Sunflower")
n15star_flowers.connect_nodes("Tulip", "Daffodil")
n15star_flowers.connect_nodes("Lavender", "Sunflower")
n15star_flowers.connect_nodes("Lavender", "Daffodil")
n15star_flowers.connect_nodes("Sunflower", "Peony")
n15star_flowers.connect_nodes("Peony", "Geranium")
n15star_flowers.connect_nodes("Peony", "Carnation")
n15star_flowers.connect_nodes("Peony", "Daisy")
n15star_flowers.connect_nodes("Geranium", "Carnation")
n15star_flowers.connect_nodes("Geranium", "Daisy")
n15star_flowers.connect_nodes("Geranium", "Orchid")
n15star_flowers.connect_nodes("Carnation", "Daisy")
n15star_flowers.connect_nodes("Carnation", "Orchid")
n15star_flowers.connect_nodes("Daisy", "Orchid")
n15star_flowers.connect_nodes("Orchid", "Iris")
n15star_flowers.connect_nodes("Iris", "Poppy")
n15star_flowers.connect_nodes("Iris", "Marigold")
n15star_flowers.connect_nodes("Iris", "Lily")
n15star_flowers.connect_nodes("Poppy", "Marigold")
n15star_flowers.connect_nodes("Poppy", "Lily")
n15star_flowers.connect_nodes("Poppy", "Hyacinth")
n15star_flowers.connect_nodes("Marigold", "Lily")
n15star_flowers.connect_nodes("Marigold", "Hyacinth")
n15star_flowers.connect_nodes("Lily", "Hyacinth")
n15star_flowers.connect_nodes("Daffodil", "Hyacinth")
n15star_flowers_desc = n15star_flowers.generate_description_flowers()
# print(n15star_flowers_desc)



# n16cluster

n16cluster_rooms = graphs.Graph()
for i in range (1, 17):
	n16cluster_rooms.add_node(i)
n16cluster_rooms.connect_nodes(1, 2)
n16cluster_rooms.connect_nodes(1, 3)
n16cluster_rooms.connect_nodes(1, 4)
n16cluster_rooms.connect_nodes(1, 7)
n16cluster_rooms.connect_nodes(2, 3)
n16cluster_rooms.connect_nodes(2, 4)
n16cluster_rooms.connect_nodes(2, 14)
n16cluster_rooms.connect_nodes(3, 4)
n16cluster_rooms.connect_nodes(3, 16)
n16cluster_rooms.connect_nodes(4, 5)
n16cluster_rooms.connect_nodes(5, 6)
n16cluster_rooms.connect_nodes(5, 7)
n16cluster_rooms.connect_nodes(5, 8)
n16cluster_rooms.connect_nodes(6, 7)
n16cluster_rooms.connect_nodes(6, 8)
n16cluster_rooms.connect_nodes(6, 11)
n16cluster_rooms.connect_nodes(7, 8)
n16cluster_rooms.connect_nodes(8, 9)
n16cluster_rooms.connect_nodes(9, 10)
n16cluster_rooms.connect_nodes(9, 11)
n16cluster_rooms.connect_nodes(9, 12)
n16cluster_rooms.connect_nodes(10, 11)
n16cluster_rooms.connect_nodes(10, 12)
n16cluster_rooms.connect_nodes(11, 12)
n16cluster_rooms.connect_nodes(12, 13)
n16cluster_rooms.connect_nodes(13, 14)
n16cluster_rooms.connect_nodes(13, 15)
n16cluster_rooms.connect_nodes(13, 16)
n16cluster_rooms.connect_nodes(14, 15)
n16cluster_rooms.connect_nodes(14, 16)
n16cluster_rooms.connect_nodes(15, 16)
n16cluster_rooms.connect_nodes(15, 10)
n16cluster_rooms_desc = n16cluster_rooms.generate_description_rooms()


n16cluster_friends = graphs.Graph()
n16cluster_friends.add_node("Anne")
n16cluster_friends.add_node("Bob")
n16cluster_friends.add_node("Charles")
n16cluster_friends.add_node("Deborah")
n16cluster_friends.add_node("Emily")
n16cluster_friends.add_node("Mary")
n16cluster_friends.add_node("Kelly")
n16cluster_friends.add_node("Sam")
n16cluster_friends.add_node("John")
n16cluster_friends.add_node("George")
n16cluster_friends.add_node("Fred")
n16cluster_friends.add_node("Harrison")
n16cluster_friends.add_node("Isabelle")
n16cluster_friends.add_node("Lauren")
n16cluster_friends.add_node("Ned")
n16cluster_friends.add_node("Olivia")
n16cluster_friends.connect_nodes("Anne", "Bob")
n16cluster_friends.connect_nodes("Anne", "Charles")
n16cluster_friends.connect_nodes("Anne", "Deborah")
n16cluster_friends.connect_nodes("Anne", "Kelly")
n16cluster_friends.connect_nodes("Bob", "Charles")
n16cluster_friends.connect_nodes("Bob", "Deborah")
n16cluster_friends.connect_nodes("Bob", "Lauren")
n16cluster_friends.connect_nodes("Charles", "Deborah")
n16cluster_friends.connect_nodes("Charles", "Olivia")
n16cluster_friends.connect_nodes("Deborah", "Emily")
n16cluster_friends.connect_nodes("Emily", "Mary")
n16cluster_friends.connect_nodes("Emily", "Kelly")
n16cluster_friends.connect_nodes("Emily", "Sam")
n16cluster_friends.connect_nodes("Mary", "Kelly")
n16cluster_friends.connect_nodes("Mary", "Sam")
n16cluster_friends.connect_nodes("Mary", "Fred")
n16cluster_friends.connect_nodes("Kelly", "Sam")
n16cluster_friends.connect_nodes("Sam", "John")
n16cluster_friends.connect_nodes("John", "George")
n16cluster_friends.connect_nodes("John", "Fred")
n16cluster_friends.connect_nodes("John", "Harrison")
n16cluster_friends.connect_nodes("George", "Fred")
n16cluster_friends.connect_nodes("George", "Harrison")
n16cluster_friends.connect_nodes("Fred", "Harrison")
n16cluster_friends.connect_nodes("Harrison", "Isabelle")
n16cluster_friends.connect_nodes("Isabelle", "Lauren")
n16cluster_friends.connect_nodes("Isabelle", "Ned")
n16cluster_friends.connect_nodes("Isabelle", "Olivia")
n16cluster_friends.connect_nodes("Lauren", "Ned")
n16cluster_friends.connect_nodes("Lauren", "Olivia")
n16cluster_friends.connect_nodes("Ned", "Olivia")
n16cluster_friends.connect_nodes("Ned", "George")
n16cluster_friends_desc = n16cluster_friends.generate_description_friends()


n16cluster_flowers = graphs.Graph()
n16cluster_flowers.add_node("Rose")
n16cluster_flowers.add_node("Tulip")
n16cluster_flowers.add_node("Lavender")
n16cluster_flowers.add_node("Sunflower")
n16cluster_flowers.add_node("Daffodil")
n16cluster_flowers.add_node("Peony")
n16cluster_flowers.add_node("Geranium")
n16cluster_flowers.add_node("Carnation")
n16cluster_flowers.add_node("Daisy")
n16cluster_flowers.add_node("Orchid")
n16cluster_flowers.add_node("Iris")
n16cluster_flowers.add_node("Poppy")
n16cluster_flowers.add_node("Marigold")
n16cluster_flowers.add_node("Lily")
n16cluster_flowers.add_node("Hyacinth")
n16cluster_flowers.add_node("Hydrangea")
n16cluster_flowers.connect_nodes("Rose", "Tulip")
n16cluster_flowers.connect_nodes("Rose", "Lavender")
n16cluster_flowers.connect_nodes("Rose", "Sunflower")
n16cluster_flowers.connect_nodes("Rose", "Geranium")
n16cluster_flowers.connect_nodes("Tulip", "Lavender")
n16cluster_flowers.connect_nodes("Tulip", "Sunflower")
n16cluster_flowers.connect_nodes("Tulip", "Lily")
n16cluster_flowers.connect_nodes("Lavender", "Sunflower")
n16cluster_flowers.connect_nodes("Lavender", "Hydrangea")
n16cluster_flowers.connect_nodes("Sunflower", "Daffodil")
n16cluster_flowers.connect_nodes("Daffodil", "Peony")
n16cluster_flowers.connect_nodes("Daffodil", "Geranium")
n16cluster_flowers.connect_nodes("Daffodil", "Carnation")
n16cluster_flowers.connect_nodes("Peony", "Geranium")
n16cluster_flowers.connect_nodes("Peony", "Carnation")
n16cluster_flowers.connect_nodes("Peony", "Iris")
n16cluster_flowers.connect_nodes("Geranium", "Carnation")
n16cluster_flowers.connect_nodes("Carnation", "Daisy")
n16cluster_flowers.connect_nodes("Daisy", "Orchid")
n16cluster_flowers.connect_nodes("Daisy", "Iris")
n16cluster_flowers.connect_nodes("Daisy", "Poppy")
n16cluster_flowers.connect_nodes("Orchid", "Iris")
n16cluster_flowers.connect_nodes("Orchid", "Poppy")
n16cluster_flowers.connect_nodes("Iris", "Poppy")
n16cluster_flowers.connect_nodes("Poppy", "Marigold")
n16cluster_flowers.connect_nodes("Marigold", "Lily")
n16cluster_flowers.connect_nodes("Marigold", "Hyacinth")
n16cluster_flowers.connect_nodes("Marigold", "Hydrangea")
n16cluster_flowers.connect_nodes("Lily", "Hyacinth")
n16cluster_flowers.connect_nodes("Lily", "Hydrangea")
n16cluster_flowers.connect_nodes("Hyacinth", "Hydrangea")
n16cluster_flowers.connect_nodes("Hyacinth", "Orchid")
n16cluster_flowers_desc = n16cluster_flowers.generate_description_flowers()



graph_names = ["n7line_rooms", "n7line_friends", "n7line_flowers", "n7tree_rooms", "n7tree_friends", "n7tree_flowers", "n13line_rooms", "n13line_friends", "n13line_flowers", "n15star_rooms", "n15star_friends", "n15star_flowers", "n16cluster_rooms", "n16cluster_friends", "n16cluster_flowers"]
graph_list = [n7line_rooms, n7line_friends, n7line_flowers, n7tree_rooms, n7tree_friends, n7tree_flowers, n13line_rooms, n13line_friends, n13line_flowers, n15star_rooms, n15star_friends, n15star_flowers,  n16cluster_rooms, n16cluster_friends, n16cluster_flowers]
graph_dict = dict(zip(graph_names, graph_list))

graph_desc_list = [n7line_rooms_desc, n7line_friends_desc, n7line_flowers_desc, n7tree_rooms_desc, n7tree_friends_desc, n7tree_flowers_desc, n13line_rooms_desc, n13line_friends_desc, n13line_flowers_desc, n15star_rooms_desc, n15star_friends_desc, n15star_flowers_desc, n16cluster_rooms_desc, n16cluster_friends_desc, n16cluster_flowers_desc]
graph_desc_dict = dict(zip(graph_names, graph_desc_list))


def path_rooms(start, end):
    start = "room " + start
    end = "room " + end
    return f"From {start}, what is the shortest path to {end}? Starting from {start}, please only list the room numbers in order, including {start}, separated by commas. Answer: "

def path_friends(start, end):
    return f"From {start}, what is the shortest path to {end}? Starting from {start}, please only list the people's names in order, including {start}, separated by commas. Answer: "

def path_flowers(start, end):
    start = start.lower()
    start_section = f"the {start.lower()} section"
    end = f"the {end.lower()} section"
    return f"From {start_section}, what is the shortest path to {end}? Starting from {start}, please only list the flower names in order, including {start}, separated by commas. Answer:"

def path_rooms_prime(graph, start, end):
    return_list = []
    answer = graph.find_shortest_path(start, end)
    start = "room " + start
    end = "room " + end
    question = f"From {start}, what is the shortest path to {end}? Starting from {start}, please only list the room numbers in order, including {start}, separated by commas. Answer: "
    return_list.append(question)
    return_list.append(answer)
    return return_list

def path_friends_prime(graph, start, end):
    return_list = []
    answer = graph.find_shortest_path(start, end)
    question = f"From {start}, what is the shortest path to {end}? Starting from {start}, please only list the people's names in order, including {start}, separated by commas. Answer: "
    return_list.append(question)
    return_list.append(answer)
    return return_list

def path_flowers_prime(graph, start, end):
    return_list = []
    answer = graph.find_shortest_path(start, end)
    start = start.lower()
    start_section = f"the {start.lower()} section"
    end = f"the {end.lower()} section"
    question = f"From {start_section}, what is the shortest path to {end}? Starting from {start}, please only list the flower names in order, including {start}, separated by commas. Answer: "
    return_list.append(question)
    return_list.append(answer)
    return return_list


def no_prime_question(graph, graph_string, start, end):
    desc = graph_desc_dict[graph_string]
  
    if "rooms" in graph_string: # rooms
      path_question = path_rooms(start, end)
    elif "friends" in graph_string: # friends
      path_question = path_friends(start, end)
    elif "flowers" in graph_string: # flowers
      path_question = path_flowers(start, end)
    else:
      path_question = ""

    return (f"Consider the folowing scenario. {desc} {path_question}")

# [0]: prime_question, [1]: prime_answer, [2]: path_question
def both_prime_question(graph, graph_string, start, end, start_prime, end_prime):
    return_list = []
    desc = graph_desc_dict[graph_string]
    prime_desc = desc
    if "rooms" in graph_string: # rooms
      prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(graph, start_prime, end_prime)[0]}"
      return_list.append(prime_question)
      prime_answer = path_rooms_prime(graph, start_prime, end_prime)[1]
      return_list.append(prime_answer)
      path_question = f"Now, consider the following scenario. {desc} {path_rooms(start, end)}"
      return_list.append(path_question)
    elif "friends" in graph_string: # friends
      prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(graph, start_prime, end_prime)[0]}"
      return_list.append(prime_question)
      prime_answer = path_friends_prime(graph, start_prime, end_prime)[1]
      return_list.append(prime_answer)
      path_question = f"Now, consider the following scenario. {desc} {path_friends(start, end)}"
      return_list.append(path_question)
    elif "flowers" in graph_string: # flowers
      prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(graph, start_prime, end_prime)[0]}"
      return_list.append(prime_question)
      prime_answer = path_flowers_prime(graph, start_prime, end_prime)[1]
      return_list.append(prime_answer)
      path_question = f"Now, consider the following scenario. {desc} {path_flowers(start, end)}"
      return_list.append(path_question)
    
    return return_list

# [0]: prime_question, [1]: prime_answer, [2]: path_question
def lexical_prime_question(graph, graph_name, start, end):

    lexical = graph_name.split('_')[1]
    graph_desc_string = graph_desc_dict[graph_name]
    return_list = []

    n7line_prime_graph = graph_dict["n7line_" + lexical]
    n7line_prime_graph_nodes = n7line_prime_graph.select_random_nodes(2)
    n7line_prime_graph_start = n7line_prime_graph_nodes[0]
    n7line_prime_graph_end = n7line_prime_graph_nodes[1]
    if len(n7line_prime_graph.find_shortest_path(n7line_prime_graph_start, n7line_prime_graph_end)):
      n7line_prime_graph_nodes = n7line_prime_graph.select_random_nodes(2)
      n7line_prime_graph_start = n7line_prime_graph_nodes[0]
      n7line_prime_graph_end = n7line_prime_graph_nodes[1]

    n7tree_prime_graph = graph_dict["n7tree_" + lexical]
    n7tree_prime_graph_nodes = n7tree_prime_graph.select_random_nodes(2)
    n7tree_prime_graph_start = n7tree_prime_graph_nodes[0]
    n7tree_prime_graph_end = n7tree_prime_graph_nodes[1]
    if len(n7tree_prime_graph.find_shortest_path(n7tree_prime_graph_start, n7tree_prime_graph_end)):
      n7tree_prime_graph_nodes = n7tree_prime_graph.select_random_nodes(2)
      n7tree_prime_graph_start = n7tree_prime_graph_nodes[0]
      n7tree_prime_graph_end = n7tree_prime_graph_nodes[1]

    n13line_prime_graph = graph_dict["n13line_" + lexical]
    n13line_prime_graph_nodes = n13line_prime_graph.select_random_nodes(2)
    n13line_prime_graph_start = n13line_prime_graph_nodes[0]
    n13line_prime_graph_end = n13line_prime_graph_nodes[1]
    if len(n13line_prime_graph.find_shortest_path(n13line_prime_graph_start, n13line_prime_graph_end)):
      n13line_prime_graph_nodes = n13line_prime_graph.select_random_nodes(2)
      n13line_prime_graph_start = n13line_prime_graph_nodes[0]
      n13line_prime_graph_end = n13line_prime_graph_nodes[1]

    n15star_prime_graph = graph_dict["n15star_" + lexical]
    n15star_prime_graph_nodes = n15star_prime_graph.select_random_nodes(2)
    n15star_prime_graph_start = n15star_prime_graph_nodes[0]
    n15star_prime_graph_end = n15star_prime_graph_nodes[1]
    if len(n15star_prime_graph.find_shortest_path(n15star_prime_graph_start, n15star_prime_graph_end)):
      n15star_prime_graph_nodes = n15star_prime_graph.select_random_nodes(2)
      n15star_prime_graph_start = n15star_prime_graph_nodes[0]
      n15star_prime_graph_end = n15star_prime_graph_nodes[1]

    n16cluster_prime_graph = graph_dict["n16cluster_" + lexical]
    n16cluster_prime_graph_nodes = n16cluster_prime_graph.select_random_nodes(2)
    n16cluster_prime_graph_start = n16cluster_prime_graph_nodes[0]
    n16cluster_prime_graph_end = n16cluster_prime_graph_nodes[1]
    if len(n16cluster_prime_graph.find_shortest_path(n16cluster_prime_graph_start, n16cluster_prime_graph_end)):
      n16cluster_prime_graph_nodes = n16cluster_prime_graph.select_random_nodes(2)
      n16cluster_prime_graph_start = n16cluster_prime_graph_nodes[0]
      n16cluster_prime_graph_end = n16cluster_prime_graph_nodes[1]


    if lexical == "rooms":

      if "n7line" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n13line
          prime_desc = n13line_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)

        elif rand > 0.5 and rand < 0.75: #n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)

        else: # n15star
          prime_desc = n15star_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_rooms(start, end)}"
        return_list.append(path_question)

      elif "n7tree" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n13line
          prime_desc = n13line_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n15star
          prime_desc = n15star_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_rooms(start, end)}"
        return_list.append(path_question)

      elif "n13line" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n15star
          prime_desc = n15star_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_rooms(start, end)}"
        return_list.append(path_question)

      elif "n15star" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n13line
          prime_desc = n13line_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_rooms(start, end)}"
        return_list.append(path_question)

      elif "n16cluster" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n15star
          prime_desc = n15star_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n13line
          prime_desc = n13line_prime_graph.generate_description_rooms()
          prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_rooms(start, end)}"
        return_list.append(path_question)

    elif lexical == "friends":

      if "n7line" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n13line
          prime_desc = n13line_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)

        elif rand > 0.5 and rand < 0.75: #n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)

        else: # n15star
          prime_desc = n15star_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_friends(start, end)}"
        return_list.append(path_question)

      elif "n7tree" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n13line
          prime_desc = n13line_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n15star
          prime_desc = n15star_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_friends(start, end)}"
        return_list.append(path_question)

      elif "n13line" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n15star
          prime_desc = n15star_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_friends(start, end)}"
        return_list.append(path_question)

      elif "n15star" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n13line
          prime_desc = n13line_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_friends(start, end)}"
        return_list.append(path_question)

      elif "n16cluster" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n15star
          prime_desc = n15star_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n13line
          prime_desc = n13line_prime_graph.generate_description_friends()
          prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_friends(start, end)}"
        return_list.append(path_question)

    elif lexical == "flowers":

      if "n7line" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n13line
          prime_desc = n13line_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)

        elif rand > 0.5 and rand < 0.75: #n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)

        else: # n15star
          prime_desc = n15star_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_flowers(start, end)}"
        return_list.append(path_question)

      elif "n7tree" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n13line
          prime_desc = n13line_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n15star
          prime_desc = n15star_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_flowers(start, end)}"
        return_list.append(path_question)

      elif "n13line" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n15star
          prime_desc = n15star_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_flowers(start, end)}"
        return_list.append(path_question)

      elif "n15star" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n16cluster
          prime_desc = n16cluster_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n16cluster_prime_graph, n16cluster_prime_graph_start, n16cluster_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n13line
          prime_desc = n13line_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_flowers(start, end)}"
        return_list.append(path_question)

      elif "n16cluster" in graph_name:
        rand = np.random.rand()

        if rand < 0.25: # n7line
          prime_desc = n7line_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.5 and rand > 0.25: # n7tree
          prime_desc = n7tree_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        elif rand < 0.75 and rand > 0.5: # n15star
          prime_desc = n15star_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)[1]
          return_list.append(prime_answer)
        
        else: # n13line
          prime_desc = n13line_prime_graph.generate_description_flowers()
          prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[0]}"
          return_list.append(prime_question)
          prime_answer = path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)[1]
          return_list.append(prime_answer)
          
        path_question = f"Now consider the following scenario. {graph_desc_string} {path_flowers(start, end)}"
        return_list.append(path_question)
    

    return return_list

# [0]: prime_question, [1]: prime_answer, [2]: path_question, [3]: prime_graph_string
def structural_prime_questions(graph, graph_string, start, end, rooms_prime_graph_start, rooms_prime_graph_end, friends_prime_graph_start, friends_prime_graph_end, flower_prime_graph_start, flower_prime_graph_end):
    structure = graph_string.split('_')[0]
    return_list = []
    graph_desc_string = graph_desc_dict[graph_string]
    rooms_prime_graph = graph_dict[structure + "_rooms"]
    friends_prime_graph = graph_dict[structure + "_friends"]
    flower_prime_graph = graph_dict[structure + "_flowers"]

    if "rooms" in graph_string: # rooms

      if np.random.rand() > .5: # flowers
        prime_graph_string = structure + "_flowers"
        prime_desc = flower_prime_graph.generate_description_flowers()
        prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(flower_prime_graph, flower_prime_graph_start, flower_prime_graph_end)[0]}"
        return_list.append(prime_question)
        prime_answer = path_flowers_prime(flower_prime_graph, flower_prime_graph_start, flower_prime_graph_end)[1]
        return_list.append(prime_answer)

      else: # friends
        prime_graph_string = structure + "_friends"
        prime_desc = friends_prime_graph.generate_description_friends()
        prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(friends_prime_graph, friends_prime_graph_start, friends_prime_graph_end)[0]}"
        return_list.append(prime_question)
        prime_answer = path_friends_prime(friends_prime_graph, friends_prime_graph_start, friends_prime_graph_end)[1]
        return_list.append(prime_answer)

      path_question = f"Now consider the following scenario. {graph_desc_string} {path_rooms(start, end)}"
      return_list.append(path_question)

    elif "friends" in graph_string: # friends

      if np.random.rand() > .5: # flowers
        prime_graph_string = structure + "_flowers"
        prime_desc = flower_prime_graph.generate_description_flowers()
        prime_question = f"Consider the following scenario. {prime_desc} {path_flowers_prime(flower_prime_graph, flower_prime_graph_start, flower_prime_graph_end)[0]}"
        return_list.append(prime_question)
        prime_answer = path_flowers_prime(flower_prime_graph, flower_prime_graph_start, flower_prime_graph_end)[1]
        return_list.append(prime_answer)

      else: # rooms
        prime_graph_string = structure + "_rooms"
        prime_desc = rooms_prime_graph.generate_description_rooms()
        prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(rooms_prime_graph, rooms_prime_graph_start, rooms_prime_graph_end)[0]}"
        return_list.append(prime_question)
        prime_answer = path_rooms_prime(rooms_prime_graph, rooms_prime_graph_start, rooms_prime_graph_end)[1]
        return_list.append(prime_answer)

      path_question = f"Now consider the following scenario. {graph_desc_string} {path_friends(start, end)}"
      return_list.append(path_question)

    elif "flowers" in graph_string: # flowers

      if np.random.rand() > .5: # friends
        prime_graph_string = structure + "_friends"
        prime_desc = friends_prime_graph.generate_description_friends()
        prime_question = f"Consider the following scenario. {prime_desc} {path_friends_prime(friends_prime_graph, friends_prime_graph_start, friends_prime_graph_end)[0]}"
        return_list.append(prime_question)
        prime_answer = path_friends_prime(friends_prime_graph, friends_prime_graph_start, friends_prime_graph_end)[1]
        return_list.append(prime_answer)

      else: # rooms
        prime_graph_string = structure + "_rooms"
        prime_desc = rooms_prime_graph.generate_description_rooms()
        prime_question = f"Consider the following scenario. {prime_desc} {path_rooms_prime(rooms_prime_graph, rooms_prime_graph_start, rooms_prime_graph_end)[0]}"
        return_list.append(prime_question)
        prime_answer = path_rooms_prime(rooms_prime_graph, rooms_prime_graph_start, rooms_prime_graph_end)[1]
        return_list.append(prime_answer)

      path_question = f"Now consider the following scenario. {graph_desc_string} {path_flowers(start, end)}"
      return_list.append(path_question)
      return_list.append(prime_graph_string)

    return return_list

# [0]: prime_question, [1]: prime_answer, [2]: path_question, [3]: prime_graph_string
def unrelated_prime_question(graph, graph_string, start, end):
  structure = graph_string.split('_')[0]
  return_list = []
  
  if structure == 'n7line':
    rand = np.random.rand()
    if rand < 0.25: # n16cluster
      alt_struct = 'n16cluster'
    elif rand < 0.5 and rand > 0.25: # n7tree
      alt_struct = 'n7tree'
    elif rand > 0.5 and rand < 0.75: # n15star
      alt_struct = 'n15star'
    else: # n13line
      alt_struct = 'n13line'
  
  elif structure == 'n7tree':
    rand = np.random.rand()
    if rand < 0.25: # n7line
      alt_struct = 'n7line'
    elif rand < 0.5 and rand > 0.25: # n16cluster
      alt_struct = 'n16cluster'
    elif rand > 0.5 and rand < 0.75: # n15star
      alt_struct = 'n15star'
    else: # n13line
      alt_struct = 'n13line'
  
  elif structure == 'n13line':
    rand = np.random.rand()
    if rand < 0.25: # n7line
      alt_struct = 'n7line'
    elif rand < 0.5 and rand > 0.25: # n7tree
      alt_struct = 'n7tree'
    elif rand > 0.5 and rand < 0.75: # n15star
      alt_struct = 'n15star'
    else: # n16cluster
      alt_struct = 'n16cluster'
 
  elif structure == 'n15star':
    rand = np.random.rand()
    if rand < 0.25: # n7line
      alt_struct = 'n7line'
    elif rand < 0.5 and rand > 0.25: # n7tree
      alt_struct = 'n7tree'
    elif rand > 0.5 and rand < 0.75: # n16cluster
      alt_struct = 'n16cluster'
    else: # n13line
      alt_struct = 'n13line'
  
  elif structure == 'n16cluster':
    rand = np.random.rand()
    if rand < 0.25: # n7line
      alt_struct = 'n7line'
    elif rand < 0.5 and rand > 0.25: # n7tree
      alt_struct = 'n7tree'
    elif rand > 0.5 and rand < 0.75: # n15star
      alt_struct = 'n15star'
    else: # n13line
      alt_struct = 'n13line'

  
  lexical = graph_string.split('_')[1]
  if lexical == 'rooms':
    path_question = path_rooms(start, end)
    rand = np.random.rand()
    if rand < 0.5:
      alt_lex = 'friends'
    elif rand > 0.5:
      alt_lex = 'flowers'
  elif lexical == 'friends':
    path_question = path_friends(start, end)
    rand = np.random.rand()
    if rand < 0.5:
      alt_lex = 'rooms'
    elif rand  > 0.5:
      alt_lex = 'flowers'
  elif lexical == 'flowers':
    path_question = path_flowers(start, end)
    rand = np.random.rand()
    if rand < 0.5:
      alt_lex = 'rooms'
    elif rand  > 0.5:
      alt_lex = 'friends'
  
  graph_desc_string = graph_desc_dict[graph_string]
  prime_graph_string = alt_struct + '_' + alt_lex
  prime_graph = graph_dict[prime_graph_string]
  prime_graph_desc_string = graph_desc_dict[prime_graph_string]

  prime_graph_nodes = prime_graph.select_random_nodes(2)
  prime_graph_start = prime_graph_nodes[0]
  prime_graph_end = prime_graph_nodes[1]

  if alt_lex == 'rooms':
    prime_question = f"Consider the following scenario. {prime_graph_desc_string} {path_rooms_prime(prime_graph, prime_graph_start, prime_graph_end)[0]}"
    return_list.append(prime_question)
    prime_answer = path_rooms_prime(prime_graph, prime_graph_start, prime_graph_end)[1]
    return_list.append(prime_answer)

  elif alt_lex == 'friends':
    prime_question = f"Consider the following scenario. {prime_graph_desc_string} {path_friends_prime(prime_graph, prime_graph_start, prime_graph_end)[0]}"
    return_list.append(prime_question)
    prime_answer = path_friends_prime(prime_graph, prime_graph_start, prime_graph_end)[1]
    return_list.append(prime_answer)

  elif alt_lex == 'flowers':
    prime_question = f"Consider the following scenario. {prime_graph_desc_string} {path_flowers_prime(prime_graph, prime_graph_start, prime_graph_end)[0]}"
    return_list.append(prime_question)
    prime_answer = path_flowers_prime(prime_graph, prime_graph_start, prime_graph_end)[1]
    return_list.append(prime_answer)

  full_path_question = f"Now consider the following scenario. {graph_desc_string} {path_question}"
  return_list.append(full_path_question)
  return_list.append(prime_graph_string)
  
  return return_list

for graph_title in graph_names:
  for i in range(100):

    graph_name = graph_title

    file_path = f"{graph_name}_questions.jsonl"
    graph = graph_dict[graph_name]
    graph_desc_string = graph_desc_dict[graph_name]

    nodes = graph.select_random_nodes(4)
    start = nodes[0]
    end = nodes[1]
    start_prime = nodes[2]
    end_prime = nodes[3]
    
    if len(graph.find_shortest_path(start, end)) == 2 or len(graph.find_shortest_path(start_prime, end_prime)):
      nodes = graph.select_random_nodes(4)
      start = nodes[0]
      end = nodes[1]
      start_prime = nodes[2]
      end_prime = nodes[3]

    rooms_graph_name = f"{graph_name.split('_')[0]}_rooms"
    rooms_graph = graph_dict[rooms_graph_name]
    rooms_nodes = rooms_graph.select_random_nodes(2)
    rooms_prime_graph_start = rooms_nodes[0]
    rooms_prime_graph_end = rooms_nodes[1]
    if len(rooms_graph.find_shortest_path(rooms_prime_graph_start, rooms_prime_graph_end)) == 2:
      rooms_nodes = rooms_graph.select_random_nodes(2)
      rooms_prime_graph_start = rooms_nodes[0]
      rooms_prime_graph_end = rooms_nodes[1]

    friend_graph_name = f"{graph_name.split('_')[0]}_friends"
    friend_graph = graph_dict[friend_graph_name]
    friend_nodes = friend_graph.select_random_nodes(2)
    friends_prime_graph_start = friend_nodes[0]
    friends_prime_graph_end = friend_nodes[1]
    if len(friend_graph.find_shortest_path(friends_prime_graph_start, friends_prime_graph_end)) == 2:
      friend_nodes = friend_graph.select_random_nodes(2)
      friends_prime_graph_start = friend_nodes[0]
      friends_prime_graph_end = friend_nodes[1]


    flower_graph_name = f"{graph_name.split('_')[0]}_flowers"
    flower_graph = graph_dict[flower_graph_name]
    flower_nodes = flower_graph.select_random_nodes(2)
    flower_prime_graph_start = flower_nodes[0]
    flower_prime_graph_end = flower_nodes[1]
    if len(flower_graph.find_shortest_path(flower_prime_graph_start, flower_prime_graph_end)) == 2:
      flower_nodes = flower_graph.select_random_nodes(2)
      flower_prime_graph_start = flower_nodes[0]
      flower_prime_graph_end = flower_nodes[1]

    shortest_path = graph.find_shortest_path(start, end)


  # [0]: prime_question, [1]: prime_answer, [2]: path_question, [3]: prime_graph_string

    json_dict = {
                      "Graph": graph_name,

                      "No Prime Question": no_prime_question(graph, graph_name, start, end),
                      "No Prime Question Answer": shortest_path,
                      
                      "Both Prime Question User1": both_prime_question(graph, graph_name, start, end, start_prime, end_prime)[0],
                      "Both Prime Question Assistant": both_prime_question(graph, graph_name, start, end, start_prime, end_prime)[1],
                      "Both Prime Question User2": both_prime_question(graph, graph_name, start, end, start_prime, end_prime)[2],
                      "Both Prime Question Answer": shortest_path,
                      
                      "Lexical Prime Question User1": lexical_prime_question(graph, graph_name, start, end)[0],
                      "Lexical Prime Question Assistant": lexical_prime_question(graph, graph_name, start, end)[1],
                      "Lexical Prime Question User2": lexical_prime_question(graph, graph_name, start, end)[2],
                      "Lexical Prime Question Answer": shortest_path,
                      
                      "Structural Prime Question User1": structural_prime_questions(graph, graph_name, start, end, rooms_prime_graph_start, rooms_prime_graph_end, friends_prime_graph_start, friends_prime_graph_end, flower_prime_graph_start, flower_prime_graph_end)[0],
                      "Structural Prime Question Assistant": structural_prime_questions(graph, graph_name, start, end, rooms_prime_graph_start, rooms_prime_graph_end, friends_prime_graph_start, friends_prime_graph_end, flower_prime_graph_start, flower_prime_graph_end)[1],
                      "Structural Prime Question User2": structural_prime_questions(graph, graph_name, start, end, rooms_prime_graph_start, rooms_prime_graph_end, friends_prime_graph_start, friends_prime_graph_end, flower_prime_graph_start, flower_prime_graph_end)[2],
                      "Structural Prime Question Answer": shortest_path,
                      
                      "Unrelated Prime Question User1": unrelated_prime_question(graph, graph_name, start, end)[0],
                      "Unrelated Prime Question Assistant": unrelated_prime_question(graph, graph_name, start, end)[1],
                      "Unrelated Prime Question User2": unrelated_prime_question(graph, graph_name, start, end)[2],
                      "Unrelated Prime Question Answer": shortest_path,
                  }



    with open(file_path, 'a') as outfile:
          json_string = json.dumps(json_dict)
          outfile.write(json_string + '\n')