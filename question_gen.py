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
n15star_flowers.add_node("Hyancinth")
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
n15star_flowers.connect_nodes("Poppy", "Hyancinth")
n15star_flowers.connect_nodes("Marigold", "Lily")
n15star_flowers.connect_nodes("Marigold", "Hyancinth")
n15star_flowers.connect_nodes("Lily", "Hyancinth")
n15star_flowers.connect_nodes("Daffodil", "Hyancinth")
n15star_flowers_desc = n15star_flowers.generate_description_flowers()
# print(n15star_flowers_desc)


graph_names = ["n7line_rooms", "n7line_friends", "n7line_flowers", "n7tree_rooms", "n7tree_friends", "n7tree_flowers", "n13line_rooms", "n13line_friends", "n13line_flowers", "n15star_rooms", "n15star_friends", "n15star_flowers"]
graph_list = [n7line_rooms, n7line_friends, n7line_flowers, n7tree_rooms, n7tree_friends, n7tree_flowers, n13line_rooms, n13line_friends, n13line_flowers, n15star_rooms, n15star_friends, n15star_flowers]
graph_dict = dict(zip(graph_names, graph_list))

graph_desc_list = [n7line_rooms_desc, n7line_friends_desc, n7line_flowers_desc, n7tree_rooms_desc, n7tree_friends_desc, n7tree_flowers_desc, n13line_rooms_desc, n13line_friends_desc, n13line_flowers_desc, n15star_rooms_desc, n15star_friends_desc, n15star_flowers_desc]
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
    answer = graph.find_shortest_path(start, end)
    start = "room " + start
    end = "room " + end
    return f"From {start}, what is the shortest path to {end}? Starting from {start}, please only list the room numbers in order, including {start}, separated by commas. Answer: {answer}"

def path_friends_prime(graph, start, end):
    answer = graph.find_shortest_path(start, end)
    return f"From {start}, what is the shortest path to {end}? Starting from {start}, please only list the people's names in order, including {start}, separated by commas. Answer: {answer}"

def path_flowers_prime(graph, start, end):
    answer = graph.find_shortest_path(start, end)
    start = start.lower()
    start_section = f"the {start.lower()} section"
    end = f"the {end.lower()} section"
    return f"From {start_section}, what is the shortest path to {end}? Starting from {start}, please only list the flower names in order, including {start}, separated by commas. Answer: {answer}"



def no_prime_question(graph, graph_string, start, end):
    if "rooms" in graph_string: # rooms
      path_question = path_rooms(start, end)
    elif "friends" in graph_string: # friends
      path_question = path_friends(start, end)
    elif "flowers" in graph_string: # flowers
      path_question = path_flowers(start, end)
    else:
      path_question = ""

    return path_question

def both_prime_question(graph, graph_string, start, end, start_prime, end_prime):
    desc = graph_desc_dict[graph_string]
    if "rooms" in graph_string: # rooms
      prime = path_rooms_prime(graph, start_prime, end_prime)
      path_question = path_rooms(start, end)
    elif "friends" in graph_string: # friends
      prime = path_friends_prime(graph, start_prime, end_prime)
      path_question = path_friends(start, end)
    elif "flowers" in graph_string: # flowers
      prime = path_flowers_prime(graph, start_prime, end_prime)
      path_question = path_flowers(start, end)
    else:
      prime = ""
      path_question = ""

    return(f"{desc} {prime} {path_question}")

def lexical_prime_question(graph, graph_name, start, end):

    lexical = graph_name.split('_')[1]
    graph_desc_string = graph_desc_dict[graph_name]

    n7line_prime_graph = graph_dict["n7line_" + lexical]
    n7line_prime_graph_nodes = n7line_prime_graph.select_random_nodes(2)
    n7line_prime_graph_start = n7line_prime_graph_nodes[0]
    n7line_prime_graph_end = n7line_prime_graph_nodes[1]

    n7tree_prime_graph = graph_dict["n7tree_" + lexical]
    n7tree_prime_graph_nodes = n7tree_prime_graph.select_random_nodes(2)
    n7tree_prime_graph_start = n7tree_prime_graph_nodes[0]
    n7tree_prime_graph_end = n7tree_prime_graph_nodes[1]

    n13line_prime_graph = graph_dict["n13line_" + lexical]
    n13line_prime_graph_nodes = n13line_prime_graph.select_random_nodes(2)
    n13line_prime_graph_start = n13line_prime_graph_nodes[0]
    n13line_prime_graph_end = n13line_prime_graph_nodes[1]

    n15star_prime_graph = graph_dict["n15star_" + lexical]
    n15star_prime_graph_nodes = n15star_prime_graph.select_random_nodes(2)
    n15star_prime_graph_start = n15star_prime_graph_nodes[0]
    n15star_prime_graph_end = n15star_prime_graph_nodes[1]

    if lexical == "rooms":

      if "n7line" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7tree
          # print("prime: n7tree")
          prime = path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)
          prime_desc = n7tree_prime_graph.generate_description_rooms()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n13line")
          prime = path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)
          prime_desc = n13line_prime_graph.generate_description_rooms()
        else: # n15star
          # print("prime: n15star")
          prime = path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)
          prime_desc = n15star_prime_graph.generate_description_rooms()
        path_question = path_rooms(start, end)

      elif "n7tree" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7line
          # print("prime: n7line")
          prime = path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)
          prime_desc = n7line_prime_graph.generate_description_rooms()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n13line")
          prime = path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)
          prime_desc = n13line_prime_graph.generate_description_rooms()
        else: # n15star
          # print("prime: n15star")
          prime = path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)
          prime_desc = n15star_prime_graph.generate_description_rooms()

        path_question = path_rooms(start, end)

      elif "n13line" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7line
          # print("prime: n7line")
          prime = path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)
          prime_desc = n7line_prime_graph.generate_description_rooms()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n7tree")
          prime = path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)
          prime_desc = n7tree_prime_graph.generate_description_rooms()
        else: # n15star
          # print("prime: n15star")
          prime = path_rooms_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)
          prime_desc = n15star_prime_graph.generate_description_rooms()

        path_question = path_rooms(start, end)

      elif "n15star" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7line
          # print("prime: n7line")
          prime = path_rooms_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)
          prime_desc = n7line_prime_graph.generate_description_rooms()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n13line")
          prime = path_rooms_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)
          prime_desc = n13line_prime_graph.generate_description_rooms()
        else: # n7tree
          # print("prime: n7tree")
          prime = path_rooms_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)
          prime_desc = n7tree_prime_graph.generate_description_rooms()
        path_question = path_rooms(start, end)

      else:
        prime = ""
        path_question = ""


    elif lexical == "friends":

      if "n7line" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7tree
          # print("prime: n7tree")
          prime = path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)
          prime_desc = n7tree_prime_graph.generate_description_friends()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n13line")
          prime = path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)
          prime_desc = n13line_prime_graph.generate_description_friends()
        else: # n15star
          # print("prime: n15star")
          prime = path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)
          prime_desc = n15star_prime_graph.generate_description_friends()

        path_question = path_friends(start, end)

      elif "n7tree" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7line
          # print("prime: n7line")
          prime = path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)
          prime_desc = n7line_prime_graph.generate_description_friends()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n13line")
          prime = path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)
          prime_desc = n13line_prime_graph.generate_description_friends()
        else: # n15star
          # print("prime: n15star")
          prime = path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)
          prime_desc = n15star_prime_graph.generate_description_friends()

        path_question = path_friends(start, end)

      elif "n13line" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7line
          # print("prime: n7line")
          prime = path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)
          prime_desc = n7line_prime_graph.generate_description_friends()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n7tree")
          prime = path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)
          prime_desc = n7tree_prime_graph.generate_description_friends()
        else: # n15star
          # print("prime: n15star")
          prime = path_friends_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)
          prime_desc = n15star_prime_graph.generate_description_friends()

        path_question = path_friends(start, end)

      elif "n15star" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7line
          # print("prime: n7line")
          prime = path_friends_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)
          prime_desc = n7line_prime_graph.generate_description_friends()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n13line")
          prime = path_friends_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)
          prime_desc = n13line_prime_graph.generate_description_friends()
        else: # n7tree
          # print("prime: n7tree")
          prime = path_friends_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)
          prime_desc = n7tree_prime_graph.generate_description_friends()

        path_question = path_friends(start, end)

      else:
        prime = ""
        path_question = ""


    elif lexical == "flowers":

      if "n7line" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7tree
          # print("prime: n7tree")
          prime = path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)
          prime_desc = n7tree_prime_graph.generate_description_flowers()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n13line")
          prime = path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)
          prime_desc = n13line_prime_graph.generate_description_flowers()
        else: # n15star
          # print("prime: n15star")
          prime = path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)
          prime_desc = n15star_prime_graph.generate_description_flowers()

        path_question = path_flowers(start, end)

      elif "n7tree" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7line
          # print("prime: n7line")
          prime = path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)
          prime_desc = n7line_prime_graph.generate_description_flowers()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n13line")
          prime = path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)
          prime_desc = n13line_prime_graph.generate_description_flowers()
        else: # n15star
          # print("prime: n15star")
          prime = path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)
          prime_desc = n15star_prime_graph.generate_description_flowers()

        path_question = path_flowers(start, end)

      elif "n13line" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7line
          # print("prime: n7line")
          prime = path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)
          prime_desc = n7line_prime_graph.generate_description_flowers()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n7tree")
          prime = path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)
          prime_desc = n7tree_prime_graph.generate_description_flowers()
        else: # n15star
          # print("prime: n15star")
          prime = path_flowers_prime(n15star_prime_graph, n15star_prime_graph_start, n15star_prime_graph_end)
          prime_desc = n15star_prime_graph.generate_description_flowers()

        path_question = path_flowers(start, end)

      elif "n15star" in graph_name:
        rand = np.random.rand()

        if rand < 0.33: # n7line
          # print("prime: n7line")
          prime = path_flowers_prime(n7line_prime_graph, n7line_prime_graph_start, n7line_prime_graph_end)
          prime_desc = n7line_prime_graph.generate_description_flowers()
        elif rand < 0.66 and rand > 0.33: # n13line
          # print("prime: n13line")
          prime = path_flowers_prime(n13line_prime_graph, n13line_prime_graph_start, n13line_prime_graph_end)
          prime_desc = n13line_prime_graph.generate_description_flowers()
        else: # n7tree
          # print("prime: n7tree")
          prime = path_flowers_prime(n7tree_prime_graph, n7tree_prime_graph_start, n7tree_prime_graph_end)
          prime_desc = n7tree_prime_graph.generate_description_flowers()
        path_question = path_flowers(start, end)

      else:
        prime = ""
        path_question = ""

    else:
      prime = ""
      path_question = ""

    return(f"{prime_desc} {prime} {graph_desc_string} {path_question}")

def structural_prime_questions(graph, graph_string, start, end, rooms_prime_graph_start, rooms_prime_graph_end, friends_prime_graph_start, friends_prime_graph_end, flower_prime_graph_start, flower_prime_graph_end):
    structure = graph_string.split('_')[0]
    graph_desc_string = graph_desc_dict[graph_string]
    rooms_prime_graph = graph_dict[structure + "_rooms"]
    friends_prime_graph = graph_dict[structure + "_friends"]
    flower_prime_graph = graph_dict[structure + "_flowers"]

    if "rooms" in graph_string: # rooms

      if np.random.rand() > .5: # flowers
        # print("prime: flowers")
        prime = path_flowers_prime(flower_prime_graph, flower_prime_graph_start, flower_prime_graph_end)
        prime_desc = flower_prime_graph.generate_description_flowers()
      else: # friends
        # print("prime: friends")
        prime = path_friends_prime(friends_prime_graph, friends_prime_graph_start, friends_prime_graph_end)
        prime_desc = friends_prime_graph.generate_description_friends()

      path_question = path_rooms(start, end)

    elif "friends" in graph_string: # friends

      if np.random.rand() > .5: # flowers
        # print("prime: flowers")
        prime = path_flowers_prime(flower_prime_graph, flower_prime_graph_start, flower_prime_graph_end)
        prime_desc = flower_prime_graph.generate_description_flowers()
      else: # rooms
        # print("prime: rooms")
        prime = path_rooms_prime(rooms_prime_graph, rooms_prime_graph_start, rooms_prime_graph_end)
        prime_desc = rooms_prime_graph.generate_description_rooms()

      path_question = path_friends(start, end)

    elif "flowers" in graph_string: # flowers

      if np.random.rand() > .5: # room
        # print("prime: rooms")
        prime = path_rooms_prime(rooms_prime_graph, rooms_prime_graph_start, rooms_prime_graph_end)
        prime_desc = rooms_prime_graph.generate_description_rooms()
      else: # friends
        # print("prime: friends")
        prime = path_friends_prime(friends_prime_graph, friends_prime_graph_start, friends_prime_graph_end)
        prime_desc = friends_prime_graph.generate_description_friends()

      path_question = path_flowers(start, end)

    else:
      prime = ""
      path_question = ""

    return(f"{prime_desc} {prime} {graph_desc_string} {path_question}")

# file_path = "n13line_rooms_questions.jsonl"
file_path = "n15star_flowers_questions.jsonl"

for i in range(10):

  # graph_name = "n13line_rooms"
  graph_name = "n15star_flowers"
  graph = graph_dict[graph_name]
  graph_desc_string = graph_desc_dict[graph_name]


  nodes = graph.select_random_nodes(4)
  start = nodes[0]
  end = nodes[1]
  start_prime = nodes[2]
  end_prime = nodes[3]

  rooms_prime_graph_start = start_prime
  rooms_prime_graph_end = end_prime

  # rooms_graph_name = "n13line_rooms"
  rooms_graph_name = "n15star_rooms"
  rooms_graph = graph_dict[rooms_graph_name]
  rooms_nodes = rooms_graph.select_random_nodes(2)
  rooms_prime_graph_start = rooms_nodes[0]
  rooms_prime_graph_end = rooms_nodes[1]

  # friend_graph_name = "n13line_friends"
  friend_graph_name = "n15star_friends"
  friend_graph = graph_dict[friend_graph_name]
  friend_nodes = friend_graph.select_random_nodes(2)
  friends_prime_graph_start = friend_nodes[0]
  friends_prime_graph_end = friend_nodes[1]

  # flower_graph_name = "n13line_flowers"
  flower_graph_name = "n15star_flowers"
  flower_graph = graph_dict[flower_graph_name]
  flower_nodes = flower_graph.select_random_nodes(2)
  flower_prime_graph_start = flower_nodes[0]
  flower_prime_graph_end = flower_nodes[1]

  shortest_path = graph.find_shortest_path(start, end)



  json_dict = {
                    "Graph": graph_name,
                    "Description": graph_desc_string,
                    "No Prime Question": no_prime_question(graph, graph_name, start, end),
                    "No Prime Question Answer": shortest_path,
                    "Both Prime Question": both_prime_question(graph, graph_name, start, end, start_prime, end_prime),
                    "Both Prime Question Answer": shortest_path,
                    "Lexical Prime Question": lexical_prime_question(graph, graph_name, start, end),
                    "Lexical Prime Question Answer": shortest_path,
                    "Structural Prime Question": structural_prime_questions(graph, graph_name, start, end, rooms_prime_graph_start, rooms_prime_graph_end, friends_prime_graph_start, friends_prime_graph_end, flower_prime_graph_start, flower_prime_graph_end),
                    "Structural Prime Question Answer": shortest_path,
                }


  with open(file_path, 'a') as outfile:
        json_string = json.dumps(json_dict)
        outfile.write(json_string + '\n')